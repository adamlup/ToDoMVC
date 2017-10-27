from Todo_models import Todo
from Todo_views import *

def start_controller():
    print_menu()
    choice = get_choice()
    while choice.isdigit():
        if choice == '1':
            todo_item = add_todo_item()
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
        elif choice == '6':
            pass
    
def add_todo_item():
    name = get_item_name()
    description = get_item_description()
    return name, description

start_controller()