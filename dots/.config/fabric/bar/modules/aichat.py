from __init__ import *

ai_url: str = "https://morphic.sh/"

class AIbuttons(Box):
    def __init__(self):
        super().__init__(
            name="chat-buttons",
            orientation="h",
            h_expand=True,
            spacing=4,
        )

        self.web_module = AIweb()

        self.web = Box(h_expand=True, v_expand=True, children=[self.web_module])

        self.corners_top = CenterBox(
            name="corners",
            orientation="h",
            v_expand=True,
            h_expand=True,
        )

        self.corners_bottom = CenterBox(
            name="corners",
            orientation="h",
            # v_expand=True,
            h_expand=True,
        )

        self.corner_top_left = Corner(name="corner-dark", orientation="top-left", size=20)
        self.corner_top_right = Corner(name="corner-dark", orientation="top-right", size=20)
        
        self.corner_bottom_left = Corner(name="corner-dark", orientation="bottom-left", size=20)
        self.corner_bottom_right = Corner(name="corner-dark", orientation="bottom-right", size=20)

        self.corners_top.add_start(self.corner_top_left)
        self.corners_top.add_end(self.corner_top_right)
        self.corners_bottom.add_start(self.corner_bottom_left)
        self.corners_bottom.add_end(self.corner_bottom_right)

        self.corner_box = Box(
            name="corner-box",
            orientation="v",
            h_expand=True,
            v_expand=True,
            h_align="fill",
            v_align="fill",
            children=[
                self.corners_top,
                self.corners_bottom,
            ],
        )

        self.overlay = Overlay(
            name="overlay",
            v_expand=True,
            h_expand=True,
            overlays=[
                self.web,
                self.corner_box,
            ]
        )

        self.overlay.set_overlay_pass_through(self.corner_box, True)

        self.parent = self

        self.chat_reload = Button(
            name="common-button",
            h_expand=False,
            child=Label(label=icons.reload, markup=True),
        )

        self.chat_url = Button(
            name="chat-url",
            label=f"{ai_url}",
            h_expand=True,
            v_expand=True,
            v_align="center",
        )

        self.chat_detach = Button(
            name="common-button",
            h_expand=False,
            child=Label(label=icons.detach, markup=True),
        )

        self.buttons = [
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
        match button:
            case self.chat_reload:
                self.web_module.reload()
            case self.chat_detach:
                self.parent.content_box.set_reveal_child(False)
                return exec_shell_command_async(f"""
                hyprctl dispatch exec {get_relative_path(f'./scripts/webview.py {ai_url}')}
                """, lambda *args: None)
            case self.chat_url:
                self.parent.content_box.set_reveal_child(False)
                return exec_shell_command_async(f'xdg-open {ai_url}', lambda *args: None)

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
            url=f"{ai_url}",
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
                self.buttons.overlay,
            ]
        )
