# x="new"
# y=x.upper()
# print(y)
# z=y.lower()
# print(z)


# y=10

# print(f"this is {y}th python class")


# +,-,*,%,/,\
# +=,-+,*=
# ==,>=,<=,!=
# and,or,not

# x=10
# y=20

# # print(x+y)
# print( x!=y )



# x=['car1','car2',10]
# x.append("car3")
# print(x)

# x=("car1","car2","car3","car3")
# y=list(x)
# y[1]="car3"
# y[2]="car2"
# x=tuple(y)
# print(x)
# z=set(x)
# print(z)



# d={
#     "name":"mrv",
#     "name1":"mrv"
# }
# print(d.items())

# x=int(input("enter the value for x :"))
# y=int(input("enter the value for y :"))

# if x>y:
#     print("x is greater")
# elif x<y:
#     print("x is less then y")
# else:
#     print("this is else")
# count = 1
# while x>y:
#     print("this is correct" ,count)
#     count +=1
#     if count==10:
#         break

# for i in range(1,10):
#     print("the value is ",i)

# def myfun():
#     print("this is myfun")

# x=int(input("enter the value to invoke the function :"))
# if x==9:
#     myfun()

    
# def myfun(a,b):
#     print("the value is :",a + b)

# x=int(input('enter x value: '))
# y=int(input('enter y value: '))

# myfun(x,y)

# x=10
# def myfun():
#     y=20
#     print("x value is:",x)
#     print("y value is:",y)

# myfun()
# print("x value is:",x)
# print("y value is:",y)

# x=[]
# x.append("car")
# print(x)

# class HelloWorld():
#    x=5
        
    
# y=HelloWorld()
# print(y.x)
# z=HelloWorld()
# print(z.x)

# class Python():
#     def __init__(self,x,y):
#         self.name=x
#         self.phone=y
#     def myfun(self):
#         print("welcome to ",self.name)
# o=Python("mrv",8787)

# print(o.name)
# print(o.phone)
# o.myfun()
# o1=Python("it",67676)
# print(o1.name)
# print(o1.phone)

# import mod

# mod.myfun(6,7)

# try:
#     print(x)
# except:
#     print("an error occured")
# x=10
# print(x)


# x=10

# print(f"this is {x}th value")

# import random

# start = int(input("enter the starting value :"))
# end = int(input("enter the ending value :"))

# while start >= end:
#     print("please enter the values from low to high")
#     start = int(input("enter the starting value :"))
#     end = int(input("enter the ending value :"))

# genrandom= random.randint(start,end)

# print(f'guess the number between {start } and {end} ,you have 5 attempts left')
# attempts=5

# while attempts >0:
#     guess = int(input("enter the guess: "))
#     attempts -=1
#     if guess < genrandom:
#         print(f"your guessed value is less than generated value.{attempts} attempts left")
#     elif guess > genrandom:
#         print(f"your guessed value is more than generated value.{attempts} attempts left")
#     else:
#         print("congratulation you found the number")
#         break

# else:
#     print(f"out of attempts the generated number is - {genrandom},try agian")
           

# x=str(input("enter the value :"))
# str(x)
# y=x[::-1]
# if x==y:
#     print("it is an palidrome")
# else:
#     print("it is not an palidrome")
# Get user input
# num = int(input("Enter a number: "))

# # Check if the number is prime
# if num <= 1:
#     print(f"{num} is not a prime number.")
# elif num == 2:
#     print(f"{num} is a prime number.")
# elif num % 2 == 0:
#     print(f"{num} is not a prime number.")
# else:
#     is_prime = True
#     for i in range(3, int(num**0.5) + 1,2):
#         if num % i == 0:
#             print(f"{num} is not a prime number.")
#             break
#         else:
#             print("it is prime number")
    
# x=open("create.txt",'w')  
# x.write("hello welcome to flask class")
# x.close()
# x=open("create.txt")  
# print(x.read())
# print(x.read())    
# x=open("create.txt",'x')

# import psycopg2
# from psycopg2 import sql

# DB_HOST='localhost'
# DB_PORT='5432'
# DB_NAME='postgres'
# DB_USER='postgres'
# DB_PASSWORD='Abhi@2001'

# def connect():
#     try:
#         connection=psycopg2.connect(
#             host=DB_HOST,
#             port=DB_PORT,
#             database=DB_NAME,
#             user=DB_USER,
#             password=DB_PASSWORD
#         )
#         return connection
#     except Exception as e:
#         print(f"error connecting:{e}")
#         return Home

# def fetch():
#     connection=connect()
#     if connection is None:
#         return
#     cursor = connection.cursor()
#     val=(3,'python','class')
#     cursor.execute("insert into python (id,user1,pass1) values(%s,%s,%s)",val)
#     connection.commit()
#     cursor.close()
#     connection.close()

# fetch()
    
# def fetchbyid(id):
#     connection=connect()
#     if connection is None:
#         return
#     cursor = connection.cursor()
#     cursor.execute('select * from python where id=%s',(id,))
#     res=cursor.fetchone()
#     print(res)
#     cursor.close()
#     connection.close()

# fetchbyid(2)

import tkinter as tk
from tkinter import messagebox

# def myfun():
#     name = entername.get()
#     password=enterpass.get()
#     print(f"name : {name}")
#     print(f"password :{password}")

# root = tk.Tk()
# root.title("user form")
# root.geometry("500x300")

# labelname=tk.Label(root,text="Name")
# labelname.pack(pady=5)
# entername=tk.Entry(root)
# entername.pack(pady=5)
# labelpass = tk.Label(root,text="Password")
# labelpass.pack(pady=5)
# enterpass=tk.Entry(root,show="*")
# enterpass.pack(pady=5)

# submit=tk.Button(root,text="submit", command=myfun)
# submit.pack(pady=5)
# root.mainloop()\



# x=5
# for i in range(x,0,-1):
#     print(" " * (x - i) + "*" * (2 * i -1))
# for i in range(2,x+1):
#     print(" " * (x - i) + "*" * (2 * i -1))
