import mysql.connector as sql
import time
"""mysql.connector ~ python module"""

def connect(command):
    """This function makes connectivity of python with Mysql."""
    
    connection =sql.connect(host="localhost",user="root",passwd="0531",database="pharmacy")
    cursor=connection.cursor(buffered=True)
    cursor.execute(command)
    return cursor,connection

def execute_ddl(command):
    """This function executes writing type queries"""
    
    cursor,connection=connect(command)
    try:
        connection.commit()
    except Exception:
        pass
    connection.close()
    
def execute_dml(command,x=1):
    
    
    cursor,connection=connect(command)
    if cursor!=None:
        if x==1:
            rec=cursor.fetchall()
        elif x==2:
            
            rec=cursor.fetchone()
        temp=[]
        try:
            for i in rec:
                for j in i:
                 temp.append(j)
            rec=temp
        except Exception:
            rec=rec[0]
    else:
        print("⚠connection failed⚠")
    connection.close()
    return rec


def add_data(ch):
    if ch=="1":                                                 
        name=input( "enter customers name:")
        command="select c_name from customer;"
        rec=execute_dml(command)
        if name in rec :
            print("Alerady exists!! \n ⚠️Are you sure to use same name again ⚠️\n⏩press 0 rewrite name \n⏩press  any other key to to continue")
            check=int(input())
            if check==0 :
               add_data(ch)
            
        else:
            phone=input ("📞 enter a 10 digit valid Phone no. 📞")
            command="insert into customer (c_name,phone) values('{}','{}');".format(name,phone)
            execute_ddl(command)
            print("RECORD ADDED✔️")
    elif ch=="2":                                         
        name=input( "enter product name:")
        command="select p_name from product;"
        rec=execute_dml(command)
        quantity=int(input("enter quantity of "+name+":"))
        if name in rec:
            command="update product set qunantity=qunantity+{};".format(quantity)
        else:
            cmpny=input("enter "+name+" company:")
            price=int(input("enter per peice price of product:"))
        command=" insert into product (p_name,price,company,quantity) values('{}','{}','{}','{}');".format(name,price,cmpny,quantity)
        execute_ddl(command)
        print("RECORD ADDED✔️")
    menu()
        

def update(ch):
    if ch=="3":
        command="select c_name,c_id from customer;"
        rec=execute_dml(command)
        print("CUSTOMERS \nID  NAME")
        for i in range(1,len(rec)+1):
            if i%2==0:
                print(rec[i-1]," ",rec[i-2]," ")
        c_name=input("enter customer name:")
        command="select c_name from customer;"
        rec=execute_dml(command)
        if c_name in rec:
            print("⏩Press 1 to modify Name\n⏩Press 2 to chnage Phone no. ")
            cho=int(input())
            c_id=int(input("enter customer id:"))
            if cho==1:
                new_name=input("enter new name:")
                command=" UPDATE CUSTOMER SET C_NAME='{}'where c_id={};".format(new_name,c_id)
                execute_ddl(command)
                print (" "*30 ,"UPATE SUCESSFUL✔️")
            elif cho==2:
                phone=input("enter new phone:")
                command="update customer set phone='{}' where c_id='{}' and c_name='{}';".format(phone,c_id,c_name)
                execute_ddl(command)
                print (" "*30,"UPATE SUCESSFUL✔\n️")
            else :
                print("⚠WRONG CHOICE⚠")
        else:
            print("NO CUSTOMER FOUND")
    
    elif ch=="4":
        command="select p_name,p_id from product;"
        rec=execute_dml(command)
        print("PRODUCTS \nID  NAME")
        for i in range(1,len(rec)+1):
            if i%2==0:
                print(rec[i-1]," ",rec[i-2]," ")
        p_name=input("enter product name:")
        command="select p_name from product;"
        rec=execute_dml(command)
        if p_name in rec:
            print("⏩Press 1 to modify Name of medicine\n⏩Press 2 to chnange company name\n⏩Press 3 to update price of medicine")
            cho=input()
            p_id=int(input("Enter product id:"))
            if cho=="1":
                new_name=input("enter name edited to be:")
                command="update product set p_name='{}' where p_id='{}' and p_name='{}';".format(new_name,p_id,p_name)
                execute_ddl(command)
                print (" "*30 ,"UPATE SUCESSFUL✔️")
            elif cho=="2":
                company=input("enter company name:")
                command="update product set company='{}' where p_id='{}' and p_name='{}';".format(company,p_id,p_name)
                execute_ddl(command)
                print (" "*30 ,"UPATE SUCESSFUL✔️")
            elif cho=="3":
                price=input("enter new price of medicin:")
                command="update product set price={} where p_id='{}' and p_name='{}';".format(price,p_id,p_name)
                execute_ddl(command)
                print (" "*30 ,"UPATE SUCESSFUL✔️")
            else:
                print("⚠WRONG CHOICE⚠")

        else:
            print("⚠NO MEDICINE FOUND⚠")
    menu()

    
