import datetime

from anvil.tables import app_tables
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
import sqlite3
import webbrowser
from kivy.core.window import Window
from event_creation_form import (EventPlanning, GuestInvitation, FoodItems)
from wallet import (EventWallet, WalletBasicDetails, ActivateWallet, TopUpWallet)
import bcrypt
import anvil.server

anvil.server.connect("server_ZQNS2ROMN5KSV6VF4I3J7TKE-W5EMMXR3HB5MX5EH")

kv = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True
<MainScreen>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1  
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(20)

        Image:
            source: "SIDELOGO.jpg"
            size_hint: None, None
            size: "90dp", "80dp"


        Image:
            source:"LOGO.jpg"
            pos_hint: {'center_x': 0.5, 'center_y': 0.85}
            size_hint: None, None
            allow_stretch: True
            size: "350dp", "120dp"

        MDLabel:
            text: "Hello!"
            halign: "center"
            bold: True
        MDLabel:
            text: "Welcome to GEP! We’re glad you have decided to join us."
            halign: "center"
            size_hint_y: None
            height: dp(10)

        MDGridLayout:
            cols: 2
            spacing: 20
            padding: "0dp", "40dp", "0dp", "0dp"

            MDFillRoundFlatIconButton:
                text: "Login"
                on_release: app.root.current = "login"
                on_release: app.root.get_screen("main").change_text()
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                md_bg_color: 2/255, 61/255, 224/255, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

            MDFillRoundFlatIconButton:
                text: "Signup"
                on_release: app.root.current = "signup"
                on_release: app.root.get_screen("main").change_text1()
                pos_hint: {'right': 1, 'y': 0.5}
                md_bg_color: 2/255, 61/255, 224/255, 1
                font_name: "Roboto-Bold"
                size_hint: 1, None
                text_color: 1, 1, 1, 1
                height: "50dp"
                font_name: "Roboto-Bold"
        MDLabel:
            text:''

        BoxLayout:
            orientation: 'vertical'
            padding: dp(20)
            spacing: dp(20)

            MDLabel:
                text: 'Follow On Our Social Media'
                halign: "center"

            MDGridLayout:
                cols: 3
                spacing: dp(20)
                size_hint: None, 1
                size: self.minimum_size  # Ensure the grid layout takes its minimum size
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}  # Center the grid layout


                MDFloatingActionButton:
                    icon: 'facebook'
                    on_press: app.open_link("https://www.facebook.com")
                    md_bg_color: 2/255, 61/255, 224/255, 1
                MDFloatingActionButton:
                    icon: 'google'
                    on_press: app.open_link("https://www.google.com")
                    md_bg_color: 252/255, 3/255, 65/255, 1
                MDFloatingActionButton:
                    icon: 'linkedin'
                    on_press: app.open_link("https://www.linkedin.com/company/gtplind/")
                    md_bg_color: 2/255, 2/255, 187/255, 1

        MDLabel:
            text:''

