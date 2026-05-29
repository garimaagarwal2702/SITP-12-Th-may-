# Tuple 
# tpl = (1,2,3,'hello',1,20) # tuple allows duplicate values also all data types
# print("this is my first tuple",tpl) # it is immutable
# print("len of my tuple:-", len(tpl))

# # indexing and slicing
# print(tpl[0])
# print(tpl[1])
# print(tpl[2])
# print(tpl[3])
# print(tpl[4])
# print(tpl[2:5])
# print(tpl[::-1])

#tuple decalre
# a = 1,2,54,45,65,'hello' # by default if we type something like this it will automatically give tuple
# print(a)
# print(type(a))
# print(len(a))

#tuple unpacking
# a, b, c = (1,2,3)
# print(a)
# print(b)
# print(c)

# a,b = (1,2,3,)
# print(a) # this will give error and don't print anything
# print(b)

a,b,c = (1,2,3)
print(a)
print(b) # this will not give error and print a and b as 1 and 2

# tpl = (1,2,3,"hello",3,2,5.5,6)
# print(tpl)
# print(tpl.count(2)) # we have to argument of what element we want to know the no. of elements in tuple
# print(tpl.index(2)) # we use index to know the index of given element of tuple in index

# #type casting
# tpl = (1,2,3,"hii",5,4)
# print("this is my tuple", tpl)
# print("type of my tuple", type(tpl))
# print("tpl convert into list")
# lst = list(tpl)
# print("this is my list", lst)
# print("this is the type", type(lst))
# lst.append(100)
# print(lst)
# tpl = tuple(lst)
# print(tpl)
