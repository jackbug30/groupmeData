
# I use this for testing, and for an interface controller later. 

from breakdown_processing import get_groups, get_messages, user_breakdown
from visualize_data import top_text_pi_plot, top_liked_messages, keyword_search
            


def intro_music():
    print("ill get creative here later")


#encapsulates basic config work, pretty self explanitory
def choose_group():
    try: 
        g_count = input("How many groups (starts with the most recent)  ")

        if (g_count == "q"):
            return
        groups = get_groups(g_count)

    except:
        print("Invalid input.")

    for i in range(len(groups)):
        print(str(i + 1) + " " + groups[i]["name"])

    while(True):
        try:
            chosen_id = int(input(""))
            return groups[chosen_id - 1]
             
        except:
            print("\n you chose an invalid option. \n")
    return 

def choose_execute_operation(group):
    options = ["pi chart  of top texters", "Top liked messages", "keyword search"]
    messages = get_messages(group["id"])

    print("\n options for operations on the group. \n")
    for i in range(len(options)):
        print(str(i + 1) + " " + options[i])

    while(True):
        try:
            choice = input("")
            
            if (choice == "q"):
                return 
            
            elif (choice == "1"):
                print("how many users?")
                
                try:
                    num = int(input(""))
                    top_text_pi_plot(num, user_breakdown(messages))
                except:
                    print("invalid number")

            elif (choice == "2"):
                print("How many messages?")

                try:
                    num = int(input(""))
                    top_liked_messages(num, messages)
                except:
                    print("invalid number")
            
            elif (choice == "3"):
                print("\n Type in key words to search for in the messages. Seperate them with a space. \n")
                key_words = input("").split()

                keyword_search(messages, key_words)

        except:
            print("you entered an invalid input")

def main():
    
    intro_music()

    while (True):
        group = choose_group()
        choose_execute_operation(group)

if __name__ == "__main__":
    main() 

    