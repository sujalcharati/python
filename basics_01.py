    # printing 
# def myname(name):
#     print('my name is ',name)
# myname('sujal')


# def calculateOperation( len ,wid):
#     # area =len*wid
#     area =len**wid
#     print(area)
# calculateOperation(2,4)    
    
# def checkRelation():
#     # if(2==2):
#     if(2!=3):
#         print('its equal')
#     else:
#         print('its not equal')
# checkRelation();        
    

#           variable assign
# def variableAssigns():
#     sujalage=19
#     sujalgender='male'
#     print(f'{sujalage}, {sujalgender}')
# variableAssigns()


                # list
# mylist =["sonu", "suchi","susama"]
# print(mylist)
# print(mylist[0])
# print(len(mylist))
# del mylist[1]
# print(mylist)


        #    range
# a = range(10)
# in_between_numbers = list(a[1:5])
# print(in_between_numbers)


# Using list.append to add elements to a list
# mylist = ["sonu", "suchi", "susama"]
# print("Original list:", mylist)

# # Appending new elements to the list
# mylist.append("sujal")
# mylist.append("sunu")

# print("Updated list:", mylist)

                       # Taking user input and converting types
# def userInputConversion():
#     # Taking integer input
#     user_age = int(input("Enter your age: "))
#     print(f"Your age is: {user_age} and its type is {type(user_age)}")

#     # Taking float input
#     user_height = float(input("Enter your height in meters: "))
#     print(f"Your height is: {user_height} meters and its type is {type(user_height)}")

#     # Taking string input
#     user_name = input("Enter your name: ")
#     print(f"Your name is: {user_name} and its type is {type(user_name)}")

# userInputConversion()
                   

             #    if control flow
# def checkAge():
#     your_age =int(input('enter your age'))
#     if(your_age >=18):
#         print('eligible to vote')
#     else:
#         print(' Not eligible to vote ')
# checkAge()        
              


        #   looping statment
# Using while loop to print numbers from 1 to 5
# def printNumbers():
#     i = 1
#     while i <= 5:
#         print(i)
#         i += 1

# printNumbers()
# # Using for loop to print numbers from 1 to 5
# def printNumbersForLoop():
#     for i in range(1, 6):
#         print(i)

# printNumbersForLoop()



# Using list comprehension to create a new list with names in uppercase
# people = ["sonu", "suchi", "susama", "sujal", "sunu"]
# uppercase_people = [x.upper() for x in people]
# print(uppercase_people)


# Using map and split to convert a list of strings to a list of integers
# def convertStringToInt():
#     string_numbers = "1 2 3 4 5"
#     list_of_strings = string_numbers.split()
#     list_of_integers = list(map(int, list_of_strings))
#     print(list_of_integers)

# convertStringToInt()

# # Using map and split to convert a list of strings to a list of floats
# def convertStringToFloat():
#     string_numbers = "1.1 2.2 3.3 4.4 5.5"
#     list_of_strings = string_numbers.split()
#     list_of_floats = list(map(float, list_of_strings))
#     print(list_of_floats)

# convertStringToFloat()


# Using a lambda function to add two numbers
# add = lambda x, y: x + y
# result = add(5, 3)
# print(result)
# # Using a lambda function to multiply two numbers
# multiply = lambda x, y: x * y
# result = multiply(5, 3)
# print(result)

# # Using a lambda function to find the maximum of two numbers
# maximum = lambda x, y: x if x > y else y
# result = maximum(5, 3)
# print(result)

# # Using a lambda function to check if a number is even
# is_even = lambda x: x % 2 == 0
# result = is_even(4)
# print(result)

# # Using a lambda function to reverse a string
# reverse_string = lambda s: s[::-1]
# result = reverse_string("hello")
# print(result)


# Writing to a file
# def writeToFile():
#     with open('example.txt', 'w') as file:
#         file.write('Hello, this is a test file.\n')
#         file.write('This is the second line.\n')

# writeToFile()

# Reading from a file
# def readFromFile():
#     with open('example.txt', 'r') as file:
#         content = file.read()
#         print(content)

# readFromFile()

# Appending to a file
# def appendToFile():
#     with open('example.txt', 'a') as file:
#         file.write('This is an appended line.\n')

# appendToFile()
# readFromFile()

# # Reading a file line by line
# def readFileLineByLine():
#     with open('example.txt', 'r') as file:
#         for line in file:
#             print(line.strip())

# readFileLineByLine()




# Working with dictionaries
# def dictionaryExamples():
#     # Creating a dictionary
#     person = {
#         "name": "Sujal",
#         "age": 19,
#         "gender": "male"
#     }
#     print("Original dictionary:", person)

#     # Accessing values in a dictionary
#     print("Name:", person["name"])
#     print("Age:", person["age"])

#     # Adding a new key-value pair
#     person["city"] = "Kathmandu"
#     print("Updated dictionary:", person)

#     # Updating an existing key-value pair
#     person["age"] = 20
#     print("Dictionary after updating age:", person)

#     # Deleting a key-value pair
#     del person["gender"]
#     print("Dictionary after deleting gender:", person)

# dictionaryExamples()

# # Working with tuples
# def tupleExamples():
#     # Creating a tuple
#     my_tuple = ("apple", "banana", "cherry")
#     print("Original tuple:", my_tuple)

#     # Accessing elements in a tuple
#     print("First element:", my_tuple[0])
#     print("Second element:", my_tuple[1])

#     # Tuples are immutable, so we cannot change their elements
#     # But we can concatenate tuples
#     new_tuple = my_tuple + ("date", "elderberry")
#     print("Concatenated tuple:", new_tuple)

#     # Finding the length of a tuple
#     print("Length of the tuple:", len(my_tuple))

#     # Unpacking a tuple
#     (fruit1, fruit2, fruit3) = my_tuple
#     print("Unpacked tuple:", fruit1, fruit2, fruit3)

# tupleExamples()