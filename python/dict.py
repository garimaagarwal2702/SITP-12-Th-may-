#dictionary IS MUTTABLE and can have duplicate values
student= {"name":"garima",
           "class": "Second year",
             "roll no.":19,
               "branch":"CSE",
                 "adderess":"jaipur"}
# name, class, roll no, branch, address are keys 
# garima second year 21 and cse and jaipur are values
# key + values = "item"
# print(student)

# print("dict keys", student.keys())
# print("dict values", student.values())
# print("dict items",student.items())

# print(student['name'])
# print(student['class'])
# print(student['branch'])

# #adding item in dictionary
# student['subject'] = 'python'
# print(student)

# #task 1 to use the update function and also use from key
# print(student.get('name')) # get function is used to find the value of passed key

#print(student.clear()) # it doesn't take argument and clear whole dict
#print(student.copy()) # it will copy the whole dict as it is 
#print(student.pop("name")) # it takes argument the name of the key not index
#print(student.popitem()) # it takes out the last key and value from the dict and dont take argument

# car = {"brand":"kia",
#        "model": "seltos",
#        "year": 2000}
# print(car)
# x = car.setdefault("color", "green")
# print(x)

# # Task 2  deep copy and copy difference "

car = { "brand": ['ford', 'honda', 'hero'],
       "model": "mustang",
       "year": 1964}
       
print(car)
car['year'] = 2000 # updating the dict key value
print(car)

for x in car.values():
    print(x)

for x in car.keys():
    print(x)

for x in car.items():
    print(x)
 
