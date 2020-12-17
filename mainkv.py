##File ini dikoneksikan dengan file login.py
##File ini merupakan file yang digunakan untuk mendesain halaman tampilan


LoginPage = '''
ScreenManager:
    LoginScreen:
    RegisterScreen:
    ChooseScreen:
    ReqScreen:

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

        MDRaisedButton:
            text: "Log In"
            pos_hint: {"center_x": .5, "center_y": .35}
            size_hint_x: .4
            on_press: 
                
                root.manager.transition.direction = 'left'

                root.manager.current = 'choose'



        MDTextButton:
            text: "Don't have an account? Create one"
            pos_hint: {"center_x": .5, "center_y": .25}
            size_hint_x: .4
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 60
            on_press: 
                root.manager.current = 'register'
                root.manager.transition.direction = 'left'
        
        MDTextButton:
            text: "Forgotten password?"
            pos_hint: {"center_x": .5, "center_y": .20}
            size_hint_x: .4
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 110
        
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
            id: username
            hint_text: "Enter Your Name"
            pos_hint: {"center_x": .5, "center_y": .60}
            size_hint_x: .7
            icon_right: 'account'
            icon_right_color: app.theme_cls.primary_color
            required: True
            helper_text:'Required'
            helper_text_mode:  'on_error'

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
        
        MDTextField:
            id: password
            hint_text: "Confirm Password"
            pos_hint: {"center_x": .5, "center_y": .36}
            size_hint_x: .7
            icon_right: 'lock'
            icon_right_color: app.theme_cls.primary_color
            password: True
            required: True
            helper_text:'Required'
            helper_text_mode:  'on_error'

        MDRaisedButton:
            text: "Create"
            pos_hint: {"center_x": .5, "center_y": .28}
            size_hint_x: .4
            on_press: 
                root.manager.current = 'loginscreen'
                root.manager.transition.direction = 'right'

        
        MDTextButton:
            text: "Have an accout? Log in"
            pos_hint: {"center_x": .5, "center_y": .20}
            size_hint_x: .4
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            on_press: 
                root.manager.current = 'loginscreen'
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
            pos_hint: {"center_x": .5, "center_y": .6}
            size_hint_x: .6
            on_press: 
                root.manager.current = 'req'
                root.manager.transition.direction = 'left'
            

        MDRaisedButton:
            text: "MAHASISWA"
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint_x: .6


        MDTextButton:
            text: "Logout"
            pos_hint: {"center_x": .5, "center_y": .25}
            size_hint_x: .4
            on_press: 
                root.manager.current = 'loginscreen'
                root.manager.transition.direction = 'right'

<ReqScreen>:
    name: 'req'
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

    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_x": .05, "center_y": .93}
        on_press:
            root.manager.current = 'choose'
            root.manager.transition.direction = 'right'


'''
