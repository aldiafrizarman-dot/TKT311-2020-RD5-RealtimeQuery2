from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivymd.uix.dialog import MDDialog
from kivy.uix.textinput import TextInput
from kivymd.uix.button import MDFlatButton
import requests
from mainkv import LoginPage


from kivy.core.window import Window
Window.size = (450, 650)


class LoginScreen(Screen):
    pass
class RegisterScreen(Screen):
    pass
class ChooseScreen(Screen):
    pass
class ReqScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(LoginScreen(name = 'loginscreen'))
sm.add_widget(RegisterScreen(name = 'register'))
sm.add_widget(ChooseScreen(name = 'choose'))
sm.add_widget(ReqScreen(name = 'req'))



class RealtimeQueryApp(MDApp):
    def build(self):
        login_page = Builder.load_string(LoginPage)
        return login_page
    

RealtimeQueryApp().run()