<SignupScreen>:
    canvas.before:
        Color:
            rgba:  1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(5)
        BoxLayout:
            orientation: "vertical"

            MDGridLayout:
                cols: 1
                size_hint_y: None
                height: dp(35)
                BoxLayout:
                    orientation: "vertical"
                    spacing: dp(30)
                    padding: dp(5)
                    MDLabel:
                        text: 'Create Account'
                        font_size:dp(30)
                        halign: 'left'
                        bold: True
                    MDLabel:
                        text: ' Please fill the input below here'
                        halign: 'left'
                BoxLayout:
                    orientation: "vertical"
                    Image:
                        source: "SIDELOGO.jpg"
                        pos_hint: {'center_x': 0.9, 'center_y': 0.1}
                        size_hint: None, None
                        size: "90dp", "80dp"

        MDTextField:
            id: name
            hint_text: 'Enter full name'
            multiline: False
            helper_text: 'Enter a valid name'
            helper_text_mode: 'on_focus'
            icon_left: 'account'
            font_name: "Roboto-Bold"
            pos_hint: {'center_y': 0.1}

        MDTextField:
            id: mobile
            hint_text: 'Enter mobile number'
            multiline: False
            helper_text: 'Enter a valid number'
            helper_text_mode: 'on_focus'
            icon_left: 'cellphone'
            font_name: "Roboto-Bold"
            input_type: 'number'  

        MDTextField:
            id: email
            hint_text: 'Enter your email'
            multiline: False
            helper_text: 'Enter a valid email'
            helper_text_mode: 'on_focus'
            icon_left: 'email'
            font_name: "Roboto-Bold"

        MDFloatLayout:
            MDTextField:
                id: password
                hint_text: "Password"
                password: True
                helper_text: "Enter your password"
                helper_text_mode: "on_focus"
                icon_left: "lock"
                pos_hint: {"center_x": 0.5, "top": 1}   

            MDIconButton:
                id: icon1
                icon: 'eye'
                pos_hint: {"right": 1, "top": 1}
                on_release: root.password_change()

        MDFloatLayout:
            MDTextField:
                id: password2
                hint_text: "Re-Enter Password"
                password: True
                helper_text: "Enter your password"
                helper_text_mode: "on_focus"
                icon_left: "lock"
                pos_hint: {"center_x": 0.5, "top": 1}   

            MDIconButton:
                id: icon2
                icon: 'eye'
                pos_hint: {"right": 1, "top": 1}
                on_release: root.password_change2()



        GridLayout:
            cols: 2
            spacing: dp(20)
            padding: dp(20)
            pos_hint: {'center_x': 0.50, 'center_y': 0.5}
            size_hint: 1, None
            height: "50dp"
            MDFillRoundFlatIconButton:
                text: "Back"
                on_release: app.root.current = "main"
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

            MDFillRoundFlatIconButton:
                text: "Signup"
                on_release: app.root.get_screen("signup").login(name.text,mobile.text,email.text, password.text, password2.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"
        MDLabel:
            text:""
        BoxLayout:
            orientation: 'horizontal'
            size_hint: None, None
            width: "190dp"
            height: "35dp"
            pos_hint: {'center_x': 0.5, 'center_y': 0.2}

            MDLabel:
                text: "Already have an account?"
                font_size:dp(14)
                theme_text_color: 'Secondary'
                halign: 'center'
                valign: 'center'

            MDFlatButton:
                text: "Sign in"
                font_size:dp(18)
                theme_text_color: 'Custom'
                text_color: 6/255, 143/255, 236/255, 1
                on_release: app.root.current = 'login'

<MainDashboardLB>

    MDScreen:

        MDNavigationLayout:

            MDScreenManager:

                MDScreen:

                    BoxLayout:
                        orientation: 'vertical'

                        MDTopAppBar:
                            title: ""
                            elevation: 0
                            pos_hint: {"top": 1}
                            md_bg_color: "#ffffff"
                            specific_text_color: "#4a4939"
                            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                            right_action_items: [["wallet",lambda x: root.wallet_function()],["logout", lambda x: app.logout_function()]]
                        ScrollView:
                            MDBoxLayout:
                                orientation: 'vertical'
                                size_hint_y: None
                                spacing: dp(10)
                                padding: dp(25)
                                height: dp(1500) 
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    spacing: dp(10)
                                    BoxLayout:  
                                        orientation: 'vertical'
                                        size_hint_y: None
                                        height: dp(100)
                                        MDLabel:
                                            text: 'Find the trending events'
                                            bold: True
                                            size_hint_y: None
                                            height: dp(10)
                                        MDFloatLayout:
                                            MDTextField:
                                                hint_text: "Search"
                                                pos_hint: {"center_x": 0.5, "top": 1}
                                                on_text: app.on_search(self.text)

                                            MDIconButton:
                                                icon: 'magnify'
                                                pos_hint: {"right": 1, "top": 1} 
                                    BoxLayout:  
                                        orientation: 'vertical'
                                        size_hint_y: None
                                        height: dp(150)
                                        MDGridLayout:
                                            cols: 2
                                            size_hint_y: None
                                            height: dp(35)
                                            MDLabel:
                                                text: "Popular Events"
                                                bold: True
                                                halign: "left"
                                                font_size:dp(14)
                                                text_color: 0, 0, 0, 1 
                                                halign: 'left'

                                            MDFlatButton:
                                                text: "See all"
                                                font_size:dp(12)
                                                theme_text_color: 'Custom'
                                                text_color: 6/255, 143/255, 236/255, 1
                                        MDGridLayout:
                                            cols: 2
                                            spacing: dp(16)

                                            MDCard:
                                                size_hint: 1, None
                                                height: dp(35)
                                                orientation: 'vertical'
                                                size: "280dp", "220dp"
                                                pos_hint: {"center_x": 0.5, "center_y": 0.5}

                                                Image:
                                                    source: "BIRTHDAY.jpg"
                                                    size_hint_y: 0.6  
                                                    allow_stretch: True 

                                                MDBoxLayout:
                                                    orientation: 'vertical'
                                                    padding: dp(16)

                                                    MDLabel:
                                                        text: "Birthday Party"
                                                        theme_text_color: "Secondary"
                                                        halign: "center"
                                                        font_size: "18sp"
                                                        size_hint_y: None
                                                        height: "40dp"

                                                    BoxLayout:
                                                        orientation: 'horizontal'
                                                        size_hint_y: None
                                                        height: dp(30)


                                                        MDIconButton:
                                                            icon: 'map-marker'
                                                            icon_size: dp(15) 
                                                            theme_text_color: 'Custom'
                                                            text_color: 6/255, 143/255, 236/255, 1

                                                        MDLabel:
                                                            text: "Location"
                                                            font_size: dp(15)
                                                            theme_text_color: 'Custom'
                                                            text_color: 6/255, 143/255, 236/255, 1

                                                    MDFillRoundFlatIconButton:
                                                        text: "Interested"
                                                        font_size: dp(13)
                                                        text_color: 98/255, 6/255, 204/255, 1 
                                                        icon: "thumb-up-outline"
                                                        icon_color: 98/255, 6/255, 204/255, 1
                                                        pos_hint: {'center_x': 0.6, 'center_y': 0.4}
                                                        md_bg_color: 1, 1, 1, 1
                                            MDCard:
                                                size_hint: 1, None
                                                height: dp(35)
                                                orientation: 'vertical'
                                                size: "280dp", "220dp"
                                                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                                                Image:
                                                    source: "GETTOGETHER.jpg"
                                                    size_hint_y: 0.6  
                                                    allow_stretch: True 

                                                MDBoxLayout:
                                                    orientation: 'vertical'
                                                    padding: dp(16)

                                                    MDLabel:
                                                        text: "Get Together"
                                                        theme_text_color: "Secondary"
                                                        halign: "center"
                                                        font_size: "18sp"
                                                        size_hint_y: None
                                                        height: "40dp"

                                                    BoxLayout:
                                                        orientation: 'horizontal'
                                                        size_hint_y: None
                                                        height: dp(30)


                                                        MDIconButton:
                                                            icon: 'map-marker'
                                                            icon_size: dp(15) 
                                                            theme_text_color: 'Custom'
                                                            text_color: 6/255, 143/255, 236/255, 1

                                                        MDLabel:
                                                            text: "Location"
                                                            font_size: dp(15)
                                                            theme_text_color: 'Custom'
                                                            text_color: 6/255, 143/255, 236/255, 1

                                                    MDFillRoundFlatIconButton:
                                                        text: "Interested"
                                                        font_size: dp(13)
                                                        text_color: 98/255, 6/255, 204/255, 1 
                                                        icon: "thumb-up-outline"
                                                        icon_color: 98/255, 6/255, 204/255, 1
                                                        pos_hint: {'center_x': 0.6, 'center_y': 0.4}
                                                        md_bg_color: 1, 1, 1, 1

                                    BoxLayout:  
                                        orientation: 'vertical'
                                        spacing: dp(10)

                                        MDGridLayout:
                                            cols: 2
                                            size_hint_y: None
                                            height: dp(35)
                                            MDLabel:
                                                text: "Running Events"
                                                bold: True
                                                halign: "left"
                                                font_size:dp(14)
                                                text_color: 0, 0, 0, 1 
                                                halign: 'left'
                                        MDGridLayout:
                                            cols: 3
                                            size_hint_y: None
                                            height: dp(70)
                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                Image:
                                                    source: "DPARTY.jpg"
                                                    size_hint_y: 0.6  
                                                    allow_stretch: True
                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                spacing: dp(5)
                                                MDLabel:
                                                    text: "  Drinking party"
                                                    font_size: dp(12)
                                                    bold: True
                                                MDLabel:
                                                    text: "  location"
                                                    font_size: dp(12)
                                                    text_color: 6/255, 143/255, 236/255, 1

                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                spacing: dp(5)
                                                MDRaisedButton:
                                                    text: "Live"
                                                    text_color: 230/255, 0, 0, 1
                                                    md_bg_color: 1, 230/255,230/255, 1
                                                    pos_hint: {'right': 1, 'y': 0.5}
                                                    size_hint: None, None
                                                    size: "70dp", "20dp" 
                                                    font_name: "Roboto-Bold"


                                        MDGridLayout:
                                            cols: 2
                                            size_hint_y: None
                                            height: dp(35)
                                            spacing: dp(5)

                                            MDLabel:
                                                text: "See More"
                                                text_color: 0, 0, 0, 1
                                                font_size: dp(13)
                                                halign: "right"
                                                theme_text_color: 'Custom'          
                                            MDIconButton:
                                                icon: 'arrow-right-thick'
                                                text_color: 0, 0, 0, 1
                                                icon_size: dp(13) 
                                                halign: "left"
                                                theme_text_color: 'Custom'
                                    BoxLayout:  
                                        orientation: 'vertical'
                                        MDGridLayout:
                                            cols: 1
                                            size_hint_y: None
                                            height: dp(35)
                                            MDLabel:
                                                text: "Let's get started"
                                                bold: True
                                                halign: "center"
                                        MDGridLayout:
                                            cols: 2
                                            spacing:dp(15)
                                            size_hint_y: None
                                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                            height: self.minimum_height
                                            width: self.minimum_width
                                            size_hint_x: None
                                            MDFlatButton:
                                                size_hint: None, None
                                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                                on_release: app.root.current = 'EventPlanning'
                                                md_bg_color: 1/255, 6/255, 48/255, 1 
                                                size_hint_y: None
                                                height: dp(60)
                                                size_hint_x: None
                                                width: dp(110)

                                                BoxLayout:
                                                    orientation: 'horizontal'
                                                    spacing:dp(10)
                                                    MDLabel:
                                                        text: "Event Creation"
                                                        font_size:dp(14)
                                                        bold:True
                                                        theme_text_color: 'Custom'
                                                        halign: "center"
                                                        text_color:1,1,1,1
                                                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                            MDFlatButton:
                                                size_hint: None, None
                                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                                md_bg_color: 1/255, 6/255, 48/255, 1 
                                                size_hint_y: None
                                                height: dp(60)
                                                size_hint_x: None
                                                width: dp(110)

                                                BoxLayout:
                                                    orientation: 'horizontal'
                                                    spacing:dp(10)
                                                    MDLabel:
                                                        text: "View Events"
                                                        font_size:dp(14)
                                                        bold:True
                                                        theme_text_color: 'Custom'
                                                        halign: "center"
                                                        text_color:1,1,1,1
                                                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                            MDFlatButton:
                                                size_hint: None, None
                                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                                md_bg_color: 1/255, 6/255, 48/255, 1 
                                                size_hint_y: None
                                                height: dp(60)
                                                size_hint_x: None
                                                width: dp(110)
                                                BoxLayout:
                                                    orientation: 'horizontal'
                                                    spacing:dp(10)
                                                    MDLabel:
                                                        text: "Budget for Events"
                                                        font_size:dp(14)
                                                        bold:True
                                                        theme_text_color: 'Custom'
                                                        halign: "center"
                                                        text_color:1,1,1,1
                                                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                                            MDFlatButton:
                                                size_hint: None, None
                                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                                md_bg_color: 1/255, 6/255, 48/255, 1 
                                                size_hint_y: None
                                                height: dp(60)
                                                size_hint_x: None
                                                width: dp(110)

                                                BoxLayout:
                                                    orientation: 'horizontal'
                                                    spacing:dp(10)
                                                    MDLabel:
                                                        text: "Vendor Management"
                                                        font_size:dp(14)
                                                        bold:True
                                                        theme_text_color: 'Custom'
                                                        halign: "center"
                                                        text_color:1,1,1,1
                                                        pos_hint: {'center_x': 0.5, 'center_y': 0.5} 
                                            MDFlatButton:
                                                size_hint: None, None
                                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                                md_bg_color: 1/255, 6/255, 48/255, 1  
                                                size_hint_y: None
                                                height: dp(60)
                                                size_hint_x: None
                                                width: dp(110)

                                                BoxLayout:
                                                    orientation: 'horizontal'
                                                    spacing:dp(10)
                                                    MDLabel:
                                                        text: "Guest List Management"
                                                        font_size:dp(14)
                                                        bold:True
                                                        theme_text_color: 'Custom'
                                                        halign: "center"
                                                        text_color:1,1,1,1
                                                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                            MDFlatButton:
                                                size_hint: None, None
                                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                                md_bg_color: 1/255, 6/255, 48/255, 1 
                                                size_hint_y: None
                                                height: dp(60)
                                                size_hint_x: None
                                                width: dp(110)

                                                BoxLayout:
                                                    orientation: 'horizontal'
                                                    spacing:dp(10)
                                                    MDLabel:
                                                        text: "Task check list"
                                                        font_size:dp(14)
                                                        bold:True
                                                        theme_text_color: 'Custom'
                                                        halign: "center"
                                                        text_color:1,1,1,1
                                                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                    MDLabel:
                                        text: ''
                                    MDLabel:
                                        text: ''


            MDNavigationDrawer:
                id: nav_drawer
                radius: (0, 16, 16, 0)

                MDNavigationDrawerMenu:

                    MDNavigationDrawerHeader:
                        title: "Welcome"
                        title_color: "#4a4939"
                        text: "sai mamidala"
                        spacing: "4dp"
                        padding: "12dp", 0, 0, "56dp"

                    MDNavigationDrawerLabel:
                        text: "Explore Menu"

                    DrawerClickableItem:
                        icon: "account"
                        text_right_color: "#4a4939"
                        text: "Profile"

                    DrawerClickableItem:
                        icon: "message-processing"
                        text: "Communication"
                    DrawerClickableItem:
                        icon: "alert"
                        text: "Emergency"
                    DrawerClickableItem:
                        icon: "book-edit"
                        text: "Feedback"
                    DrawerClickableItem:
                        icon: "help-circle"
                        text: "Help"
                    DrawerClickableItem:
                        icon: "cog"
                        text: "Settings"

                    MDNavigationDrawerDivider:

<LoginScreen>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1  
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        spacing: dp(25)
        padding: dp(20)

        Image:
            source: "SIDELOGO.jpg"
            size_hint: None, None
            size: "90dp", "80dp"


        MDLabel:
            text: 'Welcome Back!'
            halign: 'left'
            font_name:"Roboto-Bold"
            pos_hint: {'center_x': 0.5, 'center_y': 0.81}
        MDLabel:
            text: ' Please sign in to continue'
            halign: 'left'
        MDTextField:
            id: email      
            hint_text: "Email/Mobile Number"
            helper_text_mode: "on_focus"
            icon_left: "email"
            font_name: "Roboto-Bold"
            pos_hint: {'center_x': 0.5, 'center_y': 0.57}
        MDFloatLayout:
            MDTextField:
                id: password
                hint_text: "Password"
                password: True
                helper_text: "Enter your password"
                helper_text_mode: "on_focus"
                icon_left: "lock"
                pos_hint: {"center_x": 0.5, "top": 1}   

            MDIconButton:
                id: icon1
                icon: 'eye'
                pos_hint: {"right": 1, "top": 1}
                on_release: root.password_change()
        MDLabel:
            text:""
        MDLabel:
            text:""
        MDFlatButton:
            text: "Forget password?"
            halign: "right"
            font_size:dp(14)
            theme_text_color: 'Custom'
            text_color: 6/255, 143/255, 236/255, 1         
        GridLayout:
            cols: 2
            spacing:dp(20)
            padding:dp(20)
            pos_hint: {'center_x': 0.5, 'center_y': 0.32}
            size_hint: 1, None
            height: "50dp"
            MDFillRoundFlatIconButton:
                text: "Back"
                on_release: app.root.current = "main"
                on_release: app.root.get_screen("login").change_text3()
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

            MDFillRoundFlatIconButton:
                text: "Login"
                on_release: app.root.get_screen("login").on_login(email.text, password.text)
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"
        MDLabel:
            text:""
        MDLabel:
            text:""
        BoxLayout:
            orientation: 'vertical'
            padding: dp(20)
            spacing: dp(20)
            MDLabel:
                text: '-----------0r-----------'
                halign: "center"

            MDLabel:
                text: 'Sign Up'
                halign: "center"

            MDGridLayout:
                cols: 2
                spacing: dp(20)
                size_hint: None, 1
                size: self.minimum_size  # Ensure the grid layout takes its minimum size
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}  # Center the grid layout


                MDFloatingActionButton:
                    icon: 'facebook'
                    md_bg_color: 2/255, 61/255, 224/255, 1
                MDFloatingActionButton:
                    icon: 'google'
                    md_bg_color: 252/255, 3/255, 65/255, 1
        MDLabel:
            text:""
        MDLabel:
            text: ""
        BoxLayout:
            orientation: 'horizontal'
            size_hint: None, None
            width: "190dp"
            height: "35dp"
            pos_hint: {'center_x': 0.5, 'center_y': 0.2}

            MDLabel:
                text: "Don't have an account?"
                font_size:dp(14)
                theme_text_color: 'Secondary'
                halign: 'center'
                valign: 'center'

            MDFlatButton:
                text: "Sign Up"
                font_size:dp(18)
                theme_text_color: 'Custom'
                text_color: 6/255, 143/255, 236/255, 1
                on_release: app.root.current = 'signup'

