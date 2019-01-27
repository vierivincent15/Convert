from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.app import App
from authentication import download_data, invalid_user, print_confirmation, success_page
from itemtopts import retrieve_points, delete_pending, upload_points
from userdata import update_credits
from kivy.clock import Clock
import random
from ultrasonic import presence_of_object
from ldrsensor import check_ldr

a = ["1"]
'''variable a is used to store the global variable'''

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layoutMain = GridLayout(rows = 3)
        self.layout1 = GridLayout(cols = 2)
        self.title_label = Label(text = "CONVERT", font_size = 72)
        self.student_id = Label(text = "Student ID:", font_size = 48)
        self.id_input = TextInput(text = "", font_size = 48)
        self.enter_button = Button(text = "ENTER", font_size = 48, on_press = self.change_screen)
        
        self.layout1.add_widget(self.student_id)
        self.layout1.add_widget(self.id_input)
        self.layoutMain.add_widget(self.title_label)
        self.layoutMain.add_widget(self.layout1)
        self.layoutMain.add_widget(self.enter_button)
        self.add_widget(self.layoutMain)
        global text_input
        text_input = self.id_input
    def change_screen(self, value):
        '''screen can change to either FAIL or CONFIRMATION depending on the user input.'''
        user_dict = download_data()
        a.append(str(self.id_input.text))
        if self.id_input.text in user_dict:
            self.manager.transition.direction = "left"
            self.manager.current = "confirmation"
            current_id.text = str(a[len(a)-1])
            confirmation_title.text = print_confirmation(str(a[len(a)-1]))
            
        else:
            self.manager.transition.direction = "down"
            self.manager.current = "fail"
            
            fail_label.text = invalid_user(str(a[len(a)-1]))
        
    