def delete(ch):
    if ch=="5":
        command="select c_name,c_id from customer;"
        rec=execute_dml(command)
        print("CUSTOMERS \nID  NAME")
        for i in range(1,len(rec)+1):
            if i%2==0:
                print(rec[i-1]," ",rec[i-2]," ")
        c_id=int(input("Enter customer's id:"))
        print("☠️ Are you sure to delete this record ☠\n⏩Press 1 to Delete \n⏩Press any key to cancel️")
        cho=input()
        if cho=="1":
            command="delete from customer where c_id='{}';".format(c_id)    
            execute_ddl(command)
            print("Deletion Successful✔")
        else:
            print("✖Delition cancelled✖️")
    if ch=="6":
        command="select p_name,p_id from product;"
        rec=execute_dml(command)
        print("PRODUCTS \nID  NAME")
        for i in range(1,len(rec)+1):
            if i%2==0:
                print(rec[i-1]," ",rec[i-2]," ")
        p_id=int(input("Enter product's id:"))
        print("☠️ Are you sure to delete this record ☠\n⏩Press 1 to Delete \n⏩Press any key to cancel️")
        cho=input()
        if cho=="1":
            command="delete from product where p_id={};".format(p_id)    
            execute_ddl(command)
            print("Deletion Successful✔")
        else:
            print("✖Delition cancelled✖️")
    if ch=="7":
        command="select total_amount,t_id from transaction;"
        rec=execute_dml(command)
        print("TRANSACTION \nID  AMOUNT")
        for i in range(1,len(rec)+1):
            if i%2==0:
                print(rec[i-1],"  ₹",rec[i-2]," ")
        t_id=int(input("Enter transaction id:"))
        print("☠️ Are you sure to delete this transaction ☠\n⏩Press 1 to Delete \n⏩Press any key to cancel️")
        cho=input()
        if cho=="1":
            command="delete from transaction where t_id='{}';".format(t_id)    
            execute_ddl(command)
            print("Deletion Successful✔")
        else:
            print("✖Delition cancelled✖️")
    menu()

    
def transaction(cust):
    command="select c_name from customer;"
    rec=execute_dml(command)
    if cust in rec:
        command="select p_name,p_id from product;"
        rec=execute_dml(command)
        print("PRODUCTS \nID  NAME")
        for i in range(1,len(rec)+1):
            if i%2==0:
                print(rec[i-1]," ",rec[i-2]," ")
        product=input("Enter your product name:")
        if product in rec:
            quantity =int(input("enter qunatity:"))
            command="select quantity from product where p_name='{}';".format(product)
            check_qty=execute_dml(command,2)
            if check_qty>=quantity :
                command="insert into transaction(c_id,p_id,quantity,total_amount) select c_id,p_id,{},product.price*{} from product,customer where product.p_name='{}' and customer.c_name='{}';".format(quantity,quantity,product,cust)
                execute_ddl(command)
                command="update product set quantity=quantity-'{}';".format(quantity)
                execute_ddl(command)
                print("press 1 to buy more products.\npress any key to end transiction. ")
                buych=input()
                if buych=="1":
                    transaction(cust)
                else:
                    menu()
            else:
                print("OUT OF STOCK")
                
        else:
                print("product not found" )
    else:
        print("customer not found")
    menu()


