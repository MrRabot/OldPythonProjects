import pymysql as sql
import datetime

con = sql.connect(host="localhost", user="root", password="root", database="bank")
cur = con.cursor()

print("Bank Management System...\n")


def newacc():
    print('''     New Customer Account
    ----------------------''')
    temp = input("    Press enter to continue. Else enter space to go back.\n")
    if temp == "":
        try:
            accno = int(input("Enter Account Number: "))
            cur.execute(f"select * from customer where Account_no = {accno}")
            flag = cur.fetchone()
            if flag == None:
                name = input("Enter Name: ").strip().capitalize()
                gend = input("Enter Gender(Male/Female/Trans): ").strip().capitalize()
                email = input("Enter Email: ").strip()
                phone = int(input("Enter Phone Number: "))
                acctype = input("Enter Account type(Savings/Current/Fixed): ").strip().capitalize()
                bal = int(input("Enter Initial Balance Deposit: "))
                stat = 1
                qry = f"insert into customer values({accno},'{name}','{gend}','{email}',{phone},'{acctype}',{bal},{stat})"
                cur.execute(qry)
                input("Account Created Successfully.")
            else:
                print("Error!! Account No already exits! Please try a different Account No.")
                input()
                newacc()
        except ValueError:
            print("Invalid Entry!!")
            newacc()
        con.commit()


def deposit():
    print('''     Money Deposit
    ---------------''')
    temp = input("    Press enter to continue. Else enter space to go back.\n")
    if temp == "":
        try:
            accno = int(input("Enter Account Number: "))
        except ValueError:
            print("Invalid Entry!!")
            deposit()
        cur.execute(f"select * from customer where Account_no = {accno}")
        flag = cur.fetchone()
        if flag == None:
            input("No Valid Account Found!! Account Number Does not Exist!!")
        elif flag[7] == 0:
            input("The current account is not active. Please activate Account first to deposit.")
        else:
            try:
                dep = int(input("Enter the amount to be deposited: "))
                cur.execute(f"select Balance from customer where Account_no={accno}")
                bal = cur.fetchone()
                amt = int(bal[0])
                amt += dep
                cur.execute(f"update customer set Balance = {amt} where Account_no = {accno}")
                cur.execute(f"insert into transaction values({accno}, 'Deposit', '{datetime.datetime.now()}', {dep})")
                con.commit()
                input(f"   Your Current Balance is {amt}.")
            except ValueError:
                print("Invalid Entry!!")
                deposit()


def withdraw():
    print('''     Money Withdrawal
    ------------------''')
    temp = input("    Press enter to continue. Else enter space to go back.\n")
    if temp == "":
        try:
            accno = int(input("Enter Account Number: "))
        except ValueError:
            print("Invalid Entry!!")
            withdraw()
        cur.execute(f"select * from customer where Account_no = {accno}")
        flag = cur.fetchone()
        if flag == None:
            print("No Valid Account Found!! Account Number Does not Exist!!")
            withdraw()
        elif flag[7] == 0:
            print("The current account is not active. Please activate Account first to withdraw.")
        else:
            try:
                wamt = int(input("Enter the amount to be withdrawn: "))
                cur.execute(f"select Balance from customer where Account_no={accno}")
                bal = cur.fetchone()
                amt = int(bal[0])
                if amt <= wamt:
                    print("Insufficient balance!! Please Enter a valid amount!")
                    input(f"   Your Current Balance is {amt}.")
                else:
                    amt -= wamt
                    cur.execute(f"update customer set Balance = {amt} where Account_no = {accno}")
                    cur.execute(f"insert into transaction values({accno},'Withdraw','{datetime.datetime.now()}', {wamt})")
                    con.commit()
                    input(f"   Your Current Balance is {amt}.")
            except ValueError:
                print("Invalid Entry!!")
                withdraw()


def balenqry():
    print('''     Balance Enquiry
    -----------------''')
    temp = input("    Press enter to continue. Else enter space to go back.\n")
    if temp == "":
        try:
            accno = int(input("Enter Account Number: "))
        except ValueError:
            print("Invalid Entry!!")
            balenqry()
        cur.execute(f"select * from customer where Account_no = {accno}")
        flag = cur.fetchone()
        if flag == None:
            print("No Valid Account Found!! Account Number Does not Exist!!")
            balenqry()
        elif flag[7] == 0:
            print("The current account is not active. Please activate Account first.")
        else:
            cur.execute(f"select Balance from customer where Account_no={accno}")
            bal = cur.fetchone()
            amt = int(bal[0])
            print(f"Your Current Balance is {amt}.")
    input()


