def save_list(lst):
    with open("list.txt", "w") as archive:
        for element in lst:
            archive.write(element + "\n")

def load_list():
    the_list = []
    try:
        with open("list.txt", "r") as archive:
            for line in archive:
                the_list.append(line.strip())
    except FileNotFoundError:
        pass
    return the_list

list_of_things = load_list()
action = ""

while True:
    action = input("What do you want to do? (Add / Remove / List / Close): ")

    if action == "Add":
        add = input("What do you want to add to the list? ")
        list_of_things.append(add)
        save_list(list_of_things)

    elif action == "Remove":
        remove = input("What do you want to remove? ")
        if remove in list_of_things:
            list_of_things.remove(remove)
            save_list(list_of_things)
        else:
            print(f"'{remove}' is not in the list")

    elif action == "List":
        for i, element in enumerate(list_of_things):
            print(f"{i}: {element}")
        if list_of_things == []:
            print("The list is empty")

    elif action == "Close":
        break

    else:
        print("Invalid action. Try again.")
