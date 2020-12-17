from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
Window.size = (450, 650)

LoginPage = '''



MDFloatLayout:
    MDLabel:
        text: "Welcome to Realtime Query Apps"
        pos_hint: {"center_x": .5, "center_y": .90}
        size_hint_x: .7
        font_style: "H4"
        halign: "left"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1

    MDLabel:
        text: "Login as Dosen"
        pos_hint: {"center_y": .70}
        font_style: "H5"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
    
    MDTextField:
        id: email
        hint_text: "Enter Your Email"
        pos_hint: {"center_x": .5, "center_y": .6}
        size_hint_x: .7

    MDTextField:
        id: password
        hint_text: "Password"
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint_x: .7
        password: True

    MDRaisedButton:
        text: "Log In"
        pos_hint: {"center_x": .5, "center_y": .35}
        size_hint_x: .4
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1


    MDTextButton:
        text: "Don't have an account? Create one"
        pos_hint: {"center_x": .5, "center_y": .25}
        size_hint_x: .4
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
    
    MDTextButton:
        text: "Forgotten password?"
        pos_hint: {"center_x": .5, "center_y": .20}
        size_hint_x: .4
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
    
    FloatLayout:
        MDCheckbox:
            size_hint: None, None
            size: "48dp", "48dp"
            pos_hint: {"center_x": .17, "center_y": .43}

        MDLabel:
            text: "Remember My Password"
            pos_hint: {"center_x": .4, "center_y": .43}
            font_style: "Body2"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 155

      
'''

class RQApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Cyan"
        login_page = Builder.load_string(LoginPage)
        return login_page
    


if __name__ == "__main__":
    RQApp().run()