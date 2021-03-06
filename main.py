from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivymd.theming import ThemeManager

Window.size = (450, 650)

LoginPage = '''



MDFloatLayout:
    MDLabel:
        text: "You don't have any question right now"
        pos_hint: {"center_x": .5, "center_y": .60}
        size_hint_x: .7
        font_style: "H5"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1

    MDLabel:
        text: "You must create a quest, create add button"
        pos_hint: {"center_y": .5}
        font_style: "Body1"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        password: True

    MDFloatingActionButton:
        icon: "plus"
        pos_hint: {"center_x": .8, "center_y": .1}
        md_bg_color: app.theme_cls.primary_color





'''


class RQApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Cyan"
        login_page = Builder.load_string(LoginPage)
        return login_page


if __name__ == "__main__":
    RQApp().run()