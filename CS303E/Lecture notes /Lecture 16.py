'''
#1
def find_common_players(roster1, roster2):
    common_players = set()

    for elem in roster1:
        if elem in roster2:
            common_player.add(elem)
    return common_player

    # return roster1.intersection(roster2)
            
def main():
    roster1 = {'Ana', 'Bob'}
    roster2 = {'Ana', 'Bou'}
'''
#2
def add_contact(phonebook, name, number):
    if name not in phonebook:
        phonebook[name] = number             #take the number and create a new pair
        print("added")
    else:
        print("already in the phonebook!")
        
def seartch_contact(phonebook, name):
    HMM
    
def display_contact(phonebook):
    if phonebook:           #treat list as boolean
        print("Phonebook")
    
    #print(phonebook.items())

    #for name, number in phonebook.item():
         #print(f"{name}: {number}")

def main():
    phonebook = {}
    
    add_contact(phonebook, "Angela", "9728163608")
    display_contact(phonebook)
    
main()