'''

Builder.load_string(kv)
conn = sqlite3.connect('kivymd.db')
cursor = conn.cursor()


class MainScreen(Screen):

    def change_text(self):
        # Access the label in another screen and update its text
        pass

    def change_text1(self):
        # Access the label in another screen and update its text
        pass


class SignupScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def password_change(self):
        if self.ids.password.password:
            self.ids.password.password = False
            self.ids.icon1.icon = 'eye-off'
        else:
            self.ids.password.password = True
            self.ids.icon1.icon = 'eye'

    def password_change2(self):
        if self.ids.password2.password:
            self.ids.password2.password = False
            self.ids.icon2.icon = 'eye-off'
        else:
            self.ids.password2.password = True
            self.ids.icon2.icon = 'eye'

    def show_alert_dialog(self, alert_text):
        if not hasattr(self, 'dialog') or not self.dialog:
            self.dialog = MDDialog(
                text=alert_text,
                buttons=[
                    MDFlatButton(
                        text="OK", on_release=self.close_dialog
                    ),
                ],
            )

        self.dialog.text = alert_text
        self.dialog.open()

    # Click Cancel Button
    def close_dialog(self, obj):
        # Close alert box
        self.dialog.dismiss()

    def login(self, name, mobile, email, password, password2):
        conn = sqlite3.connect('kivymd.db')
        cursor = conn.cursor()
        date_time = datetime.datetime.today()
        hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        hash_password = hash_password.decode('utf-8')

        # Create a table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS registration_table (
                            customer_id INTEGER PRIMARY KEY,
                            name TEXT,
                            mobile INT,
                            email TEXT,
                            password TEXT,
                            customer_status TEXT
                            )''')

        cursor.execute('SELECT * FROM registration_table')

        p = cursor.fetchall()

        email_list = []
        password_list = []
        customer_id = []
        for i in p:
            email_list.append(i[3])
            password_list.append(i[4])
            customer_id.append(i[0])

        data = app_tables.signup_table.search()
        anvil_customer_id = []
        anvil_email = []
        for i in data:
            anvil_customer_id.append(i['customer_id'])
            anvil_email.append(i['email'])

        if len(anvil_customer_id) == 0:
            c_id = 1000
        else:
            c_id = anvil_customer_id[-1] + 1

        if len(customer_id) == 0:
            id = 1000
        else:
            id = customer_id[-1] + 1

        if name == '' or mobile == '' or email == '' or password == '' or password2 == '':
            self.show_alert_dialog("You Must Enter All Fields")
            return

        if not (name.isalpha() and len(name) >= 3):
            self.show_alert_dialog("Invalid Name")
            return

        if not (mobile.isdigit() and len(mobile) == 10):
            self.show_alert_dialog("Invalid Mobile Number")
            return

        if not email.endswith("@gmail.com"):
            self.show_alert_dialog("Invalid Email")
            return

        if len(password) < 8:
            self.show_alert_dialog("Password should be at least 8 characters long")
            return

        if password != password2:
            self.show_alert_dialog("Passwords do not match")
            return

        if email in email_list:
            self.show_alert_dialog("Email already exists")
            return
        if email in anvil_email:
            self.show_alert_dialog("Email already exists")
            return

        try:
            sign_date_time = date_time.today()
            cursor.execute(
                "INSERT INTO registration_table (customer_id, name, mobile, email, password) VALUES (?, ?, ?, ?, ?)",
                (id, name, mobile, email, hash_password))
            app_tables.signup_table.add_row(customer_id=c_id, name=name, mobile_number=int(mobile), email=email,
                                            password=hash_password,
                                            sign_up_date_time=sign_date_time)
            conn.commit()
            self.show_alert_dialog(f'{email} is successfully signed up')
            self.manager.current = "login"

        except sqlite3.Error as err:
            self.show_alert_dialog(f"Error signing up: {err}")

        conn.close()


