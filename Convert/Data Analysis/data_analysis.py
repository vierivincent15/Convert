import numpy as np
import matplotlib.pyplot as plt
from authentication import download_data

def get_purchase_data():
    '''extract and process item purhase data'''
    user_data = download_data()
    transaction_list = []
    for key in user_data:
        if isinstance(user_data[key],dict):
            '''this if statement is to check for user and not other element of the database'''
            ls = user_data[str(key)]["History"]
            transaction_list.extend(ls)
    item_dict = {}
    for item in transaction_list:
        if float(item)<0:
            item = -1*item
            key = "Item(Price: {}pts)".format(str(item))
            if key not in item_dict:
                item_dict[key] = 1
            else:
                item_dict[key] += 1
    return item_dict
    
def display_data(data_dict):
    '''display bar chart to show relationship between item and its popularity'''
    list_key = list(data_dict.keys())
    list_key = np.array(list_key)
    list_value = list(data_dict.values())
    list_value = np.array(list_value)
    position = [0,1,2]
    position = np.array(position)
    
    plt.bar(position, list_value, 0.5, color = "maroon")
    plt.title("Item Popularity Chart")
    plt.xticks(position, list_key)
    plt.ylabel("frequency")
    plt.show()
    
def display_suggestion(data_dict):
    '''display suggestion based on item popularity data'''
    list_key = list(data_dict.keys())
    least_popular = [list_key[0]]
    most_popular = [list_key[0]]
    for key in data_dict:
        if int(data_dict[key]) <= data_dict[least_popular[0]]:
            least_popular[0] = key
        if int(data_dict[key]) >= data_dict[most_popular[0]]:
            most_popular[0] = key
    least_popular.append(data_dict[least_popular[0]])
    most_popular.append(data_dict[most_popular[0]])
    leastpopular_string = "Based on the item popularity trend, {} is the least popular with only {} purchases. You may want to either review the price or seek for alternative reward.".format(least_popular[0], least_popular[1])
    mostpopular_string = "Based on the item popularity trend, {} is the most popular with {} purchases. You may want to keep this item on your reward list.".format(most_popular[0], most_popular[1])
    suggestion_string = leastpopular_string + "\n\n" + mostpopular_string
    return suggestion_string

users_data = get_purchase_data()
display_data(users_data)
print(display_suggestion(users_data))
        
    