# # Name = input("Enter a string:-") # taking a input string
# # print(Name) # printing the string
# # print(Name[::-1]) # reversing the string 
# # print(len(Name)) # counting the no. of characters g

# # a = 10 # integer
# # b = 14.5 # float
# # c = "garima" # string
# # d = [10, 34,"hello" ] #list
# # e = (2,3,4) #tuple
# # f = True # boolean 
# # g = 4 + 3j # complex number 
# # h = {3, 4, 5} # set 
# # i = {"name": "garima", "age":19} # dictionary

# # print("this is integer number",a)
# # print("this is float number", b)
# # print("this is a string", c)
# # print("this is a list", d)
# # print("this is a tuple", e)
# # print("this is bool", f)
# # print("this is complex number", g)
# # print("this is set", h)
# # print("this is dictionary", i)

# # name = input("Enter any string:-")
# # print(name.upper())
# # print(name.lower())
# # print(len(na

# str1 = "Garima"
# str2 = "Agarwal"
# name = str1 + str2

# Students = ["Garima", "muskan", "Priya", "Swati"]
# Students.append("priyanshi")
# print(Students)

# a = 10
# b = 10.5
# c = "Hello"
# d = True
# e = [2,3,4, "hello"]
# f = (2,3,4,5,6)
# g = {4,5,6,7}
# h = {"name": "garima",
#      "class": "2nd",
#      "roll no.": 19
#      }

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)
# print(h)

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))
# print(type(h))

# a = [2,3,4,5,]
# a[2] = 10 # here we are changing the element by index from list.
# print(a) # printing new list


# tpl = (2,3,5,6)
# print(tpl)
# print(tpl[0])
# print(tpl[1])
# print(tpl[2])
# print(tpl[3])

# sat = {1,2,5,6}
# sat2 = {3,5,6}
# print(sat.union(sat2))
# print(sat.intersection(sat2))

# dict1 = {"name": "garima",
#           "year": "second year",
#           "roll no.": 19
#           }
# print(dict1)
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())

# Mini Student Management System

# Storing student details using dictionary
# student = {
#     "name": "garima",
#     "roll_no": 118,
#     "course": "B.Tech",
#     "address": "Italy",
#     "subject": ["english","maths","science","g.k","physics"]
# }

# # Storing subject marks using list
# marks = [95, 90, 88, 88, 99]

# # Calculating total marks
# total = sum(marks)

# # Calculating average marks
# average = total / len(marks)

# Displaying output
# print("===== Student Management System =====")

# print("Student Name :", student["name"])
# print("Roll Number  :", student["roll_no"])
# print("Course       :", student["course"])
# print("address      :", student["address"])
# print("subject      :", student["subject"])

# print("\nSubject Marks :", marks)

# print("Total Marks   :", total)
# print("Average Marks :", average)

#1
# number = int(input("Enter your number:-"))
# print(number)
# if number > 0:
#     print("this is positive")
# elif number < 0:
#     print("this is negative")
# else :
#     print("this is zero")

# # #2
# number = int(input("Enter your number:-"))
# print("This is your number:-", number)
# if number % 2 == 0:
#     print("It is a even number")
# else :
#     print("It is a odd number")

# # #3
# total_marks = int(input("Enter your marks:-"))
# print(total_marks)
# if total_marks >= 33:
#     print("Pass")
# else :
#     print("Fail")

# # #4
# num1 = int(input("enter your first number:"))
# num2 = int(input("enter your second number"))
# num3 = int(input("enter your third number"))
# print("first number:-", num1)
# print("second number:-", num2)
# print("third number:-", num3)
# if num1 > num2 and num1 > num3:
#     print("First is largest")
# elif num2 > num3 and num2 > num1:
#     print("Second is largest")
# else : 
#     print("Third is largest")

# #5
# age = int(input("Enter your age:-"))
# print(age)
# if age >= 18:
#     print("you are eligible")
# else : 
#     print("you are not eligible")

# #6
# username = input("Enter your username:-")
# password = int(input("Enter your password:-"))
# if username == "garimaagarwal444":
#     if password == 123445678:
#         print("Your username is:-",username)
#         print("your password is:-", password)
#         print("Login successful")
#     else :
#         print("Your username is:-",username)
#         print("Password is not correct")
# else :
#     print("Invalid username")

# #7
# Password = int(input("enter your pin"))
# amount = float(input("enter withdrawal amount"))
# Balance = float(600000)
# if Password == 1234:
#     if Balance >= amount:
#         print("your balance is :-",Balance)
#         print("withdrawal amount :-",amount)
#         print("your transaction is successful")
#     else :
#         print("your balance is :-",Balance)
#         print("withdrawal amount :-",amount)
#         print("Not efficient balance")
# else :
#     print("Password is not correct")

# def prime():
#     for x in range(1,101):
#         if x>1:
#             for i in range(2,x):
#                 if x % i==0:
#                     break
#                 else:
#                     print(x)
# prime()

def grade(a):
    print(a)
    for x in a:
        if x>=90 and x<=100:
            print("A+")
        elif x>=80 and x<=90:
            print("A")
        elif x>=70 and x<=80:
            print("B")
        elif x>=60 and x<=70:
            print("C")
        elif x>=40 and x<=60:
            print("D")
        else:
            print("F")
b = [23,45,67,46,57]
grade(a = b)