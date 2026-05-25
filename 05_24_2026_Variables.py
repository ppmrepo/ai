# num1 = 200
# num2 = 300
# result = num1 + num2
# print("The result of adding", num1, "and", num2, "is:", result)
# print (type(num1)) # This will print the type of num1, which is <class 'int'>

# x = 10.5
# y = -5.2
# z = x + y
# print("The result of adding", x, "and", y, "is:", z)
# print (type(y))

# name = "Alice"
# greeting = "Hello, " + name + "!"
# print(greeting) 

# address = '123 Main Street  Cityville'
# print("The address is:", address)
# print (type(address))   

# city = """New York
#          USA
#          Earth"""
# print("The city is:", city)
# print (type(city))

# print ("First char" ,greeting[0]) # This will print the first character of the greeting string, which is 'H'
# print ("Last char" ,name[-1]) # This will print the last character of the greeting string, which is '!'
# print ("Substring" ,greeting[0:9]) # This will print the substring of
# print ("Length of greeting" ,len(greeting)) # This will print the length of the greeting string, which is 13
# print ("Uppercase greeting" ,greeting.upper()) # This will print the greeting string in uppercase, which is 'HELLO, ALICE!'
# print ("Lowercase greeting" ,greeting.lower()) # This will print the greeting string in lowercase, which is 'hell

# print ("Substring " ,len(name)) # This will raise an error because  there is no method called length() for strings. The correct way to get the length of a string is to use the len() function, like this: len(greeting)

# print ("reverse", name[:: -1]) # This will print the name string in reverse order, which is 'ecilA'
# print ("last two chars " ,name[-2:-1])

# print ("last two chars " ,name[-2:]) # This will print the last two characters of the name string, which is 'ce'    

# str1 ="Python"
# #str1[0] = 'J' # This will raise an error because strings in Python are immutable, meaning that you cannot change individual characters of a string after it has been created.
# str2 ="Hi" + " "+ str1
# print (str2) # This will print 'HiPython' because we are concatenating the string 'Hi' with the string 'Python' and storing the result in str2.

# print (str1 * 3) # This will print 'PythonPythonPython' because we are repeating the string 'Python' three times using the multiplication operator (*).

# print ("Py" in str1) # This will raise an error because 'py' is not defined as a variable. If you want to check if the substring 'py' is in the string 'Python', you should use quotes around 'py', like this: 'py' in str1. This will return False because 'py' is not a substring of 'Python'.    

# print ("Python".upper()) # This will print 'PYTHON' because we are calling the upper() method on the string 'Python', which converts all characters to uppercase.

# print ("PYTHON".lower()) # This will print 'python' because we are calling the lower() method on the string 'PYTHON', which converts all characters to lowercase.

# print ("   Hello, World!   ".strip()) # This will print 'Hello, World!' because we are calling the strip() method on the string '   Hello, World!   ', which removes any leading and trailing whitespace characters.

# print ("Hello, world".replace("world","Python")) # This will print 'Hello, Python' because we are calling the replace() method on the string 'Hello, world', which replaces all occurrences of the substring 'world' with the substring 'Python'.

# print ("Hello, world".split(",")) # This will print ['Hello', ' world'] because we are calling the split() method on the string 'Hello, world', which splits the string into a list of substrings based on the delimiter ','.

# print ("Hello World".lower())

# print (",".join(["Hello", "World"]).replace(","," ")) # This will print 'Hello,World' because we are calling the join() method on the string ',', which concatenates the elements of the list ['Hello', 'World'] into a single string with ',' as the separator.

str2 = "PYTHON"

# for ch in str2:
#     print (ch) # This will print each character of the string 'PYTHON' on a new line because we are iterating over the string using a for loop and printing each character.


for ch in str2[::-1]:
    print (ch) # This will print each character of the string 'PYTHON' in reverse order on a new line because we are slicing the string with a step of -1, which reverses the string, and then iterating over it with a for loop to print each character.


str3 ="Welcome"
str4 = "to Python programming"

msg = f"{str3} {str4}" # This will create a formatted string using an f-string, which allows us to embed expressions inside string literals. The resulting string will be 'Welcome to Python programming' because we are concatenating the values of str3 and str4 with a space in between.
print ("Formated Message: " +msg)

print("Hello \n World") # This will print 'Hello' and 'World' on separate lines because we are using the newline character (\n) to indicate a line break in the string.

print ("Hello \t World") # This will print 'Hello' and 'World' separated by a tab space because we are using the tab character (\t) to indicate a horizontal tab in the string.   

