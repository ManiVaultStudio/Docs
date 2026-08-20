# Choosing the right scope

Choose the owner and lifetime of a value before choosing its storage API.

| Example | Owner and lifetime | Mechanism |
| --- | --- | --- |
| Point size in one scatterplot | Plugin instance; saved with its project | Plugin action serialization |
| Initial point size for newly created scatterplots | Plugin kind; application preference | Plugin global settings action, read once during instance initialization |
| Rendering policy that every open instance must obey | Plugin kind; application preference | Plugin global settings action, read and observed by every instance |
| Internal preference with no settings UI | Plugin kind; application preference | `Plugin::getSetting()` and `setSetting()` |
| Derived display state or an in-progress operation | Runtime only | Recompute it; do not persist it as a setting |

For the broader action-persistence comparison, see {doc}`Choosing a settings scope <../actions/settings_scopes>`.

## Global default or live policy

A global setting can have either of two useful semantics. Decide which one applies and document it.

**Default for new instances**
: Read the global value when constructing or initializing an instance. Copy it into an instance-owned action, then let the instance diverge. Serialize that local action with the project. Later changes to the global default affect only new instances.

**Live plugin-wide policy**
: Read the current value and connect to the global action's change signal. Every active instance responds when the preference changes. Do not serialize a competing per-instance copy.

Do not combine these semantics accidentally. If a project restores an instance value and a global signal later overwrites it, users cannot tell which scope is authoritative.

## When not to use global settings

Avoid a global setting when the value:

- describes a dataset, view, selection, layout, or project;
- must travel with a project to another installation;
- differs naturally between two instances open at the same time;
- contains a secret, credential, or large payload;
- is merely a cache that can be recreated;
- controls one operation rather than a persistent preference.

Global settings should be few, stable, and understandable outside the context of any one project.
