print("==Welcome to the contact book==")
contacts = {}

def add_contact(name, phone_nr):
    while True:
        contact_name = input(name)
        if contact_name == "":
            print("You must give a name")
        else:
            if contact_name in contacts:
                duplicate_name = input("Contact with that name already exists.\nChoose 1 to add another name\n Choose any key to return to the menu ")
                if duplicate_name == "1":
                    continue
                else:
                    break
            else: 
                while True:
                    contact_phone = input(phone_nr)
                    if contact_phone.isdigit():
                        print("Contact "+contact_name + " added to the contact list")
                        contacts[contact_name] = contact_phone
                        return
                    else:
                        print("Number must contain only digits")

def show_contacts():
    if contacts:
        for key, value in contacts.items():
            print(key, ": ", value)
    else:
        print("Contact list is empty")                  

def find_contact(name):
    contact_name = input(name)
    if contact_name in contacts:
        print(contact_name, contacts[contact_name])
    else:
        print("Contact "+ contact_name + " not found")

def delete_contact(name):
    contact_name = input(name)
    if contact_name in contacts:
        print("Contact "+contact_name+ " removed from the contact list")
        del contacts[contact_name]
    else:
        print("Contact "+contact_name+ " not found")
        

while True:
    menu = input("What would you like to do\n 1. Add new contact\n 2. Show all contacts\n 3. Find contact\n 4. Delete contact\n 5. Exit ")
    if menu == "1":
        add_contact("Give name ", "Give number ")
    elif menu == "2":
        show_contacts()
    elif menu == "3":
        find_contact("Input contact name ")
    elif menu == "4":
        delete_contact("Input contact name ")
    elif menu =="5":
        print("Leaving contact book")
        break
    else:
        print("Choose one of the available options: 1-5")