def viewall():
    print('''    View All Accounts ?''')
    temp = input("    Press enter to continue. Else enter space to go back.\n")
    if temp == "":
        cur.execute("select * from customer")
        data = cur.fetchall()
        print("| %11s| %33s| %7s| %30s| %13s| %8s| %8s| %6s|" % ("Account_no", "Name", "Gender", "Email", "Number", "Acc_Type", "Balance", "Active"))
        print("_" * 133)
        for i in data:
            print("| %11d| %33s| %7s| %30s| %13d| %8s| %8d| %6d|" % (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
    input()


def accedit():
    print('''     Account Edit
    --------------''')
    temp = input("    Press enter to continue. Else enter space to go back.\n")
    if temp == "":
        try:
            accno = int(input("Enter Account Number: "))
        except ValueError:
            print("Invalid Entry!!")
            accedit()
        cur.execute(f"select * from customer where Account_no = {accno}")
        flag = cur.fetchone()
        if flag == None:
            print("No Valid Account Found!! Account Number Does not Exist!!")
            accedit()
        else:
            def edit():
                print('''Enter
                1. to Change Name
                2. Change Gender
                3. Change Email
                4. Change Number
                5. Change Account Type
                6. Change Account Status
                ''')
                opt = int(input("Input: "))


                if opt == 1:
                    name = input("Enter Name: ")
                    cur.execute(f"update customer set Name= '{name}' where Account_no= {accno}")
                elif opt == 2:
                    gender = input("Enter Gender: ")
                    cur.execute(f"update customer set Gender= '{gender}' where Account_no= {accno}")
                elif opt == 3:
                    email = input("Enter Email: ")
                    cur.execute(f"update customer set Email= '{email}' where Account_no= {accno}")
                elif opt == 4:
                    number = int(input("Enter Number: "))
                    cur.execute(f"update customer set Phone= {number} where Account_no= {accno}")
                elif opt == 5:
                    type = input("Enter Account Type: ")
                    cur.execute(f"update customer set Acc_Type= '{type}' where Account_no= {accno}")
                elif opt == 6:
                    act = input("Set Account Status(1 for active/0 for inactive): ")
                    if act == "0":
                        stat = False
                    else:
                        stat= True
                    cur.execute(f"update customer set Active= {stat} where Account_no= {accno}")
                else:
                    input("Invalid Entry!!")
                    edit()
                opt2 = input("Are you sure you want to save your changes?(Y/N): ").upper()

                if opt2 == "Y":
                    con.commit()
                elif opt2 == "N":
                    accedit()
                else:
                    print("Invalid Entry!!")
                    edit()
            edit()

def trans():
    cur.execute(f"select * from transaction order by date desc limit 5")
    data = cur.fetchall()
    print("| %11s| %8s| %19s| %9s|" % ("Account_no", "T_Type","Date","Amount"))
    print("_"*56)
    for i in data:
        print("| %11d| %8s| %19s| %9d|"%(i[0], i[1], i[2], i[3]))
    input()

def close():
    print('''     Account Deactivate
    --------------------''')
    temp = input("    Press enter to continue. Else enter space to go back.\n")
    if temp == "":
        try:
            accno = int(input("Enter Account Number: "))
        except ValueError:
            print("Invalid Entry!!")
            accedit()
        cur.execute(f"select * from customer where Account_no = {accno}")
        flag = cur.fetchone()
        if flag == None:
            print("No Valid Account Found!! Account Number Does not Exist!!")
            accedit()
        else:
            cur.execute(f"update customer set active = {False} where Account_no= {accno}")

        opt = input(f"Are you sure you want to Deactivate this Account:{accno} ?(Y/N): ").strip().upper()
        if opt == "Y":
            con.commit()
        input("Account Deactivated!!")





while True:
    print()
    print('''     Main Menu
    -----------
    1. Create New Account

    2. Deposit Amount

    3. Withdraw Amount

    4. Balance Enquiry

    5. View All Accounts

    6. Modify An Account

    7. Mini Statement

    8. Close An Account

    9. Exit
    ''')
    optn = 9


    def optnin():
        global optn
        try:
            optn = int(input("Input: "))
        except ValueError:
            print("Invalid Entry!!")
            optnin()


    optnin()

    if optn == 1:
        newacc()
    elif optn == 2:
        deposit()
    elif optn == 3:
        withdraw()
    elif optn == 4:
        balenqry()
    elif optn == 5:
        viewall()
    elif optn == 6:
        accedit()
    elif optn == 7:
        trans()
    elif optn == 8:
        close()
    elif optn == 9:
        con.close()
        exit(0)
    else:
        print("Invalid Option!!")
        optnin()
