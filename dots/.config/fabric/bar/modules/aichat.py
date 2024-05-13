from __init__ import *

class AIbuttons(Box):
    def __init__(self):
        super().__init__(
            name="chat-buttons",
            orientation="h",
            h_expand=True,
            spacing=4,
        )

        self.web = AIweb()

        self.expanded = False

        self.chat_expand = Button(
            name="chat-expand",
            h_expand=False,
            child=Image(
                name="chat-expand-image",
                image_file=get_relative_path("../assets/maximize.svg")
            )
        )

        self.chat_reload = Button(
            name="chat-reload",
            h_expand=False,
            child=Image(
                name="chat-reload-image",
                image_file=get_relative_path("../assets/refresh.svg")
            )
        )

        self.chat_url = Button(
            name="chat-url",
            label="localhost:3141/Alpha",
            h_expand=True,
            v_expand=True,
            v_align="center",
        )

        self.chat_detach = Button(
            name="chat-detach",
            h_expand=False,
            child=Image(
                name="chat-detach-image",
                image_file=get_relative_path("../assets/external.svg")
            )
        )

        self.buttons = [
            self.chat_expand,
            self.chat_reload,
            self.chat_url,
            self.chat_detach
        ]

        for btn in self.buttons:
            bulk_connect(
                btn,
                {
                    "button-press-event": self.on_button_press,
                    "enter-notify-event": self.on_button_hover,
                    "leave-notify-event": self.on_button_unhover,
                },
            )

        self.set_children(self.buttons)

    def on_button_press(self, button: Button, event):
        if button == self.chat_expand:
            self.expanded = not self.expanded
            if self.expanded:
                chat.content.set_style('min-width: 550px;')
                self.chat_expand.get_children()[0].set_from_file(get_relative_path('../assets/minimize.svg'))
            else:
                chat.content.set_style('min-width: 300px;')
                self.chat_expand.get_children()[0].set_from_file(get_relative_path('../assets/maximize.svg'))

        elif button == self.chat_reload:
            self.web.reload()

        elif button == self.chat_detach:
            self.content_box.set_reveal_child(False)
            self.chat_box.set_reveal_child(False)
            return exec_shell_command_async(get_relative_path(f'../scripts/webview.py http://localhost:3141/Alpha'), lambda *args: None)

        elif button == self.chat_url:
            self.content_box.set_reveal_child(False)
            self.chat_box.set_reveal_child(False)
            return exec_shell_command_async('xdg-open http://localhost:3141/Alpha', lambda *args: None)

    def on_button_hover(self, button: Button, event):
        return self.change_cursor("pointer")

    def on_button_unhover(self, button: Button, event):
        return self.change_cursor("default")

class AIweb(WebView):
    def __init__(self):
        super().__init__(
            name="ai-chat",
            h_expand=True,
            v_expand=True,
            url="http://localhost:3141/Alpha",
        )

class AIchat(Box):
    def __init__(self):
        super().__init__(
            name="chat-box",
            spacing=4,
            orientation="v",
            h_expand=True,
            v_expand=True,
        )

        self.buttons = AIbuttons()
        self.web = self.buttons.web

        self.set_children(
            [
                self.buttons,
                self.web,
            ]
        )