class LoginScreen(Screen):
    def password_change(self):
        if self.ids.password.password:
            self.ids.password.password = False
            self.ids.icon1.icon = 'eye-off'
        else:
            self.ids.password.password = True
            self.ids.icon1.icon = 'eye'

    def change_text3(self):
        # Access the label in another screen and update its text
        login_status_label1 = MDApp.get_running_app().root.get_screen('signup')
        login_status_label1.ids.name.text = ""
        login_status_label1.ids.mobile.text = ""
        login_status_label1.ids.email.text = ""
        login_status_label1.ids.password.text = ""
        login_status_label1.ids.password2.text = ""

    def show_alert_dialog(self, alert_text):
        if not hasattr(self, 'dialog') or not self.dialog:
            self.dialog = MDDialog(
                text=alert_text,
                buttons=[
                    MDFlatButton(
                        text="OK", on_release=self.close_dialog
                    ),
                ],
            )
        self.dialog.text = alert_text
        self.dialog.open()

    def close_dialog(self, obj):
        # Close alert box
        self.dialog.dismiss()

    def on_login(self, email, password):
        conn = sqlite3.connect('kivymd.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM registration_table WHERE email = ?', (email,))
        user = cursor.fetchone()
        data = app_tables.signup_table.search()
        anvil_email = []
        anvil_password = []
        for i in data:
            anvil_email.append(i['email'])
            anvil_password.append(i['password'])

        if not user:
            self.show_alert_dialog("User not found")
        else:
            stored_password = user[4]

            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                cursor.execute("UPDATE registration_table SET customer_status = ? WHERE email = ?", ('logged', email))
                conn.commit()
                self.manager.current = "success"
            else:
                self.show_alert_dialog("Invalid credentials")
        if email not in anvil_email and not user:
            self.show_alert_dialog("Please SignUp Email Not Found")
        else:
            if email in anvil_email:
                index = anvil_email.index(email)
                print(bcrypt.checkpw(password.encode('utf-8'), anvil_password[index].encode('utf-8')))
                if email == anvil_email[index] and bcrypt.checkpw(password.encode('utf-8'),
                                                                  anvil_password[index].encode('utf-8')):
                    self.manager.current = "success"
                else:
                    self.show_alert_dialog("Invalid credentials")

        conn.close()


