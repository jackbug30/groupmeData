import requests

baseURL = "https://api.groupme.com/v3"
accessToken = "[your token here]"
groupID = "[group id, from getGroups(), here]"

def getBreakdown():
    users = {}
    while True: #api will only return small groups of messages so have to do lots
        try:
            url = baseURL + "/groups/" + groupID + "/messages?token=" + accessToken + "&before_id=" + lastID
        except:
            url = baseURL + "/groups/" + groupID + "/messages?token=" + accessToken
        r = requests.get(url)
        data = r.json() #data now in JSON
        for x in range(20): #iterate through the 20 messages in this block
            try:
                name = data['response']['messages'][x]['name'] #most recent message ID
            except:
                break
            try:
                users[name] += 1
            except:
                users[name] = 1
        try:
           lastID = data['response']['messages'][19]['id']
        except:
            break
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



#api sends sender_id (not user_id) and sender_typer (user or system)...
#system id is 'system'
#wanted = data['response']['messages'][0]['id'] #most recent message ID
