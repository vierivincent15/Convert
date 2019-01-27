from firebase import firebase

url= "https://dpro-86dcc.firebaseio.com/"
token= "3NIeTUZ3RmcJADd2B2zUPYMyZOqDL9V1QiIZVk0X"

firebase=firebase.FirebaseApplication(url,token)

def retrieve_points():
    '''retrieve points stored in firebase'''
    pts = firebase.get('/pending mass')
    return pts

def delete_pending():
    '''delete pending points stored in firebase'''
    new_pts = 0
    firebase.put('/', "pending mass", new_pts)

def upload_points(value):
    '''upload points to firebase acquired from recycling items'''
    new_pts = value
    firebase.put('/', "pending mass", new_pts)
    