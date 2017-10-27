from Todo_models import Todo


def print_menu():
    choice_list = ['Add ToDo', 'Modify item', 'Delete item',
                   'Mark item as done', 'Display item\'s list',
                   'Display specific todo item\'s details']
    index = 1
    for elm in choice_list:
        print(index, elm)
        index += 1


def print_todo_items_list(todo_list):
    index = 1
    for elm in todo_list:
        print_todo_details(elm, index)
        index += 1


def print_todo_details(todo_item, index):
    print("================")
    print(index)
    print("name: ", todo_item.name)
    print("status: ", todo_item.is_done)
    print("description: ", todo_item.description)
    print("================")


def get_choice():
    return input('Enter your choice: ')


def get_item_name():
    return input('Enter item name: ')


def get_item_description():
    return input('Enter item description: ')

def item_name_too_long():
    return 'Too long item name, maximum 20 characters.'

def item_description_too_long():
    return 'Too long item description, maximum 150 characters'

def main():
    print_menu()


if __name__ == '__main__':
    main()
