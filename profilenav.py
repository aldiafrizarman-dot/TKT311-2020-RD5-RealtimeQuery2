from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivymd.color_definitions import colors

Window.size = (420, 650)

nav_helper = '''

Screen:  

    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Realtime Query'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    Widget:
        
        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                Image:
                    source: 'imager.JPG'

                MDLabel:
                    text: 'Aldi Afrizarman'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: 'Dosen'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                    
                
                MDTextButton:
                    text: 'Home'
                    custom_color: 0, 0, 0, 115
                MDTextButton:
                    text: 'Quest'
                    custom_color: 0, 0, 0, 115
                MDTextButton:
                    text: 'Logout'
                    custom_color: 0, 0, 0, 115
                    
                ScrollView:
                    
                    
        

'''

class RQApp(MDApp):

    def build(self):
        screen = Builder.load_string(nav_helper)
        return screen

RQApp().run()