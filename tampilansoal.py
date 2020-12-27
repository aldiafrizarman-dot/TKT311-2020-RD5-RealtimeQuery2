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
        text: "Berapa jumlah kaki ulat bulu?"
        pos_hint: {"center_x": .5, "center_y": .7}
        size_hint_x: .7
        font_style: "Body1"
        halign: "left"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
    MDTextField:
        mode: 'rectangle'
        hint_text: "Jawab disini"
        text_solor: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .6}
        size_hint_x: .7
        required: True
        helper_text:'Required' 
        helper_text_mode:  'on_error'
        write_tab: False 

    MDRaisedButton:
        text: 'SUBMIT'
        pos_hint: {'center_x': .75, 'center_y': .5}
        size_hint: None, None    

    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_x": .05, "center_y": .93}

            


      
'''

class RQApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Cyan"
        login_page = Builder.load_string(LoginPage)
        return login_page
    


if __name__ == "__main__":
    RQApp().run()

