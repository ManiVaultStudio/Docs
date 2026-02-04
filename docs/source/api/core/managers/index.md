# Managers

Managers are central coordination components in ManiVault. They encapsulate ownership, lifecycle management, and access to related subsystems such as actions, data, projects, and application state.

Rather than exposing raw collections or global services, ManiVault uses manager classes to provide a well-defined interface for querying, modifying, and observing system-wide resources. This helps keep responsibilities clearly separated and enables plugins and applications to interact with the platform in a controlled and consistent manner.

Each manager typically focuses on a specific domain and exposes a stable API for that domain. The following sections document the available manager classes and their public interfaces.


```{toctree}
:maxdepth: 1

abstract_manager
abstract_actions_manager
abstract_data_hierarchy_manager
abstract_data_manager
abstract_error_manager
abstract_event_manager
abstract_help_manager
abstract_plugin_manager
abstract_project_manager
abstract_scripting_manager
abstract_settings_manager
abstract_task_manager
abstract_theme_manager
abstract_project_manager