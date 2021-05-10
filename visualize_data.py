# visualizes data
import matplotlib.pyplot as plt 
import json

#takes the number of users wanted, and then prints a pi plot based on the most texts 
def top_text_pi_plot(num, users):

    # Data to plot
    sizes = []
    labels = []
    user_tups = []
    message_total = 0

    for user in users.keys():
        new_tup = (user, users[user]["message_count"])
        user_tups.append(new_tup)
        message_total += users[user]["message_count"]
    
    user_tups = sorted(user_tups, key=lambda x: x[1], reverse=True)

    for i in range(num):
        percentage = str(round((user_tups[i][1]/message_total) * 100, 2)) + "%"
        labels.append(user_tups[i][0] + " " + percentage)
        sizes.append(user_tups[i][1])

    # Plot
    plt.pie(sizes, labels=labels, shadow=True, startangle=140)
   
    plt.axis('equal')
    plt.show()


def top_liked_messages(num, messages):

    message_pairs = [[len(mess["favorited_by"]),mess["text"], mess["name"]] for mess in messages]

    sorted_messages = sorted(message_pairs, key=lambda x: x[0], reverse=True)

    print("\n \n " + "-------------------")
    for i in range(num):
        print(str(i + 1) + "\n" + sorted_messages[i][1] + "\n \n" + "   Likes: " + str(sorted_messages[i][0]) + "\n   Author: " + str(sorted_messages[i][2]))
        print("-------------------")


def keyword_search(messages, key_words): 
        
    keeper_messages = []

    for mess in range(len(messages)): 
        try:
            for word in key_words:
                if word in messages[mess]["text"]:
                    keeper_messages.append(messages[mess])
        except:
            pass

    print("--------------------")
        
    for km in keeper_messages:
        print(km["text"])
        print("   Author: " + km["name"])
        print("   likes: " + str(len(km["name"])) + "\n") 
        print("--------------------")   


