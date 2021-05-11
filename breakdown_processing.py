#manages requests and formats data for the visualization and controller

import requests
import json


baseURL = "https://api.groupme.com/v3"
accessToken = "VqDGJfkyaRcR77rQoUpRRGB9FsTfOAUg7eSW7shP"

def get_groups(num): 
    url = ""
    try:
        url = baseURL + "/groups?token=" + accessToken + "&per_page=" + num
    except:
        print("Got you a bad token or a bad group count.")
        return 

    req = requests.get(url)
    data = req.json()["response"]
    return data
    #print(json.dumps(data, sort_keys=True, indent=4))

  
    


def get_messages(group_id):
    url = baseURL + "/groups/" + group_id + "/messages?token=" + accessToken
    data = requests.get(url).json()["response"]

    #message requesting has a limit, this checks for the limit and makes multiple pulls if needed. 

    if (data["count"] > 100):
        out_messages = []
        keep_looking = True

    
        #first 100
        data = requests.get(url + "&limit=100").json()["response"] 
        out_messages = out_messages + data["messages"]

        last_message_id = out_messages[99]["id"]
    
        while(keep_looking):
            
            lim = data["count"] - len(out_messages)
            
            if (lim > 100):
                temp_data = requests.get(url + "&limit=100&before_id=" + last_message_id).json()["response"]
                out_messages = temp_data["messages"] + out_messages
                last_message_id = out_messages[99]["id"]

            else:
                
                temp_data = requests.get(url + "&limit=" + str(lim) + "&before_id=" + str(last_message_id)).json()["response"]
                out_messages = temp_data["messages"] + out_messages
                keep_looking = False
        

        return out_messages

    elif (data["count"] > 20):
        data_new = requests.get(url + "&limit=100").json()["response"]
        return data_new
    

    else:
        return data

    

def user_breakdown(messages):
    users = {}

    for m in messages:
        
        if m["name"] in users.keys():
            users[m["name"]]["message_count"] += 1 
            users[m["name"]]["total_likes"] += len(m["favorited_by"])
            users[m["name"]]["texts"].insert(0, m["text"])
        
        else:
            new_user = {
                "message_count": 1,
                "total_likes": len(m["favorited_by"]),
                "texts": [m["text"]]
            }
            users[m["name"]] = new_user

    return users