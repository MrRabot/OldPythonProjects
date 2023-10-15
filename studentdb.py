import ast

print("Student Data Management System...\n")


def insert():
    try:
        file = open("Student_data.txt", "r")
        str1 = file.read()
        dict1 = ast.literal_eval(str1)
        file.close()

        def entry():
            ID = int(input("Enter Student ID: "))
            if ID in dict1:
                swth = input(
                    "The given ID already Exists!!. Are you sure you want to change the details of this ID?(Y/N): ").upper()
                if swth == "Y":
                    pass
                elif swth == "N":
                    entry()
                else:
                    print("Invalid input!!")
                    entry()
            name = input("Enter Student Name: ")
            email = input("Enter Student Email: ")
            number = int(input("Enter Student Number: "))
            branch = input("Enter Student Branch: ")
            dict1.update({ID: [name, email, number, branch]})

            def exit_entry():
                try:
                    opt = int(
                        input('''\nEnter:\n    1- to Add another Record.\n    2- Go to the Main Menu.\nInput: '''))
                except ValueError:
                    print("Invalid Value!!")
                    exit_entry()

                if opt == 1:
                    entry()
                elif opt == 2:
                    pass
                else:
                    print("Invalid Input!!")
                    exit_entry()

            exit_entry()

        entry()

        str2 = str(dict1)
        file = open("Student_data.txt", "w")
        file.write(str2)
        file.close()

    except FileNotFoundError:
        file = open("Student_data.txt", "w")
        file.write('{}')
        file.close()
        insert()


def display():
    try:
        file = open("Student_data.txt", "r")
        s1 = file.read()
        dict1 = ast.literal_eval(s1)
        file.close()
        print("%9s | %25s | %20s | %10s | %3s" % ("ID", "Name", "Email", "Number", "Branch"))
        print("-" * 80)
        for i in dict1:
            rec = dict1[i]
            print("%9d | %25s | %20s | %10d | %3s" % (i, rec[0], rec[1], rec[2], rec[3]))
    except FileNotFoundError:
        file = open("Student_data.txt", "w")
        file.write('{}')
        file.close()
        display()

def search():
    try:
        file = open("Student_data.txt", "r")
        s1 = file.read()
        dict1 = ast.literal_eval(s1)
        file.close()
        opt = int(input('''\nSearch:\n    1- Search By ID.\n    2- Search By Name.\n    3- Main Menu.\n\nInput: '''))
        if opt == 1:
            try:
                ID = int(input("Enter Student ID to search: "))
            except ValueError:
                print("Invalid Entry!!")
                search()

            if ID in dict1:
                print("%9s | %25s | %20s | %10s | %3s" % ("ID", "Name", "Email", "Number", "Branch"))
                print("-" * 80)
                rec = dict1[ID]
                print("%9d | %25s | %20s | %10d | %3s" % (ID, rec[0], rec[1], rec[2], rec[3]))
            else:
                print("No match result...")
                search()
        elif opt == 2:
            try:
                name = input("Enter Name of the Student: ")
            except ValueError:
                print("Invalid Entry: ")
                search()

            s1 = name.split(" ")
            name = ""
            for i in s1:
                if i == "":
                    continue
                i = i.capitalize()
                name += " " + i
            name = name.strip()
            print(name)

            for i in dict1:
                rec = dict1[i]
                if name == rec[0]:
                    print("%9s | %25s | %20s | %10s | %3s" % ("ID", "Name", "Email", "Number", "Branch"))
                    print("-" * 80)
                    print("%9d | %25s | %20s | %10d | %3s" % (i, rec[0], rec[1], rec[2], rec[3]))
                    search()
            print("No matching result...")
        elif opt == 3:
            pass
        else:
            print("Invalid Input!!")
            search()
    except FileNotFoundError:
        file = open("Student_data.txt", "w")
        file.write('{}')
        file.close()
        search()


def delete():
    try:
        file = open("Student_data.txt", "r")
        s1 = file.read()
        dict1 = ast.literal_eval(s1)
        file.close()
        try:
            ID = int(input("Enter Student ID to Delete: "))
        except ValueError:
            print("Invalid Entry!!")
            delete()

        if ID in dict1:
            print("%9s | %25s | %20s | %10s | %3s" % ("ID", "Name", "Email", "Number", "Branch"))
            print("-" * 80)
            rec = dict1[ID]
            print("%9d | %25s | %20s | %10d | %3s" % (ID, rec[0], rec[1], rec[2], rec[3]))
            choice = input("\n!Are you sure you want to Delete this record?(Y/N): ").upper()
            if choice == "Y":
                del dict1[ID]
                print("Record Deleted!.")
                str2 = str(dict1)

                file = open("Student_data.txt", "w")

                file.write(str2)

                file.close()
            elif choice == "N":
                pass
            else:
                print("Invalid Input!!")
                delete()

        else:
            print("No match result...")
            delete()
    except FileNotFoundError:
        file = open("Student_data.txt", "w")
        file.write('{}')
        file.close()
        delete()


while True:
    print()
    optn = int(input('''Enter -
          1 - to add New Student Record
          2 - Display All Records
          3 - Search for Student Record
          4 - Delete a Record
          5 - Exit\n\nInput: '''))
    if optn == 1:
        insert()
    elif optn == 2:
        display()
    elif optn == 3:
        search()
    elif optn == 4:
        delete()
    elif optn == 5:
        exit(0)
    else:
        print("Invalid input!! Please try again.\n")
