from firebase import firebase

url = "https://dpro-86dcc.firebaseio.com/" # URL to Firebase database
token = "3NIeTUZ3RmcJADd2B2zUPYMyZOqDL9V1QiIZVk0X" # unique token used for authentication


firebase = firebase.FirebaseApplication(url, token)

class User():
    def __init__(self, name, student_id, password, credit=0, history=[0]):
        self._name = name
        self._student_id = student_id
        self._password = password
        self._credit = credit
        self._history = history
        
    def upload (self):
        student_details = {"Name":self._name,"ID":self._student_id,"Password":self._password,"Credit":self._credit, "History":self._history}  
        firebase.put('/', str(self._student_id), student_details)
        return student_details

def signup(name, student_id, password):
    '''function to sign up user to our database'''
    User(name, student_id, password).upload()
    
   
            
def changepw(student_id,new_password):
    '''change password of a particular user'''
    user_dict = firebase.get('/')
    if str(student_id) in user_dict:
        details = user_dict[str(student_id)]
        if new_password !=details["Password"] and new_password != None:
            name = details["Name"]
            credit = details["Credit"]
            b= User(name,student_id,new_password,credit)
            b.upload()
          

def update_credits(student_id, credit_change):
    '''update credits and history list of a particular user'''
    user_dict = firebase.get('/')
    if str(student_id) in user_dict:
        details = user_dict[str(student_id)]
        NewCredit = float(details["Credit"]) + float(credit_change)
        name = details["Name"]
        password = details["Password"]
        old_hist = details["History"]
        old_hist.append(credit_change)
        updatehistory = old_hist
        b= User(name,student_id,password,NewCredit,updatehistory)
        b.upload()
            
            
            
def transaction_list(student_id):
    '''text that will pop out upon the request of showing transaction history'''
    user_dict = firebase.get('/')
    list_ = ''
    transaction_history = user_dict[student_id]["History"]
    inverted_history = transaction_history[::-1]
    if len(inverted_history) <=9:
        for i in inverted_history:
            if i>0:
                list_ = list_ + "From Bin             +{}\n".format(i)
            if i<0:
                list_ = list_ + "From Shop            {}\n".format(i)
    if len(inverted_history) >= 10:
        trimmed_history = inverted_history[:7]
        for i in trimmed_history:
            if i>0:
                list_ = list_ + "From Bin             +{}\n".format(i)
            if i<0:
                list_ = list_ + "From Shop            {}\n".format(i)
    return list_
