print("hello world")
print("123hello")

a = 34
b = "garima"

print(a)
print(b)

x = y = z = "orange"
print(x)
print(y)
print(z)

x = "A" 
y = "B" 
z = "C"
print(x)
print(y)
print(z)

#VARIABLE -- variables are containers for storing data values.
#a variable name must start with a letter or the underscore character
#a variable name can onlly contqain alpha numeric characters and underscores 
#a variable name cannot start with a number
#a variable names are case sensitive ( age ,Age and AGE are thr4e different variables)
#this means uppercase and lowercase letters are treated as diferent variables. 
#a variable name cannot be any of the python keywords.

myvar = "John"
my_var = "John"
_my_var = "John"
My_var = "John"
MYVAR = "John"
myvar2 = "John"

#print() pretty flexible

print(34)
print("salman khan")
#print(salmen khan)
print("divya",23,56.5 ,"true")
print("divya",56,"radhika")

print("hello kaha se ho ap", end="-")
print("main jaipur se hu")

print("hello", end="-")
print("world")

print("hello"); print("how you"); print("i m ok")
print(x, y, z)

#dynamic typing --- c, c++ language you habe tell the datatype before giving value to 

x = 56
print(x)
print(type(x))
#dyanamic binding == in python there is no fix datatype 

a= 45
print(a)

a = "divya"
print(a)

a = int('5')
print(a)
print(type(a))
#many vlaues to many variable -- pythohn allowaws yiou to aswsign valyes to multiple variables in one line

x,y,z = "apple","orange","banana"
print(x)
print(y)
print(z)

x = y = z = "orange"
print(x)
print(y)
print(z)

#unpack a collection == if you have a collection of values in a list, tuple etac
#puthon allows you to extract the vvlaues into variables.
#list unpackung

a = ["divya","apple","juice"]
x,y,z = a
print(x)
print(y)
print(z)

#tuple unpack
x = (3,4,5,)
a,b,c = x
print(a,b,c)

#string unpack
name = "ABC"
a,b,c = name
print(a,b,c)

x = "python"
y = "is"
z = "good"
print(x,y,z)

#casting -- if you want ot specify the data type of a variabl, this can be done with casting

x = int(3)
y = float(3)
z = str(3)
print(x)
print(y)
print(z)

#type conversion --- you can convert from one type to another with the int(). FLOAT(),
#1. IMPLICIT TYPE CONVERTION -- INTERNALLY KNOW THE DATATTYPE

print(6 + 5.8)
print(type(5),type(5.8))

print('5' + '5.9')
print(type('5'),type('5.9'))

#2. explicit type conversion -- program req  to change datatype
x = float(20)
print(x)

#user input -- 
#static VS dynamic software -- static dont talk with user they only gives informaton 
##dynamic -- user input data hai ( youtube, ola and ezomato)
a = input("what is your name:")
b = input("what is your age:")
print(a)
print(b)

a = input("enter a first number")
b = input("enter a second number")
c = a + b
print(c)

a = int(input("enter a first number"))
b = int(input("enter a second number"))
c = a + b
print(c)

name = input("apna naam batao:")
print("hello", name)

p = int(input("enter a number:"))
q = int(input("enter a second number:"))

sum = p*q
print("total= ", sum)

#swap two numbers program
a = 20 
b = 12

a,b = b,a
print("A:", a)
print("B:", b)

c = 30
a,b,c = c,a,b
print("A:", a)
print("B:", b)
print("C:", c)

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
