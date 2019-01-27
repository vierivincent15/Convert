from firebase import firebase

url= "https://dpro-86dcc.firebaseio.com/"
token= "3NIeTUZ3RmcJADd2B2zUPYMyZOqDL9V1QiIZVk0X"

firebase=firebase.FirebaseApplication(url,token)

def download_data():
    '''retrieve data from firebase for a particular user'''
    user_dict = firebase.get('/')
    return user_dict
    
def invalid_user(ID):
    '''text that will pop out when input ID does not match any ID in database'''
    return("{} is not a valid user!\nPlease enter a valid Student Id.".format(ID))
    
def print_confirmation(ID):
    '''confirmation text to ensure that the input ID match the user's ID'''
    return("Are you sure that {} is your Student ID?".format(ID))
    
def success_page(student_id, pts):
    '''text that will pop out upon successful recycling attempt'''
    user_dict = download_data()
    one_data = user_dict[str(student_id)]
    data_id = "Student_ID           :  " + str(one_data['ID'])
    data_credit = "Current Credit       :  " + str(one_data['Credit'])
    delta_credit = "Recycling Points  :  " + str(float(pts))
    new_credit = "New Credit            :  " + str(float(one_data['Credit']) + float(pts))
    success = "Successful! :)"
    
    new_string = "{:^20}\n\n\n{:<30}\n{:<30}\n{:<30}\n{:<30}".format(success, data_id, data_credit, delta_credit, new_credit)
    return new_string
                