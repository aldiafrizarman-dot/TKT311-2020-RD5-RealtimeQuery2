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
        text: "Register new account"
        pos_hint: {"center_y": .70}
        font_style: "H5"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
 
    MDTextField:
        id: username
        hint_text: "Enter Your Name"
        pos_hint: {"center_x": .5, "center_y": .60}
        size_hint_x: .7

    MDTextField:
        id: email
        hint_text: "Enter Your Email"
        pos_hint: {"center_x": .5, "center_y": .52}
        size_hint_x: .7

    MDTextField:
        id: password
        hint_text: "Password"
        pos_hint: {"center_x": .5, "center_y": .44}
        size_hint_x: .7
        password: True
    
    MDTextField:
        id: password
        hint_text: "Confirm Password"
        pos_hint: {"center_x": .5, "center_y": .36}
        size_hint_x: .7
        password: True

    MDRaisedButton:
        text: "Create"
        pos_hint: {"center_x": .5, "center_y": .28}
        size_hint_x: .4
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
    
    MDTextButton:
        text: "Have an accout? Log in"
        pos_hint: {"center_x": .5, "center_y": .20}
        size_hint_x: .4
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1

      
'''

class RQApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Cyan"
        login_page = Builder.load_string(LoginPage)
        return login_page
    
if __name__ == "__main__":
    RQApp().run()