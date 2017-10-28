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
            print_todo_items_list(Todo.all_todo_items)
            choice_item_by_index = choice_item_by_index()
            for i in Todo.all_todo_items:
                if i == Todo.all_todo_items[choice_item_by_index]:
                    i.name = get_item_name()
                    i.description = get_item_description()
                    break
            break

        elif choice == '3':
            choice_item_by_index = get_item_index()
            for i in Todo.all_todo_items:
                if i == Todo.all_todo_items[choice_item_by_index]:
                    Todo.all_todo_items.remove(i)
            break

        elif choice == '4':
            choice_item_by_index = get_item_index()
            for i in Todo.all_todo_items:
                if i == Todo.all_todo_items[choice_item_by_index]:
                    i.is_done = True
                    return

        elif choice == '5':
            print_todo_items_list(Todo.all_todo_items)
            break

        elif choice == '6':
            index = 0
            for i in Todo.all_todo_items:
                print_todo_item_details(i, index)
                index += 1
            break



def add_todo_item():
    while True:
        name = get_item_name()
        if len(name) > 20:
            print(item_name_too_long())
            continue
        description = get_item_description()
        if len(description) > 150:
            print(item_description_too_long())
            continue
        else:
            return Todo(name, description)


start_controller()
