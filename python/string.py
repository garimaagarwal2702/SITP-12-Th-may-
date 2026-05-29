#string rules-
# #1 sequence of characters written inside quotes.
# #2 includes letters, numbers and spaces
# #3 strings are immutable unchanged
# #4 but we can manipulate strings use methods like concatenation, slicing, formatting to create new string
# #5 delete entire stirng variable (python not possible to delete individyal character)

a = 'hello'
print(a)

b = 'python is good'
print(b)

c = '''hey how you
sab badiya
main theek hu'''
print(c)

# name = "garima"
# print("MY name is :-", name)
# print("type of my variable :-", type(name))

# print("len of my string :- ",len(name)) #tell characters of the string

# upper_case = name.upper()#converts all elments in upper case
# print(upper_case)

# lower_case = name.lower()#converts all elements in lower case
# print(lower_case)

# name = "RIYA"
# print(name.casefold())

##Task 1 what is difference between lower() and casefold()
#a = "Straße"
#print(a.lower()) #lower prints only normal language into lower and don't change in english 
#b = "Straße"
#print(b.casefold()) # casefold prints multi language into lower and change in english 

##Task 2 what is differnce between title() and capitalize()
# name = "riya"
# print(name.title()) # title toh agar paragraph likha ho toh har word ka first letter capital ho jata h
# print(name.capitalize()) # isme paragraph ka first word ka first letter convert ho jata h

## how to reverse string this is task 3
#name = "Garima"
#print(name[::-1]) # it will reverse all values without giving range

##task 4 can the space between strings can be removed by strip
#name = "upflairs      " # jab koi string ke aage ya peeche space jyada lag jaye toh vo bhi length me count hote h
#print(len(name))  # toh unko hatane ke liye strip use karte h 
#print(name.strip()) # lekin strip beech wale space nhi hatata

#indexing and slicing
name = "Garima Agarwal"
print(name[2])
print(name[2:8])

#indexing
print(name[-1])#shows last element of string

name = "erika" #we can also add space after this.
last_name = "fernendas" 

print(name + " " + last_name)

str1 = "garima"
str2 = "agarwal"
#print(str1 * str1)
print(str1 + str1)#this will run and print name two times
print(str1 + str2)#this will print both names without space in between
#print(str1 + 2)
print(str1 * 2)#this will also give outout

#print(str1 * str2)#this cant happen because this is not valid 

##task 5 what is differnce between this 
#name = 'dev'
#name = "dev"

intro = "helllo my name is garima " 
intro1 ="hello my \n name is  \n garima" # jaha jaha apan ko list ke element devide karne h vaha vaha \n use kare

print(intro) 
print(intro1.split("\n")) # intro1 string thi lekin split karne baad vo list me save hota h

name = "bhalu"
address = "jaipur" # f is used to do formatting
print(f"my name is {name} and i from {address}")  # f is used to define a variable in between the string in print

#input function is used to take input from user
name = input("enter your name:-")
print(name)
print(type(name))

#while taking input if integer value is needed as input we will predefine first its datatype because 
#python always return string value and we have to typecast it to return in any other value.

num1 = int(input("enter first number:-"))
num2 = int(input("enter second number"))
print(num1, num2)
print(type(num1))
print(type(num2))