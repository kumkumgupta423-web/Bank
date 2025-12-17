import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="bank"
)
mycursor = mydb.cursor()
def display():
    a=input("enter accno")
    sql = "select * from account where accno='"+a+"'"
    mycursor.execute(sql)
    r=mycursor.fetchall()
    if r!=[]:
        for i in r:
            print(i[0],i[1],i[2],i[3],i[4],i[5])
    else:


        print("wrong number")


def withdraw():
   a=input("enter the accno")
   b=input("enter the balance")
   tt="withdraw" 
   d=input("Enter the date")
   sql="select balance from account where accno='"+a+"'"
   mycursor.execute(sql)
   r=mycursor.fetchall()
   x=0
   if r!=[]:
       for i in r:
          x=i[0]
       if x>=int(b):
         x=int(x)-int(b)
         sql1="update account set balance = '"+str(x)+"' where accno ='"+a+"'"
         mycursor.execute(sql1)
         mydb.commit()
         sql2="insert into trans values('"+a+"','"+b+"','"+tt+"','"+d+"')"
         mycursor.execute(sql2)
         mydb.commit()
         print("update")
       else:
           print("Insufficient amount")
           
def deposit():
   a=input("enter the accno")
   b=input("enter the balance")
   tt="deposit" 
   d=input("Enter the date")
   sql="select balance from account where accno='"+a+"'"
   mycursor.execute(sql)
   r=mycursor.fetchall()
   x=0
   if r!=[]:
       for i in r:
          x=i[0]
       
       x=int(x)+int(b)
       sql1="update account set balance = '"+str(x)+"' where accno ='"+a+"'"
       mycursor.execute(sql1)
       mydb.commit()
       sql2="insert into trans values('"+a+"','"+b+"','"+tt+"','"+d+"')"
       mycursor.execute(sql2)
       mydb.commit()
       print("update")
       

def insert():
    a=input("enter accno")
    n=input("enter name")
    b=input("enter balance")
    p=input("enter phone")
    ad=input("enter adsress")
    d=input("enter date")
    sql="insert into account values('"+a+"','"+n+"','"+ad+"','"+p+"','"+b+"','"+d+"')"
    mycursor.execute(sql)
    mydb.commit()
    print("update")
def displaytrans():
    a=input("enter accno")
    sql = "select * from trans where accno='"+a+"'"
    mycursor.execute(sql)
    r=mycursor.fetchall()
    if r!=[]:
        for i in r:
            print(i[0],i[1],i[2],i[3])
    else:
      print("wrong")
      
ch='y'
while ch=='y':
  print("Insert     1")
  print("display    2")
  print("deposit    3")
  print("Withdraw 4")
  print("displaytrans 5")
  p=int(input("Enter the choice"))
  if p==1:
     insert()
  elif p==2:
    display()
  elif p==3:
     deposit()
  elif p==4:
      withdraw()
  elif p==5:
      displaytrans()
  else:
    print("Wrong choice")
  ch=input("Press y to continue")
