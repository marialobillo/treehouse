import os
# Create a new empty list named shopping_list
shopping_list = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# create a function named add_to_list that declares a parameter named item
def add_to_list(item):
    show_list()
    if len(shopping_list):
        position = input("Where should I add {}?\n"
                "Press ENTER to add to the end of the list\n"
                "> ".format(item))
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(new_item)

    show_list()



def show_help():
    clear_screen()
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
ENTER 'SHOW' for see the complete list.
""")


def show_list():
    clear_screen()
    print("Here's your list:")

    index = 1
    for item in shopping_list:
        print("{}. {}".format(index, item))
        index += 1
    print("-"*10)


show_help()

while True:
    new_item = input("> ")

    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    else:
        # call add_to_list with new_item as an argument
        add_to_list(new_item)

show_list()
