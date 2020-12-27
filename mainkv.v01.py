##File ini dikoneksikan dengan file login.py
##File ini merupakan file yang digunakan untuk mendesain halaman tampilan


MainBuilder = '''
ScreenManager:
    WelcomeScreen:
    LoginScreen:
    RegisterScreen:
    ChooseScreen:
    DosenHomeScreen:
    MahasiswaHomeScreen:
    QuestMaker:
    PasswordResetScreen:

<WelcomeScreen>:
    name: 'welcomescreen'
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
            text: "Make your own question here, and get the answers from your participants"
            pos_hint: {"center_x": .5, "center_y": .7}
            size_hint_x: .7
            font_style: "Body1"
            halign: "left"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 110
   
        MDRaisedButton:
            id: log_in_button
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint_x: .7
            text: "Sign In"
            size_hint: .7, None
            on_release:
                root.parent.current = "loginscreen"
                root.manager.transition.direction = 'left'

        MDRaisedButton:
            id: create_account_button
            pos_hint: {'center_x': .5, 'center_y': .4}
            size_hint_x: .7
            text: "Create Account"
            size_hint: .7, None
            on_release:
                root.manager.transition.direction = 'left'
                root.parent.current = "register"

    MDFloatLayout:
        MDLabel:
            text: "Copyright (c) RD5 - RPL 2020"
            pos_hint: {"center_x": .5, "center_y": .1}
            size_hint_x: .7
            font_style: "Caption"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 155
    
    
    

<LoginScreen>:
    name: 'loginscreen'
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
            text: "Login"
            pos_hint: {"center_y": .70}
            font_style: "H5"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
        
        MDTextField:
            id: email
            hint_text: "Enter Your Email"
            text_solor: app.theme_cls.primary_color
            pos_hint: {"center_x": .5, "center_y": .6}
            size_hint_x: .7
            icon_right: 'email'
            icon_right_color: app.theme_cls.primary_color
            required: True
            helper_text:'Required' 
            helper_text_mode:  'on_error'
            write_tab: False        

        MDTextField:
            id: password
            hint_text: "Password"
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint_x: .7
            password: True
            required: True
            helper_text:'Required'
            helper_text_mode:  'on_error'
            icon_right: 'lock'
            icon_right_color: app.theme_cls.primary_color
            write_tab: False 

        MDRaisedButton:
            text: "Log In"
            pos_hint: {'center_x': .5, 'center_y': .35}
            size_hint_x: .4
            size_hint: None, None
            on_release: 
                root.manager.transition.direction = 'left'
                root.manager.current = 'choose'

        MDTextButton:
            text: "Don't have an account? Create one"
            pos_hint: {"center_x": .5, "center_y": .25}
            size_hint_x: .4
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 60
            on_release: 
                root.manager.current = 'register'
                root.manager.transition.direction = 'left'
        
        MDTextButton:
            text: "Forgotten password?"
            pos_hint: {"center_x": .5, "center_y": .20}
            size_hint_x: .4
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 110
            on_release: 
                root.manager.current = 'reset_password'
                root.manager.transition.direction = 'left'
        
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
        
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": .05, "center_y": .93}
            on_release: 
                root.manager.current = 'welcomescreen'
                root.manager.transition.direction = 'right'


<RegisterScreen>:
    name: 'register'
    MDFloatLayout   
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
            id: email
            hint_text: "Enter Your Email"
            pos_hint: {"center_x": .5, "center_y": .52}
            size_hint_x: .7
            icon_right: 'email'
            icon_right_color: app.theme_cls.primary_color
            required: True
            helper_text:'Required'
            helper_text_mode:  'on_error'
            write_tab: False 

        MDTextField:
            id: password
            hint_text: "Password"
            pos_hint: {"center_x": .5, "center_y": .44}
            size_hint_x: .7
            icon_right: 'lock'
            icon_right_color: app.theme_cls.primary_color
            password: True
            required: True
            helper_text:'Required'
            helper_text_mode:  'on_error'
            write_tab: False 

        MDRaisedButton:
            text: "Create"
            pos_hint: {'center_x': .5, 'center_y': .28}
            size_hint_x: .4
            size_hint: None, None
            on_release: 
                root.manager.transition.direction = 'right'
                root.manager.current = 'loginscreen'

        
        MDTextButton:
            text: "Have an accout? Log in"
            pos_hint: {"center_x": .5, "center_y": .20}
            size_hint_x: .4
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            on_release: 
                root.manager.current = 'loginscreen'
                root.manager.transition.direction = 'right'
        
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": .05, "center_y": .93}
            on_release: 
                root.manager.current = 'welcomescreen'
                root.manager.transition.direction = 'right'


<ChooseScreen>:
    name: 'choose'
    MDFloatLayout:
        MDLabel:
            text: "Welcome to Realtime Query Apps"
            pos_hint: {"center_x": .5, "center_y": .85}
            size_hint_x: .7
            font_style: "H4"
            halign: "left"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1

        MDLabel:
            text: "Choose Account"
            pos_hint: {"center_y": .70}
            font_style: "H5"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1

        MDRaisedButton:
            text: "DOSEN"
            pos_hint: {'center_x': .5, 'center_y': .6}
            size_hint_x: .6
            size_hint: None, None
            on_release: 
                root.manager.transition.direction = 'left'
                root.manager.current = 'home_dosen'
            

        MDRaisedButton:
            text: "MAHASISWA"
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint_x: .6
            size_hint: None, None
            on_release: 
                root.manager.transition.direction = 'left'
                root.manager.current = 'home_mahasiswa'


        MDTextButton:
            text: "Logout"
            pos_hint: {"center_x": .5, "center_y": .25}
            size_hint_x: .4
            on_release: 
                root.manager.current = 'loginscreen'
                root.manager.transition.direction = 'right'

<DosenHomeScreen>:
    name: 'home_dosen'
    
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
            on_release:
                root.manager.current = 'quest_maker'
                root.manager.transition.direction = 'left'
                

        NavigationLayout:
            ScreenManager:
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'Realtime Query'
                            elevation: 4
                            left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                            elevation: 10
                            set_state:
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
                        text: 'Quest'
                        custom_color: 0, 0, 0, 115
                    MDTextButton:
                        text: 'Logout'
                        custom_color: 0, 0, 0, 115
                        on_release: 
                            root.manager.current = 'loginscreen'
                            root.manager.transition.direction = 'right'
                        
                    ScrollView:

<MahasiswaHomeScreen>
    name: 'home_mahasiswa'
    MDFloatLayout:
        MDLabel:
            text: "You must answer the question"
            pos_hint: {"center_x": .5, "center_y": .60}
            size_hint_x: .7
            font_style: "H5"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1

        MDLabel:
            text: "Tap on the button to check the quest you need to do"
            pos_hint: {"center_y": .5}
            font_style: "Body1"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            password: True

        MDRaisedButton:
            id: check_quest
            pos_hint: {'center_x': .5, 'center_y': .4}
            text: "CHECK QUEST"
            size_hint: None, None

        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": .05, "center_y": .93}
            on_release: 
                root.manager.current = 'choose'
                root.manager.transition.direction = 'right'
                        

<QuestMaker>    
    name: 'quest_maker'
    MDFloatLayout:
        MDTextField:
            id: make_quest
            hint_text: "Make your question here"
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
            on_release: 
                root.manager.current = 'home_dosen'
                root.manager.transition.direction = 'right' 

<PasswordResetScreen>
    name: 'reset_password'
    MDFloatLayout:

    MDLabel:
        text: "Reset your password"
        pos_hint: {"center_y": .60}
        font_style: "H5"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
    
    MDTextField:
        id: email
        hint_text: "Enter Your Email"
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint_x: .7
        write_tab: False 


    MDRaisedButton:
        text: "SEND"
        pos_hint: {"center_x": .5, "center_y": .4}
        size_hint_x: .4
        size_hint: None, None
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1

    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_x": .05, "center_y": .93}
        on_release:
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'right'
'''     
