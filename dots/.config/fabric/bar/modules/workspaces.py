from __init__ import *

class WorkspacesBox(Box):
    def __init__(self):
        super().__init__(orientation="v")

        buttons_list = [WorkspaceButton(label=FormattedString("")) for _ in range(10)]

        self.workspaces = Workspaces(
            name="workspaces",
            orientation="v",
            spacing=8,
            invert_scroll=True,
            empty_scroll=True,
            buttons_list=buttons_list,
        )

        self.add(self.workspaces)
