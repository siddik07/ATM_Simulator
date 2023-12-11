import sqlite3
import time
import datetime
import random as r

conn=sqlite3.connect('ATM.db')
c=conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT,accno VARCHAR(20),pins TEXT,balance REAL);")
conn.commit()

today=datetime.datetime.now()

def create_ac():
    name=input("\t\t\t\tEnter Your Name for Account:\n\n\t\t\t\t")
    print("\t\t\t\t****************************")
    name=name.upper()
    accno=r.randint(2673875105,7464301237)
    pins=input("\t\t\t\tSet  PIN for Your Account:\n\n\t\t\t\t")
    print("\t\t\t\t*******************************")
    balance=int(input("\t\t\t\tEnter Amount To Deposit :\n\n\t\t\t\t"))
    print("\t\t\t\t****************************************")
    c.execute("INSERT INTO accounts  VALUES (?,?,?,?) ",(name,accno,pins,balance))
    print("\t\t\t\tAccount created Succcessfully ")
    print("\t\t\t\t************************** ")
    conn.commit()
    print(f'''
                   Name:{name}
                   Account_No:{accno}
                   Amount:{balance}
                ''')
    
def  login():
    c.execute("SELECT * FROM accounts WHERE  name=? AND pins= ? ",(name,pins))
    account=c.fetchone()
    if account:
        return account
    else:
        print("\t\t\t\t*****************************")
        print("\t\t\t\tINVALID")
        return None
    
def withdraw(account):
    global pins
    print("\t\t\t\t***************************************")
    amount=float(input("\t\t\t\tEnter Amount To Withdraw:\n\n\t\t\t\t"))
    if amount <= account[3]:
        new_bal=account[3]-amount
        c.execute("SELECT * FROM accounts")
        c.execute("UPDATE accounts SET balance=? WHERE pins= ? ",(new_bal,pins))
        conn.commit()
        print("\t\t\t\t************************************")
        print("\t\t\t\tPlease wait,your transaction is processed")
        time.sleep(3.5)
        print("\t\t\t\t************************************")
        print("\t\t\t\tYour Transaction is completed")
        print("\t\t\t\t************************************")
        print(f''''\t\t
                        RECEIPT
        ----------------------------------------------
        Name:{name}
        Account_no:{account[1]}
        Withdraw_Amount:{amount}
        Balance:{new_bal}
        DateTime:{today}
        ----------------------------------------------
        ''')      
    else:
        time.sleep(2)
        print("\t\t\t\t*********************************")
        print("\t\t\t\tInsufficient Balance!!!! \n\t\t\t\tPlease Check Your Account")

def deposit(account):
    global pins
    print("\t\t\t\t***********************************")
    amount=int(input("\t\t\t\tEnter Amount To Deposit:\n\n\t\t\t\t"))
    new_bal=account[3]+amount
    c.execute("SELECT * FROM accounts")
    c.execute("UPDATE accounts SET balance=? WHERE pins= ? ",(new_bal,pins))
    conn.commit()
    print("\t\t\t\t************************************")
    print("\t\t\t\tPlease wait,your transaction is processed")
    time.sleep(3.5)
    print("\t\t\t\t****************************")
    print("\t\t\t\tYour Transaction is completed")
    print("\t\t\t\t**************************")
    print(f'''
                     RECEIPT
    ----------------------------------------------
    Name:{name}
    Account_no:{account[1]}
    Deposit_Amount:{amount}
    Balance:{new_bal}
    DateTime:{today}
    ----------------------------------------------
        ''')

def check_balance(account):
    print("\t\t\t\t**********************************")
    print("\t\t\t\tPlease wait,your transaction is processed")
    time.sleep(2)
    print("\t\t\t\t*****************************")
    print("\t\t\t\tYour Transaction is completed")
    print("\t\t\t\t*****************************")
    c.execute("SELECT * FROM accounts WHERE name=? AND pins= ? ",(name,pins))
    print(f'''
                     RECEIPT
    ----------------------------------------------
    Name:{name}
    Account_no:{account[1]}
    Balance:{account[3]}
    DateTime:{today}
    ----------------------------------------------
        ''')    
    conn.commit()
    
def pin_change(acccount):
    print("\t\t\t\t************************")
    p=input("\t\t\t\tEnter Your New PIN:\n\n\t\t\t\t")
    print("\t\t\t\t*************************")
    np=input("\t\t\t\tConfirm Your New PIN:\n\n\t\t\t\t")
    if p==np:
        time.sleep(2)
        c.execute("UPDATE accounts SET pins=? WHERE pins= ? ",(np,pins))
        print("\t\t\t\t******************************")
        print("\t\t\t\tYour PIN was Successfully Changed")
        conn.commit()
    else:
        print("\t\t\t\t***********************")
        print("\t\t\t\tPlease Enter Valid PIN!!")
    print("\t\t\t\t************************")
    print("\t\t\t\tThank You For Using ATM")

#mainfunction
    
print("\t\t\t\tWELCOME   TO ATM")
print("\t\t\t\t*********************")
choice=int(input("\nPress 0 for login  OR Press 1 for Register Account:"))
print("\n\t\t\t\t***************")
if choice==0:
    name=input("\t\t\t\tEnter User Name:\n\n\t\t\t\t")
    print("\t\t\t\t***********************")
    name=name.upper()
    pins=input("\t\t\t\tEnter Your PIN:\n\n\t\t\t\t")
    print("\t\t\t\t*********************")
    while True:
        account=login()
        if account:
                     print(f"WELCOME   {name}")
                     print("********************")
                     print(''' SELECT FROM THE FOLLOWING OPTOINS: \n \t\t\t\t\t1.WITHDRAW \n \t\t\t\t\t2.DEPOSIT \n \t\t\t\t\t3.BALANCE CHECK \n \t\t\t\t\t4.PIN CHANGE \n \t\t\t\t\t5.EXIT ''')
                     print("\t\t\t\t*************************")
                     choice=int(input("\t\t\t\tEnter Your Choice:"))
                     if choice==1:
                            withdraw(account)
                     elif choice==2:
                            deposit(account)
                     elif choice==3:
                            check_balance(account)
                     elif choice==4:
                            pin_change(account)
                     elif choice==5:
                            print("\t\t\t\tThank you for using ATM")
                            break
                     else:
                            print("\t\t\t\tInvalid choice!!!!")
                            print("\t\t\t\tDo You Want To Continue")
                     print("\t\t\t\t*****************************")
                     cont=int(input("\t\t\t\tPress 0 for Continue OR Press 1 for Exit:"))
                     if cont==0:
                            continue
                     else:

                            print("\t\t\t\t*****************************")
                            print("\t\t\t\tThank You For Using ATM ")
                            break

        else:
                print("\t\t\t\t*****************************")
                print("\t\t\t\tGood bye!!!")
                break
else:
            create_ac()

time.sleep(3)

conn.close()

            

    





