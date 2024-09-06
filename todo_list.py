task_list = []
completed_task_list = []
status = {}

while True:
    try:
        print("\n Welcome to the To-Do List App! \n")
        menu_selection = input("Menu: \n 1. Add a task \n 2. View Tasks \n 3. Mark a task as complete \n 4. Delete a task \n 5. Quit \n Enter you number selection here: ")

        if menu_selection == "1":
            add_task = input("Please add the task you desire to your To-Do List: ")
            task_list.append(add_task)
            status[add_task] = "Incomplete"
            print("\nCurrent To-Do List: ")
            for k, v in status.items():
                print(f"Task: {k} - Status: {v}")

        elif menu_selection == "2":
            if len(task_list) == 0:
                print("The To-Do List is empty")
            else:
                for k, v in status.items():
                    print(f"Task: {k} - Status: {v}")

        elif menu_selection == "3":
            if len(task_list) == 0:
                print("The To-Do List is empty")
            else:
                for (i, items) in enumerate(task_list):
                    print(i+1, items)
                complete_task = int(input("Which task have you completed? (select the number by the item)"))
                task_item_complete = task_list[complete_task-1]
                completed_task_list.append(task_item_complete)
                status[task_item_complete] = "Complete"               
                task_list.remove(task_item_complete)
                print(f"\nHere is your completed task list: {completed_task_list}")

        elif menu_selection == "4":
            if len(task_list) == 0:
                print("The To-Do List is empty")
            else:
                for (i, items) in enumerate(task_list):
                    print(i+1, items)
                remove_task = int(input("Which would you like to delete? (select the number by the item)"))
                task_item = task_list[remove_task-1]
                task_list.remove(task_item)
            del status[task_item]
            print(f"\nDeleted: {task_item}")

        elif menu_selection == "5":
            if len(completed_task_list) == 0:
                print("No completed Task")
            print("Thank you for using the To-Do List App!")                          
            break
    except ValueError:
        print("Please only input numbers.")
    except IndexError:
        print("The To-Do list is currently empty.")
    except NameError:
        print("The List is currently empty")
    except KeyError:
        print("The List is currently empty")
    else:
        print("\nOne percent better everyday.")
        
    finally:
        print("\nHere is your To-Do List:")
        for k, v in status.items():
            print(f"Task: {k} - Status: {v}")
