
from breakdown_processing import *
from visualize_data import *
            
def main():
    getGroups()
    messages = get_messages(group_ids[0])
    breakdown = user_breakdown(messages)

    
    


if __name__ == "__main__":
    main() 

    