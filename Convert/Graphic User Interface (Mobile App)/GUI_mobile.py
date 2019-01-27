from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.app import App
from userdata import changepw, update_credits, signup, transaction_list
from authentication import download_data


a= ["1"]
'''variable a is used to store the global variable'''

class LoginPage(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layoutMain = GridLayout(rows = 4)
        self.layout1 = GridLayout(cols = 2)
        self.layout2 = GridLayout(cols = 2)
        self.layout3 = GridLayout(cols = 2)
        self.title_label = Label(text = "CONVERT app", font_size = 72)
        self.student_id = Label(text = "Student ID:", font_size = 40)
        self.id_input = TextInput(text = "", font_size = 40)
        
        self.password = Label(text= "Password:",font_size=40)
        self.pw_input = TextInput(text = "", font_size = 40, password = True)
        
        self.login = Button(text = "Login", font_size = 48, on_press = self.change_screen_to_menu)
        self.sign_up = Button(text = "Sign up", font_size = 48, on_press = self.change_screen_to_register)
        self.layout1.add_widget(self.student_id)
        self.layout1.add_widget(self.id_input)
        self.layout2.add_widget(self.password)
        self.layout2.add_widget(self.pw_input)
        self.layout3.add_widget(self.login)
        self.layout3.add_widget(self.sign_up)
        self.layoutMain.add_widget(self.title_label)
        self.layoutMain.add_widget(self.layout1)
        self.layoutMain.add_widget(self.layout2)
        self.layoutMain.add_widget(self.layout3)
        self.add_widget(self.layoutMain)
        
    def change_screen_to_menu(self, value):
        '''screen can change to either FAIL or MENU depending on the user input.'''
        user_dict = download_data()
        if self.id_input.text in user_dict:
            if self.pw_input.text == user_dict[self.id_input.text]["Password"]:
                a.append(str(self.id_input.text))
                self.manager.transition.direction = "left"
                self.manager.current = "menu"
                ref_to_title.text = 'Student ID: ' + str(a[len(a)-1])
                ref_to_name.text = 'Name: ' + str(user_dict[a[len(a)-1]]["Name"])
                ref_to_credit.text = "Credit: " + str(user_dict[a[len(a)-1]]["Credit"])
            else:
                self.manager.transition.direction = "down"
                self.manager.current = "fail"
        else:
            self.manager.transition.direction = "down"
            self.manager.current = "fail"        
            
    def change_screen_to_register(self,value):
        self.manager.transition.direction = "right"
        self.manager.current = "register"
        
class Register(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layoutMain = GridLayout(rows = 5)
        self.layout1 = GridLayout(cols = 2)
        self.layout2 = GridLayout(cols = 2)
        self.layout3 = GridLayout(cols = 2)
        self.layout4 = GridLayout(cols = 2)
        self.title_label = Label(text = "Register", font_size = 72)
        self.student_name = Label(text = "Full Name:", font_size = 40)
        self.name_input = TextInput(text = "", font_size = 40)
        
        self.student_id = Label(text = "Student ID:", font_size = 40)
        self.id_input = TextInput(text = "", font_size = 40)
        
        self.password = Label(text= "Password:",font_size=40)
        self.pw_input = TextInput(text = "", font_size = 40)
        
        self.sign_up = Button(text = "Sign up", font_size = 48, on_press = self.change_screen_to_login)
        self.bck = Button(text = 'Back', font_size = 48, on_press = self.change_to_bck)
        self.layout1.add_widget(self.student_name)
        self.layout2.add_widget(self.student_id)
        self.layout2.add_widget(self.id_input)
        self.layout3.add_widget(self.password)
        self.layout3.add_widget(self.pw_input)
        self.layout1.add_widget(self.name_input)
        self.layout4.add_widget(self.sign_up)
        self.layout4.add_widget(self.bck)
        self.layoutMain.add_widget(self.title_label)
        self.layoutMain.add_widget(self.layout1)
        self.layoutMain.add_widget(self.layout2)
        self.layoutMain.add_widget(self.layout3)
        self.layoutMain.add_widget(self.layout4)
        self.add_widget(self.layoutMain)
    
    def change_screen_to_login(self,value):
        user_dict = download_data()
        if self.id_input.text not in user_dict:
            signup(self.name_input.text, self.id_input.text, self.pw_input.text)
            self.manager.transition.direction = "left"
            self.manager.current = "login"
        else:
            self.manager.transition.direction = "right"
            self.manager.current = "userexist"

    def change_to_bck(self,value):
        self.manager.transition.direction = 'left'
        self.manager.current = 'login'
        
class Userexist(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.LayoutMain = BoxLayout(orientation = "vertical")
        self.print_invalid = Label(text = "User already exist", font_size = 48)
        self.ok = Button(text = "OK", font_size = 40, on_press = self.change_to_login)
        
        self.LayoutMain.add_widget(self.print_invalid)
        self.LayoutMain.add_widget(self.ok)
        self.add_widget(self.LayoutMain)
        
    def change_to_login(self,value):
        self.manager.transition.direction = "up"
        self.manager.current = "login"

class FailPage(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.LayoutMain = BoxLayout(orientation = "vertical")
        self.print_invalid = Label(text = "Invalid Student ID or Password", font_size = 48)
        self.ok = Button(text = "OK", font_size = 40, on_press = self.change_to_login)
        
        self.LayoutMain.add_widget(self.print_invalid)
        self.LayoutMain.add_widget(self.ok)
        self.add_widget(self.LayoutMain)
        
    def change_to_login(self,value):
        self.manager.transition.direction = "up"
        self.manager.current = "login"
  
class Menu(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layoutmain = GridLayout(rows = 4)
        self.layout1 = GridLayout(cols = 2)
        self.layout2 = GridLayout(cols = 2)
        self.layout3 = GridLayout(cols = 2)
        self.title_label = Label(text = "Display Student ID", font_size = 60)
        self.student_name = Label(text = "Display Name",font_size = 40)
        self.credit = Label(text = "Credit: Display Credit", font_size = 40)
        self.reward = Button(text = "Rewards", font_size = 40, on_press = self.change_to_shop)
        self.history = Button(text = "View History", font_size = 40, on_press =self.change_to_trans_history)
        self.edit = Button(text = "Change Password", font_size = 40, on_press = self.change_to_edit)
        self.exit = Button(text = "Exit", font_size = 40, on_press = self.change_to_login)
        self.layout1.add_widget(self.student_name)
        self.layout1.add_widget(self.reward)
        self.layout2.add_widget(self.credit)
        self.layout2.add_widget(self.history)
        self.layout3.add_widget(self.edit)
        self.layout3.add_widget(self.exit)
        self.layoutmain.add_widget(self.title_label)
        self.layoutmain.add_widget(self.layout1)
        self.layoutmain.add_widget(self.layout2)
        self.layoutmain.add_widget(self.layout3)
        self.add_widget(self.layoutmain)
        
        global ref_to_title
        ref_to_title = self.title_label
        global ref_to_name
        ref_to_name = self.student_name
        global ref_to_credit
        ref_to_credit = self.credit
        
    def change_to_shop(self,value):
        user_dict = download_data()
        self.manager.transition.direction = "left"
        self.manager.current = "shop"
        shop_title.text = "Credit:" + " " + str(user_dict[a[len(a)-1]]["Credit"])
        
    
    def change_to_edit(self,value):
        self.manager.transition.direction = "up"
        self.manager.current = "edit"
    
    def change_to_login(self,value):
        self.manager.transition.direction = "right"
        self.manager.current = "login"
        
    def change_to_trans_history(self,value):
        self.manager.transition.direction = "down"
        self.manager.current = "trans_history"
        history.text = transaction_list(a[len(a)-1])
        
class Transaction_history(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layoutmain = GridLayout(rows = 3)
        self.trans_title = Label(text = 'Your Transaction History', font_size = 60)
        self.trans_history = Label(text = '', font_size = 24, valign = "middle")
        self.bck = Button(text='Back', font_size= 20, on_press=self.change_to_menu)
        self.layoutmain.add_widget(self.trans_title)
        self.layoutmain.add_widget(self.trans_history)
        self.layoutmain.add_widget(self.bck)
        self.add_widget(self.layoutmain)
        
        global history
        history = self.trans_history
    def change_to_menu(self,value):
        self.manager.transition.direction = "up"
        self.manager.current = "menu"
        
class Shop(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layoutmain = GridLayout(rows = 5)
        self.layout1 = GridLayout(cols = 3)
        self.layout2 = GridLayout(cols = 3)
        self.layout3 = GridLayout(cols = 3)
        self.title_label = Label(text = "Credit: Display Credit", font_size = 60)
        self.item1 = Label(text = "Item 1",font_size = 40)
        self.item2 = Label(text = "Item 2", font_size = 40)
        self.item3 = Label(text = "Item 3", font_size = 40)
        self.cost1 = Label(text = "1.00 Credit",font_size = 40)
        self.cost2 = Label(text = "0.99 Credit", font_size = 40)
        self.cost3 = Label(text = "0.01 Credit", font_size = 40)
        self.buy1 = Button(text = "Buy!", font_size = 40, on_press = self.confirm1)
        self.buy2 = Button(text = "Buy!", font_size = 40, on_press = self.confirm2)
        self.buy3 = Button(text = "Buy!", font_size = 40, on_press = self.confirm3)
        self.back = Button(text = "Back", font_size = 40, on_press = self.change_to_menu) 
        self.layout1.add_widget(self.item1)
        self.layout1.add_widget(self.cost1)
        self.layout1.add_widget(self.buy1)
        self.layout2.add_widget(self.item2)
        self.layout2.add_widget(self.cost2)
        self.layout2.add_widget(self.buy2)
        self.layout3.add_widget(self.item3)
        self.layout3.add_widget(self.cost3)
        self.layout3.add_widget(self.buy3)
        self.layoutmain.add_widget(self.title_label)
        self.layoutmain.add_widget(self.layout1)
        self.layoutmain.add_widget(self.layout2)
        self.layoutmain.add_widget(self.layout3)
        self.layoutmain.add_widget(self.back)
        self.add_widget(self.layoutmain)
        global shop_title
        shop_title = self.title_label
        
    def confirm1(self,value):
        self.manager.transition.direction = "up"
        self.manager.current = "confirm_purchase1"
        
    def confirm2(self,value):
        self.manager.transition.direction = "up"
        self.manager.current = "confirm_purchase2"
        
    def confirm3(self,value):
        self.manager.transition.direction = "up"
        self.manager.current = "confirm_purchase3"       
        
    def change_to_menu(self,value):
        user_dict = download_data()
        self.manager.transition.direction = "right"
        self.manager.current = "menu"
        ref_to_credit.text = "Credit: " + str(user_dict[a[len(a)-1]]["Credit"])
    
class Confirm_purchase1(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layoutMain = GridLayout(rows = 2)
        self.layout1 = GridLayout(cols = 2)
        self.confirm = Label(text = "Are you sure you want to buy item 1?", font_size = 48)
        self.yes_button = Button(text = "YES", font_size = 48, on_press = self.change_to_success_)
        self.no_button = Button(text = "NO", font_size = 48, on_press = self.change_to_shop)
        
        self.layout1.add_widget(self.yes_button)
        self.layout1.add_widget(self.no_button)
        self.layoutMain.add_widget(self.confirm)
        self.layoutMain.add_widget(self.layout1)
        self.add_widget(self.layoutMain)
        
    def change_to_success_(self,value):
        user_dict = download_data()
        checkcred = user_dict[a[len(a)-1]]["Credit"]
        if checkcred > 1:
            update_credits(a[len(a)-1], -1)
            self.manager.transition.direction = "left"
            self.manager.current = "successful_purchase"
        else:
            self.manager.transition.direction = "left"
            self.manager.current = "fail_purchase"
        
    def change_to_shop(self,value):
        user_dict = download_data()
        self.manager.transition.direction = "right"
        self.manager.current = "shop"
        shop_title.text = "Credit: " + str(user_dict[a[len(a)-1]]["Credit"])

class Confirm_purchase2(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layoutMain = GridLayout(rows = 2)
        self.layout1 = GridLayout(cols = 2)
        self.confirm = Label(text = "Are you sure you want to buy item 2?", font_size = 48)
        self.yes_button = Button(text = "YES", font_size = 48, on_press = self.change_to_success_)
        self.no_button = Button(text = "NO", font_size = 48, on_press = self.change_to_shop)
        
        self.layout1.add_widget(self.yes_button)
        self.layout1.add_widget(self.no_button)
        self.layoutMain.add_widget(self.confirm)
        self.layoutMain.add_widget(self.layout1)
        self.add_widget(self.layoutMain)
        
    
    def change_to_success_(self,value):
        user_dict = download_data()
        checkcred = user_dict[a[len(a)-1]]["Credit"]
        if checkcred > 0.99:
            update_credits(a[len(a)-1], -0.99)
            self.manager.transition.direction = "left"
            self.manager.current = "successful_purchase"
        else:
            self.manager.transition.direction = "left"
            self.manager.current = "fail_purchase"
        
    def change_to_shop(self,value):
        user_dict = download_data()
        self.manager.transition.direction = "right"
        self.manager.current = "shop"
        shop_title.text = "Credit: " + str(user_dict[a[len(a)-1]]["Credit"])

class Confirm_purchase3(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layoutMain = GridLayout(rows = 2)
        self.layout1 = GridLayout(cols = 2)
        self.confirm = Label(text = "Are you sure you want to buy item 3?", font_size = 48)
        self.yes_button = Button(text = "YES", font_size = 48, on_press = self.change_to_success_)
        self.no_button = Button(text = "NO", font_size = 48, on_press = self.change_to_shop)
        self.layout1.add_widget(self.yes_button)
        self.layout1.add_widget(self.no_button)
        self.layoutMain.add_widget(self.confirm)
        self.layoutMain.add_widget(self.layout1)
        self.add_widget(self.layoutMain)
        
    def change_to_success_(self,value):
        user_dict = download_data()
        checkcred = user_dict[a[len(a)-1]]["Credit"]
        if checkcred > 0.01:
            update_credits(a[len(a)-1], -0.01)
            self.manager.transition.direction = "left"
            self.manager.current = "successful_purchase"
        else:
            self.manager.transition.direction = "left"
            self.manager.current = "fail_purchase"
        
        
        
    def change_to_shop(self,value):
        user_dict = download_data()
        self.manager.transition.direction = "right"
        self.manager.current = "shop"
        shop_title.text = "Credit: " + str(user_dict[a[len(a)-1]]["Credit"])
    
class Purchase_success(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layoutMain = BoxLayout(orientation = "vertical")
        self.print_success = Label(text = "Successful purchase", font_size = 72)
        self.ok = Button(text = "OK", font_size = 48, on_press = self.change_to_shop)
        
        self.layoutMain.add_widget(self.print_success)
        self.layoutMain.add_widget(self.ok)
        self.add_widget(self.layoutMain)
        
    def change_to_shop(self,value):
        user_dict = download_data()
        self.manager.transition.direction = "left"
        self.manager.current = "shop"
        shop_title.text = "Credit: " + str(user_dict[a[len(a)-1]]["Credit"])

class Purchase_fail(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.LayoutMain = BoxLayout(orientation = "vertical")
        self.print_invalid = Label(text = "You do not have enough Credits", font_size = 48)
        self.ok = Button(text = "OK", font_size = 40, on_press = self.change_to_shop)
        
        self.LayoutMain.add_widget(self.print_invalid)
        self.LayoutMain.add_widget(self.ok)
        self.add_widget(self.LayoutMain)
        
    def change_to_shop(self,value):
        user_dict = download_data()
        self.manager.transition.direction = "up"
        self.manager.current = "shop"
        shop_title.text = "Credit: " + str(user_dict[a[len(a)-1]]["Credit"])
        
      
class Edit(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layoutMain = GridLayout(rows = 5)
        self.layout1 = GridLayout(cols = 2)
        self.layout2 = GridLayout(cols = 2)
        self.layout3 = GridLayout(cols = 2)
        self.layout4 = GridLayout(cols = 2)
        self.title_label = Label(text = "Change Password", font_size = 72)
        self.oldpw = Label(text = "Old Password:", font_size = 40)
        self.oldpw_input = TextInput(text = "", font_size = 40)
        
        self.newpw = Label(text = "New Password", font_size = 40)
        self.newpw_input = TextInput(text = "", font_size = 40)
        
        self.cfmpw = Label(text= "Confirm New Password",font_size=40)
        self.cfmpw_input = TextInput(text = "", font_size = 40)
        
        self.cfm = Button(text = "Confirm Changes", font_size = 48, on_press = self.change_screen)
        self.bck = Button(text = "Back", font_size = 48, on_press = self.change_to_menu)
        self.layout1.add_widget(self.oldpw)
        self.layout2.add_widget(self.newpw)
        self.layout2.add_widget(self.newpw_input)
        self.layout3.add_widget(self.cfmpw)
        self.layout3.add_widget(self.cfmpw_input)
        self.layout1.add_widget(self.oldpw_input)
        self.layout4.add_widget(self.cfm)
        self.layout4.add_widget(self.bck)
        self.layoutMain.add_widget(self.title_label)
        self.layoutMain.add_widget(self.layout1)
        self.layoutMain.add_widget(self.layout2)
        self.layoutMain.add_widget(self.layout3)
        self.layoutMain.add_widget(self.layout4)
        
        self.add_widget(self.layoutMain)
    def change_screen(self,value):
        user_dict = download_data()
        if self.oldpw_input.text == user_dict[a[len(a)-1]]["Password"] :
             if self.newpw_input.text == self.cfmpw_input.text and self.oldpw_input.text !=self.newpw_input.text:
                 global newpw
                 newpw = self.newpw_input.text
                 self.manager.transition.direction = "up"
                 self.manager.current = "confirmation"
             else:
                 self.manager.transition.direction = "up"
                 self.manager.current = "invalid_pw"
        else:
            self.manager.transition.direction = "up"
            self.manager.current = "invalid_pw"
    def change_to_menu(self,value):
        self.manager.transition.direction = "right"
        self.manager.current = "menu"
        
                 
class Invalid_pw(Screen):
    
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.LayoutMain = BoxLayout(orientation = "vertical")
        self.print_invalid = Label(text = "Your new Password is invalid", font_size = 48)
        self.ok = Button(text = "OK", font_size = 40, on_press = self.change_to_edit)
        self.LayoutMain.add_widget(self.print_invalid)
        self.LayoutMain.add_widget(self.ok)
        self.add_widget(self.LayoutMain)
        
    def change_to_edit(self,value):
        self.manager.transition.direction = "up"
        self.manager.current = "edit"
        
class ConfirmationPage(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layoutMain = GridLayout(rows = 2)
        self.layout1 = GridLayout(cols = 2)
        self.confirm = Label(text = "Are you sure?", font_size = 48)
        self.yes_button = Button(text = "YES", font_size = 48, on_press = self.change_to_success)
        self.no_button = Button(text = "NO", font_size = 48, on_press = self.change_to_menu)
        
        self.layout1.add_widget(self.yes_button)
        self.layout1.add_widget(self.no_button)
        self.layoutMain.add_widget(self.confirm)
        self.layoutMain.add_widget(self.layout1)
        self.add_widget(self.layoutMain)
        
    def change_to_success(self,value):
        self.manager.transition.direction = "left"
        self.manager.current = "success"
        changepw(a[len(a)-1],newpw)
        
    def change_to_menu(self,value):
        self.manager.transition.direction = "right"
        self.manager.current = "menu"

class SuccessPage(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layoutMain = BoxLayout(orientation = "vertical")
        self.print_success = Label(text = "Success", font_size = 72)
        self.ok = Button(text = "OK", font_size = 48, on_press = self.change_to_menu)
        
        self.layoutMain.add_widget(self.print_success)
        self.layoutMain.add_widget(self.ok)
        self.add_widget(self.layoutMain)
        
    def change_to_menu(self,value):
        self.manager.transition.direction = "left"
        self.manager.current = "menu"

class GUIConvert_bin(App):
    def build(self):
        sm = ScreenManager()
        login = LoginPage(name = "login")
        fail = FailPage(name = "fail")
        menu = Menu(name= "menu")
        edit = Edit(name="edit")
        userexist = Userexist(name="userexist")
        register = Register(name="register")
        confirm = ConfirmationPage(name = "confirmation")
        success = SuccessPage(name = "success")
        shop = Shop(name = "shop")
        invalid_pw = Invalid_pw(name="invalid_pw")
        confirm_purchase1 = Confirm_purchase1(name= "confirm_purchase1")
        confirm_purchase2 = Confirm_purchase2(name= "confirm_purchase2")
        confirm_purchase3 = Confirm_purchase3(name= "confirm_purchase3")
        successful_purchase = Purchase_success(name = "successful_purchase")
        fail_purchase = Purchase_fail(name= "fail_purchase")
        transaction_history = Transaction_history(name= "trans_history")
        sm.add_widget(userexist)
        sm.add_widget(login)
        sm.add_widget(register)
        sm.add_widget(menu)
        sm.add_widget(fail)
        sm.add_widget(confirm)
        sm.add_widget(edit)
        sm.add_widget(success)
        sm.add_widget(shop)
        sm.add_widget(confirm_purchase1)
        sm.add_widget(confirm_purchase2)
        sm.add_widget(confirm_purchase3)
        sm.add_widget(successful_purchase)
        sm.add_widget(invalid_pw)
        sm.add_widget(fail_purchase)
        sm.add_widget(transaction_history)
        sm.current = "login"
        return sm

if __name__=='__main__':
    GUIConvert_bin().run()
    
