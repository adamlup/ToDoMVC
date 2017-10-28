from Todo_models import Todo
from Todo_views import *
import os
import sys


def start_controller():
    print_menu()
    choice = get_choice()
    os.system('clear')
    while choice.isdigit():
        if choice == '1':
            todo_item = add_todo_item()
            Todo.all_todo_items.append(todo_item)
            break
        elif choice == '2':
            modify_item()
            break

        elif choice == '3':
            remove_item()
            break

        elif choice == '4':
            change_item_status()
            break

        elif choice == '5':
            print_todo_items_list(Todo.all_todo_items)
            break

        elif choice == '6':
            index = 0
            for i in Todo.all_todo_items:
                print_todo_item_details(i, index)
                index += 1
            break

        elif choice == '7':
            sys.exit(0)

        else:
            return invalid_input()


def add_todo_item():
    while True:
        name = get_item_name()
        if len(name) > 20:
            item_name_too_long()
            continue
        description = get_item_description()
        if len(description) > 150:
            item_description_too_long()
            continue
        else:
            return Todo(name, description)


def modify_item():
    while True:
        choice_item_by_index = get_item_index()
        if choice_item_by_index.isdigit():
            choice_item_by_index = int(choice_item_by_index)
            if choice_item_by_index in range(len(Todo.all_todo_items)):
                for i in Todo.all_todo_items:
                    if i == Todo.all_todo_items[choice_item_by_index]:
                        i.name = get_item_name()
                        i.description = get_item_description()
                break
            else:
                return invalid_input()
        else:
            return invalid_input()


def remove_item():
    while True:
        choice_item_by_index = get_item_index()
        if choice_item_by_index.isdigit():
            choice_item_by_index = int(choice_item_by_index)
            if choice_item_by_index in range(len(Todo.all_todo_items)):
                for i in Todo.all_todo_items:
                    if i == Todo.all_todo_items[choice_item_by_index]:
                        Todo.all_todo_items.remove(i)
                break
            else:
                return invalid_input()
        else:
            return invalid_input()


def change_item_status():
    while True:
        choice_item_by_index = get_item_index()
        if choice_item_by_index.isdigit():
            choice_item_by_index = int(choice_item_by_index)
            if choice_item_by_index in range(len(Todo.all_todo_items)):
                for i in Todo.all_todo_items:
                    if i == Todo.all_todo_items[choice_item_by_index]:
                        i.is_done = True
                break
            else:
                return invalid_input()
        else:
            return invalid_input()
