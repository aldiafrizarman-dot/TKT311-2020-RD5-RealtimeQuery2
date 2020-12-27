from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivymd.uix.dialog import MDDialog
from kivy.uix.textinput import TextInput
from kivymd.uix.button import MDFlatButton
from kivy.clock import Clock
import requests
from mainkv import MainBuilder


from kivy.core.window import Window
Window.size = (450, 650)

class WelcomeScreen(Screen):
    pass
class LoginScreen(Screen):
    pass
class RegisterScreen(Screen):
    pass
class ChooseScreen(Screen):
    pass
class DosenHomeScreen(Screen):
    pass
class MahasiswaHomeScreen(Screen):
    pass
class QuestMaker(Screen):
    pass
class PasswordResetScreen(Screen):
    pass


Clock.max_iteration = 20

sm = ScreenManager()
sm.add_widget(WelcomeScreen(name = 'welcomescreen'))
sm.add_widget(LoginScreen(name = 'loginscreen'))
sm.add_widget(RegisterScreen(name = 'register'))
sm.add_widget(ChooseScreen(name = 'choose'))
sm.add_widget(DosenHomeScreen(name = 'home_dosen'))
sm.add_widget(MahasiswaHomeScreen(name = 'home_mahasiswa'))
sm.add_widget(QuestMaker(name = 'quest_maker'))
sm.add_widget(PasswordResetScreen(name = 'reset_password'))


class RealtimeQueryApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Cyan"
        login_page = Builder.load_string(MainBuilder)
        return login_page
    

RealtimeQueryApp().run()
