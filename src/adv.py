from room import Room
from player import Player
import shutil

# Declare all the rooms


def main():

    room = {
        'outside':  Room("Outside Cave Entrance",
                         "North of you, the cave mount beckons", ["Old Rusty Hammer"]),

        'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
    passages run north and east.""", ["Dusty Harmonica", "Amazon Basics Longsword"]),

        'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
    into the darkness. Ahead to the north, a light flickers in
    the distance, but there is no way across the chasm.""", ["Telescope"]),

        'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
    to north. The smell of gold permeates the air.""", ["Mushroom"]),

        'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
    chamber! Sadly, it has already been completely emptied by
    earlier adventurers. The only exit is to the south.""", ["Thank-You-Note"]),
        'Amazon Returns Center': Room("Amazon Returns Center", """\033[1;31;40mYou are greeted by the legendary Jeff Bezos, who serves you lawsuit papers the moment you enter the building.\n\tYou Win!\033[0m""", ["Lawsuit Forms"]),
    }

    # Link rooms together

    room['outside'].assign_room('s', room['foyer'])
    room['foyer'].assign_room('s', room['overlook'])
    room['foyer'].assign_room('w', room['narrow'])
    room['overlook'].assign_room('n', room['foyer'])
    room['narrow'].assign_room('s', room['treasure'])
    room['treasure'].assign_room('s', room['Amazon Returns Center'])

    valid_choices = list('newsqi') + ['inventory']
    # room['narrow'].n_to = room['treasure']
    # room['treasure'].s_to = room['narrow']

    #
    # Main
    #

    # Make a new player object that is currently in the 'outside' room.

    # Write a loop that:
    #
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.

    def sanitize_input(user_input: str, choices: list):
        return user_input in choices

    player = Player('Zoe', room['outside'])
    screen_width, screen_height = shutil.get_terminal_size()
    while True:
        room = player.get_room()
        print(f"{player}\n\n")
        print(room.get_description() + "\n")

        print("-"*screen_width + "\n")
        user_input = input(
            "Where do you want to go?\n\n\tYou can Travel to the 'n' (North), 's' (South), 'e' (East) and 'w' (West)\n\tYou can also check your inventory by typing 'inventory' or 'i'\n\n\033[1;37;43m Type your response here:\033[0m ").split(' ')
        if (len(user_input) < 1 or (not len(user_input) == 1 and 'get' not in user_input and 'drop' not in user_input)):
            # put an angry demeaning note here
            print("you need to try harder than that.")
            continue

        elif (len(user_input) == 1):
            user_input = ''.join(user_input)
            if (user_input not in valid_choices):
                print(
                    f'Choices can only be {", ".join(valid_choices).rstrip() }.')
                continue

            valid_input = sanitize_input(user_input, valid_choices)
            if not valid_input:
                print("Invalid entry. Please try again.")
            if user_input == 'q':
                print(f'Goodbye, {player.name}')
                break

            if user_input == 'i' or user_input == 'inventory':
                # Inventoryyyy
                print(f"Your inventory: {player.get_inventory()}")
                input("Press Enter to continue...")

                continue

            try:
                player.navigate(user_input)
            except:
                print("wrooooooooooooooooooooooooooong")
        if 'get' in user_input:

            things = user_input
            print(" ".join(things[1:]))
            player.get_item(" ".join(things[1:]))

        if 'drop' in user_input:
            things = user_input
            print(" ".join(things[1:]))
            player.drop_item(" ".join(things[1:]))


if __name__ == "__main__":
    main()