def show():
    print("⏩Press 1 to see the information of a medicine")
    print("⏩Press 2 to see the statement of a company")
    print("⏩Press 3 to see the details of a customer")
    cho=input()
    if cho=="1":
        command="select p_name,p_id from product;"
        rec=execute_dml(command)
        print("PRODUCTS \nID  NAME")
        for i in range(1,len(rec)+1):
            if i%2==0:
                print(rec[i-1]," ",rec[i-2]," ")
        while cho!="0":
            p_id=int(input("Enter product's id:"))
            command="select p_id from product;"
            rec=execute_dml(command)
            if p_id in rec:
                command="select * from product where p_id='{}';".format(p_id)
                rec=execute_dml(command)
                for i in range(len(rec)):   
                    if i==0:
                        print("PRODUCT ID:",rec[i])
                    elif i==1:
                        print("PRODUCT NAME:",rec[i])   
                    elif i==2:
                        print("PRODUCT PRICE:",rec[i])
                    elif i==3:
                        print("PRODUCT COMPANY:",rec[i])
                    elif i==4:
                        print("PRODUCT QUANTITY:",rec[i])
                print("⏩press 0 to go to main menu\n⏩press any key to see to see more medicine")
                print("ENTER CHOICE")
                cho=input()
            else:
                print("⚠NO MEDICINE FOUND⚠")
    elif cho=="2":
        command="select distinct company from product;"
        rec=execute_dml(command)
        print("COMPANY NAME")
        for i in range(len(rec)):
                print(rec[i])
        company=input("Enter Company Name ")
        command="select distinct company from product;"
        rec=execute_dml(command)
        if company in rec:
            command="select p_id,p_name,quantity from product where company ='{}';".format(company)
            rec=execute_dml(command)
            for i in range(1,len(rec)+1):
                if i%3==0:
                     print(rec[i-1],"|")
                else:
                    print("|",rec[i-1],end="|")
        else:
            print("⚠NO COMPANY FOUND⚠")
    elif cho=="3":
        command="select c_name,c_id from customer;"
        rec=execute_dml(command)
        print("CUSTOMERS \nID  NAME")
        for i in range(1,len(rec)+1):
            if i%2==0:
                print(rec[i-1]," ",rec[i-2]," ")
        c_id=int(input("Enter customer's id:"))
        command="select c_id from customer;"
        rec=execute_dml(command)
        if c_id in rec:
            command="select * from customer where c_id='{}';".format(c_id)
            rec=execute_dml(command)
            for i in range(len(rec)):
                if i==0:
                    print("CUSTOMER ID:",rec[i])
                elif i==1:
                    print("CUSTOMER NAME:",rec[i])
                elif i==2:
                    print("CUSTOMER PHONE:",rec[i])
                
        else:
            print("⚠NO CUSTOMER FOUND⚠")
    else:
        print("⚠INVALID CHOICE⚠")
        
    
    menu()
    

    
def call():
    ch=input("🙏Please Enter A Valid Choice:")
    print(40*"-")
    if ch>="0" and ch<="9":
        if ch=="1" or ch=="2":
            add_data(ch) 
        elif ch=="3" or ch=="4":
            update(ch)
        elif ch=="5" or ch=="6" or ch=="7":
            delete(ch)
        elif ch=="8":
            command="select c_name,c_id from customer;"
            rec=execute_dml(command)
            print("CUSTOMERS \nID  NAME")
            for i in range(1,len(rec)+1):
                if i%2==0:
                    print(rec[i-1]," ",rec[i-2]," ")
            customer=input("Enter customer name")
            transaction(customer)
        elif ch=="9":
            show()
        elif ch=="0":
            print(" "*33,"🙏"*6)
            print(" "*32,"🙏THANK YOU🙏")
            print(" "*33,"🙏"*6)
        elif ch not in ["1","2","3","4","5","6","7","8","9","0"]:
            print("⚠Invalid Choice⚠")
        

def menu():
    print(" "*20,"------------------------------------------")
    print(" "*20,"                  MENU                    ")
    print(" "*20,"------------------------------------------")
    time.sleep(1)
    print(" "*20,"⭕Press 1 to: Add a new customer️       ")
    print(" "*20,"⭕Press 2 to: Add a new product️        ")
    print(" "*20,"⭕Press 3 to: Update customer's details️")
    print(" "*20,"⭕Press 4 to: Update product's details️ ")
    print(" "*20,"⭕Press 5 to: Delete customer's details️")
    print(" "*20,"⭕Press 6 to: Delete product's details️ ")
    print(" "*20,"⭕Press 7 to: Delete a transaction    ️ ")
    print(" "*20,"⭕Press 8 to: make transaxtion           ")
    print(" "*20,"⭕Press 9 to: See any data ️            ")
    print(" "*20,"⭕press 0 to: EXIT                       ")
    print(" "*20,"-----------------------------------------")
    call()
def welcome():
    print(" "*20,40*"-")
    print(" "*20,"🙇WELCOME TO PHARMACY MANAGEMENT SYSTEM🙇")
    print(" "*20,40*"-")
    print("\n\n")
    log_in()
def log_in():
    i=0
    while i<=5:
        password=input("Enter Password:")
        if password.lower()=="******":
            print("login sucessfull")
            menu()
            break
        else:
            i=i+1
            print("Incorrect Password\nTry Again")
    else:
        print("YOU HAVE TRIED 5 TIMES\nRestart Program ")

welcome()
