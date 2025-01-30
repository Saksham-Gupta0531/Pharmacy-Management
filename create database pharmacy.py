
import mysql.connector as sql
"""mysql.connector ~ python module"""

def connect(command):
    """This function makes connectivity of python with Mysql."""
    
    connection =sql.connect(host="localhost",user="root",
                passwd="root",database="pharmacy")
    cursor=connection.cursor(buffered=True)
    cursor.execute(command)
    connection.commit()
    cursor.close()
    return cursor,connection
def create_db():
    command="create database pharmacy;"
    connect(command)
    command="use pharmacy000;"
    connect(command)
    command="create table customer(c_id int primary key auto_increment,c_name varchar(40),phone varchar(13));"
    connect(command)

    command="create table pharmacy.product(p_id int primary key auto_increment,p_name varchar(40),price int,company varchar(13),quantity int);"
    connect(command)
    command="create table pharmacy.transaction(t_id int primary key auto_increment,  c_id int, p_id int, foreign key (c_id) references customer(c_id) on delete set null, foreign key (p_id) references product(p_id) on delete set null,quantity int,total_amount int  );"
    connect(command)
create_db()    

             


def create_record_auto():
    connection=mysql.connect(host="localhost",user="root",passwd="7324",database="bank_db")
    cursor=connection.cursor(buffered=True)
    l=[[676565465, 'sanjay', 66544.0, 'Savings', 'avas vikas', '7876555564'],
               [75576565, 'akshay', 8057.0, 'Current', 'sita road', '7865473544'],
               [75675668978, 'amit sharma', 65678.0, 'Current', 'ganesh colony', '7819856158'],
               [6657567686, 'alok varshney', 55967.0, 'Savings', 'bharam bazar', '9368674455'],
               [6846875676, 'anand varshney', 315.0, 'Current', 'sita road', '7819828456'],
               [846764855, 'rohan arora', 4900.0, 'Current', 'gopal street', '7819856234']]
    for i in range(6):
        retreive = "insert into customer(ACCOUNT_NO,CUSTOMER_NAME,BALANCE,ACCOUNT_TYPE,ADDRESS,PHONE_NO) values('{}','{}','{}','{}','{}','{}')".format(l[i][0],l[i][1],l[i][2],l[i][3],l[i][4],l[i][5])
        cursor.esxecute(retreive)
        connection.commit()
        retreive="select * from bank_record"
        cursor.execute(retreive)
        data=cursor.fetchall()
        sr=data[-1][0]
        retreive = " insert into transaction(sr,trans_type,trans_date) values({},'Create',curdate())".format(sr)
        cursor.execute(retreive)
        connection.commit()
    
    connection.close()
    print("/")
create_record_auto()

