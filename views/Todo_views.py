def print_menu():
    menu_list = ['Add ToDo', 'Modify item', 'Delete item',
     'Mark item as done', 'Display item\'s list',
     'Display specific todo item\'s details']
    index = 1
    for elm in menu_list:
        print(index, elm)
        index += 1



def main():
    print_menu()

if __name__ == '__main__':
    main()