class MainDashboardLB(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.on_pre_enter()

    def change_text3(self):
        # Access the label in another screen and update its text
        login_status_label = MDApp.get_running_app().root.get_screen('login')
        login_status_label.ids.email.text = ""
        login_status_label.ids.password.text = ""
        login_status_label1 = MDApp.get_running_app().root.get_screen('signup')
        login_status_label1.ids.name.text = ""
        login_status_label1.ids.mobile.text = ""
        login_status_label1.ids.email.text = ""
        login_status_label1.ids.password.text = ""
        login_status_label1.ids.password2.text = ""
        self.manager.current = 'main'

    def load_user_data(self):
        pass

        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'MainScreen'

    def switch_screen(self, screen_name):
        print(f"Switching to screen: {screen_name}")

        # Get the screen manager
        sm = self.manager

        sm.transition = SlideTransition(direction='left')
        sm.current = screen_name



    def wallet_function(self):
        # Get the screen manager
        sm = self.manager

        # Access the desired screen by name and change the current screen
        sm.current = 'EventWallet'



class LoginApp(MDApp):
    def build(self):
        sm = ScreenManager()

        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = "DeepPurple"

        # Add screens
        main_screen = MainScreen(name="main")
        login_screen = LoginScreen(name="login")
        signup_screen = SignupScreen(name="signup")
        success_screen = MainDashboardLB(name="success")

        sm.add_widget(main_screen)
        sm.add_widget(login_screen)
        sm.add_widget(signup_screen)
        sm.add_widget(success_screen)
        sm.add_widget(EventPlanning(name='EventPlanning'))
        sm.add_widget(GuestInvitation(name='GuestInvitation'))
        sm.add_widget(FoodItems(name='FoodItems'))
        sm.add_widget(EventWallet(name='EventWallet'))
        sm.add_widget(WalletBasicDetails(name='WalletBasicDetails'))
        sm.add_widget(ActivateWallet(name='ActivateWallet'))
        sm.add_widget(TopUpWallet(name='TopUpWallet'))
        self.success_screen = success_screen

        return sm

    def logout_function(self):
        # Access the stored reference to the success_screen and call its method
        self.success_screen.change_text3()

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_keyboard)
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):

        if key == 27:
            self.go_back()
            return True
        return False

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def on_start(self):
        Window.softinput_mode = "below_target"

    def open_link(self, url):
        webbrowser.open(url)


if __name__ == "__main__":
    LoginApp().run()