from Todo_models import Todo
from Todo_views import *
import os

def start_controller():
    print_menu()
    choice = get_choice()
    while choice.isdigit():
        if choice == '1':
            todo_item = add_todo_item()
            #os.system('clear')
            #print_todo_details(todo_item)
            Todo.all_todo_items.append(todo_item)
            break
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            print_todo_items_list(Todo.all_todo_items)
            break
        elif choice == '6':
            pass


def add_todo_item():
    while True:
        name = get_item_name()
        if len(name) > 3:
            print(item_name_too_long())
            continue
        description = get_item_description()
        if len(description) > 3:
            print(item_description_too_long())
            continue
        else:
            return Todo(name, description)


start_controller()
