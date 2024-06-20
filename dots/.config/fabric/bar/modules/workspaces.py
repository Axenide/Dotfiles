from __init__ import *

class WorkspacesBox(Box):
    def __init__(self):
        super().__init__(
            orientation="v"
        )

        self.workspaces = Workspaces(
            name="workspaces",
            orientation="v",
            spacing=8,
            invert_scroll = True,
            empty_scroll = True,
            buttons_list=[
                WorkspaceButton(label=FormattedString("")),
                WorkspaceButton(label=FormattedString("")),
                WorkspaceButton(label=FormattedString("")),
                WorkspaceButton(label=FormattedString("")),
                WorkspaceButton(label=FormattedString("")),
                WorkspaceButton(label=FormattedString("")),
                WorkspaceButton(label=FormattedString("")),
                WorkspaceButton(label=FormattedString("")),
                WorkspaceButton(label=FormattedString("")),
                WorkspaceButton(label=FormattedString("")),
            ],
        )

        self.add(self.workspaces)
