print("Welcome in 'To Do List'")
print("1. Add task \n2. Show the list \n3. Mark task as completed \n4. Remove task from the list \n5. Exit list")

to_do = []
while True:
    user_pick = input("To start choose numeric value from the menu  ")
    if user_pick == "1":
        while True:
            new_task = input("Type new task or type 'q' to get back to the menu ")
            if new_task == "q":
                break
            else:
                to_do.append(new_task)
    elif user_pick == "2":
        if to_do:
            for nr, task in enumerate(to_do, 1):
                print(nr, task)
        else:
            print("The list is empty")
            continue
    elif user_pick =="3":
        if to_do:
            while True:
                try:
                    compl_task = int(input("Input number of task you wish to mark as completed "))
                    compl_task -=1
                    if 0 <= compl_task < len(to_do):
                        if str.startswith(to_do[compl_task], "DONE"):
                            print("Task already marked as finished")
                            break
                        else:
                            print(f"Task {to_do[compl_task]} marked as completed") 
                            to_do[compl_task] = "DONE "+to_do[compl_task]
                            break             
                    else:
                        print("There is no position with that number")
                        break
                except ValueError:
                    print("You need to give a number")
        else:
            print("The list is empty")
    elif user_pick == "4":
        if to_do:
            while True:
                try:
                    del_task = int(input("Input number of task you wish to remove from the list "))
                    del_task -= 1
                    if 0 <= del_task < len(to_do):
                        print(f"Task {to_do[del_task]} has been removed from the list")
                        del to_do[del_task]
                        break
                    else:
                        print("There is no position with that number")
                        break
                except ValueError:
                    print("You need to give a number")
        else:
            print("The list is empty")
    elif user_pick == "5":
        break
    else:
        print("Choose option 1-5")