class FailPage(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layoutMain = BoxLayout(orientation = "vertical")

        self.print_invalid = Label(text = '', font_size = 24, valign = "middle", halign = "center")
        self.ok = Button(text = "OK", font_size = 48, on_press = self.change_to_menu)
        
        self.layoutMain.add_widget(self.print_invalid)
        self.layoutMain.add_widget(self.ok)
        self.add_widget(self.layoutMain)
        global fail_label
        fail_label = self.print_invalid
        
    def change_to_menu(self,value):
        self.manager.transition.direction = "up"
        self.manager.current = "menu"

class ConfirmationPage(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layoutMain = GridLayout(rows = 2)
        self.layout1 = GridLayout(cols = 2)
        self.confirm = Label(text = '', font_size = 24, valign = "middle", halign = "center")
        self.yes_button = Button(text = "YES", font_size = 48, on_press = self.change_to_recycle)
        self.no_button = Button(text = "NO", font_size = 48, on_press = self.change_to_menu)
        self.studentid = Label(text = '')
        self.layout1.add_widget(self.yes_button)
        self.layout1.add_widget(self.no_button)
        self.layoutMain.add_widget(self.confirm)
        self.layoutMain.add_widget(self.layout1)
        self.add_widget(self.layoutMain)
        global confirmation_title 
        global current_id
        confirmation_title = self.confirm
        current_id = self.studentid
        
    def change_to_recycle(self,value):
        self.manager.transition.direction = "left"
        self.manager.current = "recycle"
        
        
    def change_to_menu(self,value):
        self.manager.transition.direction = "right"
        self.manager.current = "menu"
        
class RecycledPage(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.mainLayout = GridLayout(rows = 3)
        self.layout1 = GridLayout(cols = 2)
        self.recycling = Label(text = "Recycling...", font_size = 48, halign = "center")
        self.recycled = Label(text = "Points you have\nrecycled", font_size = 24, halign = "center", valign = "middle" )
        self.points_recycled = Label(text = "0", font_size = 24, halign = "center")
        self.confirm_button = Button(text = "confirm", font_size = 24, on_press = self.change_to_load)
        self.layout1.add_widget(self.recycled)
        self.layout1.add_widget(self.points_recycled)
        self.mainLayout.add_widget(self.recycling)
        self.mainLayout.add_widget(self.layout1)
        self.mainLayout.add_widget(self.confirm_button)
        self.add_widget(self.mainLayout)
        self.checking = True
        self.counter = 0
        global checking_
        checking_ = self.checking
        global points
        points = self.points_recycled
        
        Clock.schedule_interval(self.my_callback, .05)
    
    def change_to_load(self,value):
        checking_ = False
        points = float(self.counter)
        upload_points(points)
        self.counter = 0
        self.manager.transition.direction = "left"
        self.manager.current = "load"
        
    
    def my_callback(self,dt):
        if checking_ == True:
            if check_ldr() == "dark":
                self.counter += 1
                self.points_recycled.text = str(self.counter)
        
class LoadingPage(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layoutMain = GridLayout(rows = 2)
        self.text_display = Label(text = "It will take a\nwhile to load!", font_size = 48, halign = "center")
        self.oke = Button(text="OK", font_size = 24, on_press = self.change_to_success)
        self.layoutMain.add_widget(self.text_display)
        self.layoutMain.add_widget(self.oke)
        self.add_widget(self.layoutMain)
    
    def change_to_success(self, value):
        change_credit = retrieve_points()
        success_title.text = success_page(current_id.text,change_credit)
        update_credits(current_id.text, change_credit)
        delete_pending()
        points.text = '0'
        self.manager.transition.direction = "left"
        self.manager.current = "success"
        

class SuccessPage(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layoutMain = BoxLayout(orientation = "vertical")
        
        
        self.print_success = Label(text = '', font_size = 24, halign = "left")
        self.ok = Button(text = "OK", font_size = 48, on_press = self.change_to_menu)
        
        self.layoutMain.add_widget(self.print_success)
        self.layoutMain.add_widget(self.ok)
        self.add_widget(self.layoutMain)
        global success_title
        success_title = self.print_success
        
    def change_to_menu(self,value):
        checking_ = True
        text_input.text = ''
        self.manager.transition.direction = "left"
        self.manager.current = "menu"

        
class ScreenSaver(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.list_quotes = ["Recycling is Fun",
                            "Teach a man to recycle and\nhe will recycle for a day.\n\nGive a man a recycling bin\nand he will recycle his whole life.",
                            "Why recycle glass?\nThe answer is clear",
                            "Yu Lian said,\n'Do not use plastic straw!'",
                            "Save Mother Earth <3 <3 <3",
                            "R-E-C-Y-C-L-E !!!",
                            "I just like to recycle.",
                            "I am not very funny,\nI just keep recycling jokes!",
                            "I have 'bin' recycling.",
                            "What have Louth been doing?\nLouth's 'bin' recycling"]
        self.layoutMain = BoxLayout()
        self.text_display = Label(text = self.list_quotes[1], font_size = 48, halign = "center")
        self.layoutMain.add_widget(self.text_display)
        self.add_widget(self.layoutMain)
        
        Clock.schedule_interval(self.my_callback, 5)
        
    def my_callback(self,dt):
        val = random.randint(0,9)
        self.text_display.text = self.list_quotes[val]
        self.text_display.color = [random.uniform(0,1),random.uniform(0,1),random.uniform(0,1),1]

class GUIConvert_bin(App):
    def build(self):
        self.sm = ScreenManager()
        menu = MenuScreen(name = "menu")
        fail = FailPage(name = "fail")
        confirm = ConfirmationPage(name = "confirmation")
        recycle = RecycledPage(name = "recycle")
        load = LoadingPage(name = "load")
        success = SuccessPage(name = "success")
        ss = ScreenSaver(name = "ss")
        self.sm.add_widget(menu)
        self.sm.add_widget(fail)
        self.sm.add_widget(confirm)
        self.sm.add_widget(recycle)
        self.sm.add_widget(load)
        self.sm.add_widget(success)
        self.sm.add_widget(ss)
        self.sm.current = "menu"
        Clock.schedule_interval(self.my_callback,2)
        return self.sm
        
    def my_callback(self,dt):
        is_object = presence_of_object()
        if is_object == True and self.sm.current == 'ss' :
            self.sm.current = "menu"
        elif self.sm.current == "menu" and is_object == False:
            self.sm.current = "ss"


if __name__=='__main__':
    GUIConvert_bin().run()
    

        
    
