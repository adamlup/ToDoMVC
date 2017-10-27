def print_menu():
    choice_list = ['Add ToDo', 'Modify item', 'Delete item',
                   'Mark item as done', 'Display item\'s list',
                   'Display specific todo item\'s details']
    index = 1
    for elm in choice_list:
        print(index, elm)
        index += 1
    
def print_todo_items_list(todo_list):
    for elm in todo_list:
        print(elm)



def get_choice():
    return input('Enter your choice ')


def get_item_name():
    return input('Enter item name ')


def get_item_description():
    return input('Enter item description ')


def main():
    print_menu()


if __name__ == '__main__':
    main()

