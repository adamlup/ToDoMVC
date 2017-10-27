def print_menu():
    choice_list = ['Add ToDo', 'Modify item', 'Delete item',
                   'Mark item as done', 'Display item\'s list',
                   'Display specific todo item\'s details']
    index = 1
    for elm in choice_list:
        print(index, elm)
        index += 1
    
def print_todo_items_list(todo_list):
    print('Item Name')
    print(todo_list.name)
    print('Todo description')
    print(todo_list.description)


def get_choice():
    return input('Enter your choice: ')


def get_item_name():
    return input('Enter item name: ')


def get_item_description():
    return input('Enter item description: ')


def main():
    print_menu()


if __name__ == '__main__':
    main()
