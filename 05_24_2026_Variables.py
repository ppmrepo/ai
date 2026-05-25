# # num1 = 200
# # num2 = 300
# # result = num1 + num2
# # print("The result of adding", num1, "and", num2, "is:", result)
# # print (type(num1)) # This will print the type of num1, which is <class 'int'>

# # x = 10.5
# # y = -5.2
# # z = x + y
# # print("The result of adding", x, "and", y, "is:", z)
# # print (type(y))

# # name = "Alice"
# # greeting = "Hello, " + name + "!"
# # print(greeting) 

# # address = '123 Main Street  Cityville'
# # print("The address is:", address)
# # print (type(address))   

# # city = """New York
# #          USA
# #          Earth"""
# # print("The city is:", city)
# # print (type(city))

# # print ("First char" ,greeting[0]) # This will print the first character of the greeting string, which is 'H'
# # print ("Last char" ,name[-1]) # This will print the last character of the greeting string, which is '!'
# # print ("Substring" ,greeting[0:9]) # This will print the substring of
# # print ("Length of greeting" ,len(greeting)) # This will print the length of the greeting string, which is 13
# # print ("Uppercase greeting" ,greeting.upper()) # This will print the greeting string in uppercase, which is 'HELLO, ALICE!'
# # print ("Lowercase greeting" ,greeting.lower()) # This will print the greeting string in lowercase, which is 'hell

# # print ("Substring " ,len(name)) # This will raise an error because  there is no method called length() for strings. The correct way to get the length of a string is to use the len() function, like this: len(greeting)

# # print ("reverse", name[:: -1]) # This will print the name string in reverse order, which is 'ecilA'
# # print ("last two chars " ,name[-2:-1])

# # print ("last two chars " ,name[-2:]) # This will print the last two characters of the name string, which is 'ce'    

# # str1 ="Python"
# # #str1[0] = 'J' # This will raise an error because strings in Python are immutable, meaning that you cannot change individual characters of a string after it has been created.
# # str2 ="Hi" + " "+ str1
# # print (str2) # This will print 'HiPython' because we are concatenating the string 'Hi' with the string 'Python' and storing the result in str2.

# # print (str1 * 3) # This will print 'PythonPythonPython' because we are repeating the string 'Python' three times using the multiplication operator (*).

# # print ("Py" in str1) # This will raise an error because 'py' is not defined as a variable. If you want to check if the substring 'py' is in the string 'Python', you should use quotes around 'py', like this: 'py' in str1. This will return False because 'py' is not a substring of 'Python'.    

# # print ("Python".upper()) # This will print 'PYTHON' because we are calling the upper() method on the string 'Python', which converts all characters to uppercase.

# # print ("PYTHON".lower()) # This will print 'python' because we are calling the lower() method on the string 'PYTHON', which converts all characters to lowercase.

# # print ("   Hello, World!   ".strip()) # This will print 'Hello, World!' because we are calling the strip() method on the string '   Hello, World!   ', which removes any leading and trailing whitespace characters.

# # print ("Hello, world".replace("world","Python")) # This will print 'Hello, Python' because we are calling the replace() method on the string 'Hello, world', which replaces all occurrences of the substring 'world' with the substring 'Python'.

# # print ("Hello, world".split(",")) # This will print ['Hello', ' world'] because we are calling the split() method on the string 'Hello, world', which splits the string into a list of substrings based on the delimiter ','.

# # print ("Hello World".lower())

# # print (",".join(["Hello", "World"]).replace(","," ")) # This will print 'Hello,World' because we are calling the join() method on the string ',', which concatenates the elements of the list ['Hello', 'World'] into a single string with ',' as the separator.

# str2 = "PYTHON"

# # for ch in str2:
# #     print (ch) # This will print each character of the string 'PYTHON' on a new line because we are iterating over the string using a for loop and printing each character.


# for ch in str2[::-1]:
#     print (ch) # This will print each character of the string 'PYTHON' in reverse order on a new line because we are slicing the string with a step of -1, which reverses the string, and then iterating over it with a for loop to print each character.


# str3 ="Welcome"
# str4 = "to Python programming"

# msg = f"{str3} {str4}" # This will create a formatted string using an f-string, which allows us to embed expressions inside string literals. The resulting string will be 'Welcome to Python programming' because we are concatenating the values of str3 and str4 with a space in between.
# print ("Formated Message: " +msg)

# print("Hello \n World") # This will print 'Hello' and 'World' on separate lines because we are using the newline character (\n) to indicate a line break in the string.

# print ("Hello \t World") # This will print 'Hello' and 'World' separated by a tab space because we are using the tab character (\t) to indicate a horizontal tab in the string.   

list1 = [1,2,3,4,5,6,1]

print (list1)
print (type(list1)) # This will print the type of list1, which is <class 'list'>
print (list1[0]) # This will print the first element of the list, which is 1
print (list1[-1]) # This will print the last element of the list, which is 1
print (list1[0:3]) # This will print the first three elements of the list, which are [1, 2, 3]
print (len(list1)) # This will print the length of the list, which is 7

for item in list1:
    print (item) # This will print each element of the list on a new line because we are iterating over the list using a for loop and printing each item.   

for ch in list1[::-1]:
    print (ch) # This will print each element of the list in reverse order on a new line because we are slicing the list with a step of -1, which reverses the list, and then iterating over it with a for loop to print each element.


print ("Original List:" ,list1) # This will print the original list, which is [1, 2, 3, 4, 5, 6, 1]

list1[3] =35

print ("Modified List:" ,list1) # This will print the modified list, which is [1, 2, 3, 35, 5, 6, 1] because we are changing the value of the element at index 3 to 35.




tuple1 = (1,2,3,4,5,6,1)
print (tuple1)
print (type(tuple1)) # This will print the type of tuple1, which is <class 'tuple'>
print (tuple1[0]) # This will print the first element of the tuple, which is 1
print (tuple1[-1]) # This will print the last element of the tuple, which is 1
print (tuple1[0:3]) # This will print the first three elements of the tuple, which are (1, 2, 3)
print (len(tuple1)) # This will print the length of the tuple, which is 7

# tuple1[3] =35 # This will raise an error because tuples in Python are immutable, meaning that you cannot change individual elements of a tuple after it has been created.

set1 = {1,2,3,4,5,6,1}
print (set1)
print (type(set1)) # This will print the type of set1, which is <

print (len(set1)) # This will print the length of the set, which is 6 because sets do not allow duplicate elements, so the second occurrence of 1 is ignored.

set1.add(7) # This will add the element 7 to the set, resulting in {1, 2, 3, 4, 5, 6, 7}
print (set1) # This will print the modified set, which is {1, 2, 3, 4, 5, 6, 7} because we added the element 7 to the set.

dict1 = {"name": "Alice", "age": 30, "city": "New York"}
print (dict1)

print (type(dict1)) # This will print the type of dict1, which is <class 'dict'>
print (dict1["name"]) # This will print the value associated with the key "name", which is "Alice"
print (dict1["age"]) # This will print the value associated with the key "age", which is 30
print (dict1["city"]) # This will print the value associated with the key "city", which is "New York"
print (len(dict1)) # This will print the number of key-value pairs in the dictionary, which is 3    


