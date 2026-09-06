welcome_msg = "Welcome to the shopping list."
print(welcome_msg)
shopping_list = []

while True:
    option_choice = input("What do you want to do?\n 1. Add item\n 2. Show the list\n 3. Remove item from the list\n 4. Exit the list ")
    if option_choice == "1":
        item = input("What item do you want to add? ").lower()
        if item in shopping_list:
            print("Item is already in the list")
        else:
            shopping_list.append(item)
            print(f"{item} has been added to the list.")
    elif option_choice == "2":
        if shopping_list:
            for nr, product in enumerate(shopping_list, 1):
                print(nr, product)
        else:
            print("List is empty")
    elif option_choice == "3":
        if shopping_list:
            try:
                nr_del = int(input("Give item number to remove from the list "))
                no_of_items = len(shopping_list)
                if 1 <= nr_del <= no_of_items:
                    nr_del -=1
                    rmv_item = shopping_list[nr_del]
                    del shopping_list[nr_del]
                    print(f"Item '{rmv_item}' removed from the list.")
                else:
                    print("List is not that long")
            except:
                print("You must give a number")
        else:
            print("List is empty")
            
    elif option_choice == "4":
        break
    else:
        print("There is no such option ")
