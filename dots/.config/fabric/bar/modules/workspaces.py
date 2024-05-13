from __init__ import *

class WorkspacesBox(Box):
    def __init__(self):
        super().__init__(
            orientation="v"
        )

        self.workspaces = Workspaces(
            spacing=8,
            orientation="v",
            name="workspaces",
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
