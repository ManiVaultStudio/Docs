# Managers

Managers are central coordination components in ManiVault. They encapsulate ownership, lifecycle management, and access to related subsystems such as actions, data, projects, and application state.

Rather than exposing raw collections or global services, ManiVault uses manager classes to provide a well-defined interface for querying, modifying, and observing system-wide resources. This helps keep responsibilities clearly separated and enables plugins and applications to interact with the platform in a controlled and consistent manner.

Each manager typically focuses on a specific domain and exposes a stable API for that domain. The following sections document the available manager classes and their public interfaces.


```{toctree}
:maxdepth: 1

abstract_actions_manager