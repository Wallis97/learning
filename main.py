#!/usr/bin/python3
# data types in python
message = "Hello, World!"
print(type(message))
print(message)
message = 3
print(type(message))
print(message)
message = True
print(type(message))
print(message)
message = 3.14
print(type(message))
print(message)

# lists
#         -4-3-2-1
my_list = [2,4,6,7]
#          0 1 2 3
another_list = [4,2,6,7]
#          -11-10-9-8-7-6-5 -4-3-2 -1                       
long_list = [3,4, 7,3,8,4,8,33,8,8, 6]
#            0 1 2 3 4 5 6  7 8 9 10
print("are lists equal: ", my_list == another_list)
print("accessing an element of a list : ",my_list[3], my_list[-4])
print("sum of lists: ",my_list + another_list)
print("multiplication of lists: ", my_list * 3)
print("strings can be multiplicated as well: ","message "*5)
start = 2
end = 7
step = 2
print("slicing a list: ", long_list[start : end : step])
print("reversing a list: ", long_list[::-1])
print("reversing a string: ", "very important message to the world"[::-1])
# write a program to invert order of the words 

# tuples 
my_tuple = (3,5,4,4,"message")
another_tuple = (5,3,4,"message")
print(my_tuple, my_tuple[3])
# my_tuple[2] = 5 # cannot do that 
print("comparing tuples: ", my_tuple == another_tuple)

# sets 
my_set = { 3 ,5,7,3}
another_set = {7,3,5}
print(my_set)
print("comparing sets: ", my_set == another_set)
# print(my_set[2]) # cannot access sets element this way

# dictionaries
my_dictionary = {"key1":"value1","key2":"value2","key3":"value3"}
person = {
    "first name":"Ola",
    "last name": "Paczkowska",
    "city":"Sulimów",
    "city": "Wroclaw"
}
print("accessing dictionary elements: ", person["first name"])


