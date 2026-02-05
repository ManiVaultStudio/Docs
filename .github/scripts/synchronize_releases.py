#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import sys
import urllib.request
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple


@dataclass(frozen=True)
class Release:
    tag_name: str
    name: str
    body: str
    html_url: str
    published_at: Optional[str]
    draft: bool
    prerelease: bool


def gh_api_get(url: str, token: str) -> Tuple[List[Dict[str, Any]], Dict[str, str]]:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "mv-release-notes-sync",
        },
        method="GET",
    )
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        headers = {k.lower(): v for k, v in resp.headers.items()}
        return data, headers


def parse_link_header(link_value: str) -> Dict[str, str]:
    """
    GitHub uses RFC5988-ish Link headers:
      <url1>; rel="next", <url2>; rel="last"
    """
    links: Dict[str, str] = {}
    for part in link_value.split(","):
        part = part.strip()
        m = re.match(r'<([^>]+)>\s*;\s*rel="([^"]+)"', part)
        if m:
            links[m.group(2)] = m.group(1)
    return links


def fetch_all_releases(owner: str, repo: str, token: str) -> List[Release]:
    url = f"https://api.github.com/repos/{owner}/{repo}/releases?per_page=100"
    releases: List[Release] = []

    while url:
        page, headers = gh_api_get(url, token)
        for r in page:
            releases.append(
                Release(
                    tag_name=r.get("tag_name", "").strip(),
                    name=(r.get("name") or "").strip(),
                    body=(r.get("body") or "").rstrip(),
                    html_url=r.get("html_url", "").strip(),
                    published_at=r.get("published_at"),
                    draft=bool(r.get("draft")),
                    prerelease=bool(r.get("prerelease")),
                )
            )

        link = headers.get("link", "")
        next_url = ""
        if link:
            links = parse_link_header(link)
            next_url = links.get("next", "")
        url = next_url

    return releases


def sanitize_version(tag: str) -> str:
    """
    Turn tags like:
      v1.4.2 -> 1.4.2
      1.4.2  -> 1.4.2
    """
    tag = tag.strip()
    tag = re.sub(r"^[vV]", "", tag)
    return tag


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def format_date(iso: Optional[str]) -> str:
    if not iso:
        return ""
    # GitHub uses ISO8601, e.g. 2025-01-18T12:34:56Z
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        return dt.date().isoformat()
    except Exception:
        return iso


def render_release_md(rel: Release) -> str:
    version = sanitize_version(rel.tag_name) or rel.tag_name
    title = rel.name if rel.name else f"Release {version}"
    date_str = format_date(rel.published_at)

    header_lines = [f"# {title}"]
    meta_lines: List[str] = []
    if date_str:
        meta_lines.append(f"**Published:** {date_str}")
    meta_lines.append(f"**Upstream release:** {rel.html_url}")

    body = rel.body.strip()
    if not body:
        body = "_No release notes provided._"

    return "\n\n".join(
        [
            "\n".join(header_lines),
            "\n".join(meta_lines),
            body,
            "",
        ]
    )


def main() -> int:
    token = os.environ.get("GH_TOKEN", "").strip()
    owner = os.environ.get("CORE_OWNER", "ManiVaultStudio").strip()
    repo = os.environ.get("CORE_REPO", "core").strip()
    output_dir = os.environ.get("OUTPUT_DIR", "docs/release_notes/generated").strip()
    prefix = os.environ.get("FILE_PREFIX", "releasenot_").strip()
    include_prereleases = os.environ.get("INCLUDE_PRERELEASES", "false").lower() == "true"

    if not token:
        print("ERROR: GH_TOKEN is not set.", file=sys.stderr)
        return 2

    ensure_dir(output_dir)

    releases = fetch_all_releases(owner, repo, token)

    # Filter: skip drafts; optionally skip prereleases
    filtered: List[Release] = []
    for r in releases:
        if r.draft:
            continue
        if (not include_prereleases) and r.prerelease:
            continue
        if not r.tag_name:
            continue
        filtered.append(r)

    # Write files
    for r in filtered:
        version = sanitize_version(r.tag_name)
        filename = f"{prefix}{version}.md"
        path = os.path.join(output_dir, filename)
        content = render_release_md(r)

        # Write only if changed (keeps commits clean)
        old = ""
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                old = f.read()
        if old != content:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

    # Optional: remove files that no longer correspond to a release tag
    existing = {
        fn for fn in os.listdir(output_dir)
        if fn.startswith(prefix) and fn.endswith(".md")
    }
    desired = {f"{prefix}{sanitize_version(r.tag_name)}.md" for r in filtered}
    to_remove = sorted(existing - desired)

    for fn in to_remove:
        os.remove(os.path.join(output_dir, fn))

    print(f"Wrote {len(desired)} release note files to {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
