# Internal

The classes listed below are part of the public API and are therefore accessible to application and plugin developers. However, they are primarily intended for internal use by the core system and, in some cases, by first-party plugins.

While nothing technically prevents external code from using these classes, they are not designed as stable, standalone extension points. Their interfaces and behavior may evolve to support internal architectural needs, and they may change without the same level of compatibility guarantees as the officially supported extension APIs.

Developers are advised to treat these classes as implementation details unless they have a specific and well-understood reason to depend on them.

```{toctree}
:maxdepth: 1

action_overlay_widget
actions_widget
flow_layout
hierarchy_widget
icon_label
info_overlay_widget
info_widget
markdown_dialog
multi_select_combobox
overlay_widget
plugin_about_dialog
plugin_shortcuts_dialog
splash_screen_widget
view_plugin_editor_dialog
view_plugin_learning_center_overlay_widget
view_plugin_overlay_widget
you_tube_video_dialog