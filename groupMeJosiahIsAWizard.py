#my own attempt at this product. Sorry if its redundant. 
#im going object oriented, just for kicks
import requests
import json

baseURL = "https://api.groupme.com/v3"
accessToken = "VqDGJfkyaRcR77rQoUpRRGB9FsTfOAUg7eSW7shP"
operation = ""
group_ids = []
something = ""

def getGroups(): 
    url = ""
    url = baseURL + "/groups?token=" + accessToken 

    req = requests.get(url)
    data = req.json()["response"]

    for i in data:
        group_ids.append(i["id"])


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

        last_message_id = out_messages[0]["id"]
        

        while(keep_looking):
            
            lim = data["count"] - len(out_messages)
            
            if (lim > 100):
                temp_data = requests.get(url + "&limit=100&before_id=" + last_message_id).json()["response"]
                out_messages = temp_data["messages"] + out_messages

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

    
    

def interactive_bs(): 
    accessToken = input("what is your access token?")
    print(accessToken)



def main():
    getGroups()
    


if __name__ == "__main__":
    main() 

    