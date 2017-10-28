def print_menu():
    choice_list = ['Add ToDo', 'Modify item', 'Delete item',
                   'Mark item as done', 'Display item\'s list',
                   'Display specific todo item\'s details', 'Exit']
    index = 1
    for elm in choice_list:
        print(index, elm)
        index += 1


def print_todo_items_list(todo_list):
    index = 0
    for elm in todo_list:
        print(index)
        print('Name: ', elm.name)
        print('================')
        index += 1


def print_todo_item_details(todo_item, index):
    print('================')
    print('Index: ', index)
    print('Status: ', todo_item.is_done)
    print('Name: ', todo_item.name)
    print('Description: ', todo_item.description)
    print('================')


def get_choice():
    return input('\nEnter your choice: ')


def get_item_name():
    return input('Enter item name: ')


def get_item_description():
    return input('Enter item description: ')


def item_name_too_long():
    return print('Too long item name, maximum 20 characters.')


def item_description_too_long():
    return print('Too long item description, maximum 150 characters')


def get_item_index():
    return input('Choose item index to modifing: ')


def invalid_input():
    return print('Invalid input')
