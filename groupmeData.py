import requests

baseURL = "https://api.groupme.com/v3"
accessToken = "[your token here]"
groupID = "[group id, from getGroups(), here]"

def getBreakdown():
    users = {} #dictionary to hold user:# of messages
    while True: #api will only return groups of 20 messages so have to do lots
        try:
            url = baseURL + "/groups/" + groupID + "/messages?token=" + accessToken + "&before_id=" + lastID #before_id gives the 20 messages before that id
        except:
            url = baseURL + "/groups/" + groupID + "/messages?token=" + accessToken #first time scanning? before_id doesn't exist, omit to get 20 most recent
        r = requests.get(url)
        data = r.json() #data now in JSON
        for x in range(20): #iterate through the 20 messages in this block
            try:
                name = data['response']['messages'][x]['name'] #pull the name out
            except:
                break #if at end of messages, it won't exist. leave while True loop
            try:
                users[name] += 1 #increment user message count
            except:
                users[name] = 1 #or add their name to the dictionary
        try:
           lastID = data['response']['messages'][19]['id'] #get last message id to get 20 previous
        except:
            break #or already at end of list, leave while True loop
    #print(users)
    #print(len(users))
    usersList = users.keys()
    total = 0
    for user in usersList:
        total += users[user]
    #for user in usersList:
    #    print(user + " " + str(round(users[user]/total*100, 4)))
    ranking = []
    for user in usersList: #organizes users into list of tuples
        myTuple = (users[user], user, str(round(users[user]/total*100,2)))
        ranking.append(myTuple)
    ranking.sort()
    print(ranking)
    for user in ranking:
        print(user[1], user[2] + "%", user[0])
    print("Total messages: " + str(total))
    print("Total users: " + str(len(users)))


def getGroups(): #much improvement to be made, later
    url = baseURL + "/groups?per_page=100&omit=memberships&token=" + accessToken #&item=value$etc
    response = requests.get(url)
    data = response.json()
    print(data)

def main(): 
    accessToken = input("Enter your access token")
    getBreakdown()
    

if __name__ == "__main__":
    main()  

#api sends sender_id (not user_id) and sender_typer (user or system)...
#system id is 'system'
#wanted = data['response']['messages'][0]['id'] #most recent message ID
