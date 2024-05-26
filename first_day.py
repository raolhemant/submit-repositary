# a = 10 
# b = 20
# sum = a + b
# print (sum)
#  #subtract 
#  sum = a-b
#  #division
#  sum = a/b
 

 #i ma going to develop new game ..
# import random
# x = random.randint(1,11)
# print(x)
# y=int(input("enter the value"))
# total_guess=1
# while(x!=y):
#     if total_guess==5:
#         print("guess limit reached ")
#         break
#     y = int(input("guess the number:"))
#     total_guess = total_guess+1
# if y == x:   
#     print(f'congratulation your guess is{total_guess} time ')
import random
# Define the rooms of the dungeon
rooms = {
    'entrance': {
        'description': 'You are at the entrance of the dungeon. There are three doors in front of you.',
        'doors': ['room1', 'room2', 'room3']
    },
    'room1': {
        'description': 'You enter a dark room with eerie sounds echoing. You see a faint glimmer in the corner.',
        'treasure': 'gold'
    },
    'room2': {
        'description': 'You step into a room filled with cobwebs. Something skitters across the floor.',
        'trap': 'spike pit'
    },
    'room3': {
        'description': 'This room is empty except for a massive chest in the center.',
        'treasure': 'diamonds'
    }
}

# Define player attributes
player = {
    'current_room': 'entrance',
    'inventory': []
}

# Define game functions
def display_room():
    print(rooms[player['current_room']]['description'])

def move(direction):
    if direction in rooms[player['current_room']]['doors']:
        player['current_room'] = direction
        display_room()
    else:
        print("You can't go that way!")

def check_room():
    current_room = rooms[player['current_room']]
    if 'treasure' in current_room:
        print(f"You found {current_room['treasure']}!")
        player['inventory'].append(current_room['treasure'])
        del current_room['treasure']
    elif 'trap' in current_room:
        print(f"You fell into a {current_room['trap']}!")
        # Implement trap consequences here

# Main game loop
def main():
    print("Welcome to the Dungeon!")
    display_room()

    while True:
        command = input("What would you like to do? (move/check/quit) ").lower()
        
        if command == 'quit':
            print("Thanks for playing!")
            break
        elif command == 'move':
            direction = input("Which direction would you like to move? (room1/room2/room3) ").lower()
            move(direction)
        elif command == 'check':
            check_room()
            display_room()
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()
