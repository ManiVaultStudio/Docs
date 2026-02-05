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
                    tag_name=(r.get("tag_name") or "").strip(),
                    name=(r.get("name") or "").strip(),
                    body=(r.get("body") or "").rstrip(),
                    html_url=(r.get("html_url") or "").strip(),
                    published_at=r.get("published_at"),
                    draft=bool(r.get("draft")),
                    prerelease=bool(r.get("prerelease")),
                )
            )

        link = headers.get("link", "")
        url = ""
        if link:
            links = parse_link_header(link)
            url = links.get("next", "")

    return releases


def sanitize_version(tag: str) -> str:
    tag = (tag or "").strip()
    tag = re.sub(r"^[vV]", "", tag)
    return tag


def parse_semverish(ver: str) -> Tuple[int, int, int, str]:
    """
    Parse "1.4.2" -> (1,4,2,"")
    Parse "1.4"   -> (1,4,0,"")
    Parse "1.4.2-rc1" -> (1,4,2,"-rc1")  (suffix kept for tie-breaking)
    Non-matching versions sort low.
    """
    ver = (ver or "").strip()
    m = re.match(r"^(\d+)\.(\d+)(?:\.(\d+))?([\-+].+)?$", ver)
    if not m:
        return (-1, -1, -1, ver)
    major = int(m.group(1))
    minor = int(m.group(2))
    patch = int(m.group(3) or 0)
    suffix = m.group(4) or ""
    return (major, minor, patch, suffix)


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def format_date(iso: Optional[str]) -> str:
    if not iso:
        return ""
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        return dt.date().isoformat()
    except Exception:
        return iso


def render_release_md(rel: Release) -> str:
    version = sanitize_version(rel.tag_name) or rel.tag_name
    title = rel.name if rel.name else f"Release {version}"
    date_str = format_date(rel.published_at)

    meta_lines: List[str] = []
    if date_str:
        meta_lines.append(f"**Published:** {date_str}")
    meta_lines.append(f"**Upstream release:** {rel.html_url}")

    body = rel.body.strip() or "_No release notes provided._"

    return "\n\n".join(
        [
            f"# {title}",
            "\n".join(meta_lines),
            body,
            "",
        ]
    )


def render_index_md(
    releases: List[Release],
    output_dir: str,
    prefix: str,
    title: str = "Release Notes",
) -> str:
    """
    Generates an index.md that links to all generated release note files.
    Links are written relative to the index.md location.
    """
    lines: List[str] = [f"# {title}", ""]
    if not releases:
        lines.append("_No releases found._")
        lines.append("")
        return "\n".join(lines)

    lines.append("")

    lines.append("```{toctree}\n:maxdepth: 2")

    # Each link points into the generated directory
    for r in releases:
        ver = sanitize_version(r.tag_name) or r.tag_name
        fn = f"{prefix}{ver}.md"
        # Index is expected to live at docs/release_notes/index.md
        # and generated files at docs/release_notes/generated/<fn>
        rel_path = f"{fn}"
        label = ver
        date_str = format_date(r.published_at)
        if date_str:
            lines.append(f"- [{label}]({rel_path}) ({date_str})")
        else:
            lines.append(f"- [{label}]({rel_path})")

    lines.append("```")

    return "\n".join(lines)


def main() -> int:
    token = os.environ.get("GH_TOKEN", "").strip()
    owner = os.environ.get("CORE_OWNER", "ManiVaultStudio").strip()
    repo = os.environ.get("CORE_REPO", "core").strip()

    # Generated release notes go here
    output_dir = os.environ.get("OUTPUT_DIR", "docs/source/release_notes").strip()
    prefix = os.environ.get("FILE_PREFIX", "release_note_").strip()

    # Index file (Markdown) that links to all generated notes
    index_path = os.environ.get("INDEX_PATH", "docs/source/release_notes/index.md").strip()
    index_title = os.environ.get("INDEX_TITLE", "Release Notes").strip()

    include_prereleases = os.environ.get("INCLUDE_PRERELEASES", "false").lower() == "true"

    if not token:
        print("ERROR: GH_TOKEN is not set.", file=sys.stderr)
        return 2

    ensure_dir(output_dir)
    ensure_dir(os.path.dirname(index_path) or ".")

    releases = fetch_all_releases(owner, repo, token)

    # Filter: skip drafts; optionally skip prereleases; require a tag; require name starting with "Release"
    filtered: List[Release] = []
    for r in releases:
        if r.draft:
            continue
        if (not include_prereleases) and r.prerelease:
            continue
        if not r.tag_name:
            continue
        if not r.name.startswith("Release"):
            continue
        filtered.append(r)

    # Sort newest-first by version (fallback to published_at for ties)
    def sort_key(r: Release) -> Tuple[Tuple[int, int, int, str], str]:
        ver = sanitize_version(r.tag_name)
        return (parse_semverish(ver), r.published_at or "")

    filtered_sorted = sorted(filtered, key=sort_key, reverse=True)

    # Write per-release files
    desired_files: set[str] = set()
    for r in filtered_sorted:
        ver = sanitize_version(r.tag_name)
        filename = f"{prefix}{ver}.md"
        desired_files.add(filename)

        path = os.path.join(output_dir, filename)
        content = render_release_md(r)

        old = ""
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                old = f.read()

        if old != content:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

    # Remove generated files no longer matching a release
    existing = {
        fn for fn in os.listdir(output_dir)
        if fn.startswith(prefix) and fn.endswith(".md")
    }
    for fn in sorted(existing - desired_files):
        os.remove(os.path.join(output_dir, fn))

    # Write index.md (only if changed)
    index_content = render_index_md(
        releases=filtered_sorted,
        output_dir=output_dir,
        prefix=prefix,
        title=index_title,
    )
    old_index = ""
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            old_index = f.read()

    if old_index != index_content:
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(index_content)

    print(f"Wrote {len(desired_files)} release note files to {output_dir}")
    print(f"Wrote index: {index_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
