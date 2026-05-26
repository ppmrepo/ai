# def func(*param1):
#     print (param1)  

# func(1,2,3,4,5) # This will print the tuple (1, 2, 3, 4, 5) because we are passing multiple arguments to the function func, and the *param1 syntax allows us to capture all the arguments as a tuple inside the function.   



# def func2(age):
#     return "Major" if age >= 18 else "Minor" # This will return "Major" if the age is 18 or greater, and "Minor" if the age is less than 18 because we are using a ternary conditional operator to evaluate the condition and return the appropriate string based on the value of age.

# print (func2(20)) # This will print "Major" because the age 20 is greater than or equal to 18.

# def func3(db, user,password):
#     if (db=="MySQL" and user=="root" and password=="1234"):
#         return "MySQL Login successful"
#     elif (db=="Oracle" and user=="root"):
#         return "Oracle Login successful"
#     else:
#         return "Login failed" # This will return "Login failed" if the provided database, username, and password do not match any of the specified conditions in the function func3. The function checks for specific combinations of database, username, and password to determine the appropriate login message.
    
# print (func3("MySQL", "root", "1234")) # This will print "MySQL Login successful" because the provided database, username, and password match the first condition in the function func3.
# print (func3("Oracle", "root", "abcd")) # This will print "Oracle Login successful" because the provided database and username match the second condition in the function func3, even though the password does not match.
# print (func3("PostgreSQL", "admin", "admin")) # This will print

# def func4 (num1, num2):
#     sum = num1 + num2
#     print(sum, num1 , num2)

# func4(10,20) # This will print "10 20" because we are calling the function func4 with the arguments 10 and 20, which are passed to the parameters num1 and num2 respectively, and the function prints these values.

# #func4 (None, None)

# mul = lambda x : x*2

# print (mul(5))

# list1 = [1,2,3,4,5]

# square_list = list (map ( lambda x:x*x , list1)) # This will create a new list called square_list that contains the squares of the elements in list1. The map function applies the lambda function (which squares each element) to each element in list1, and the result is converted back to a list.)

# print (set(map(lambda x:x*x,list1))) # This will print a map object, which is an iterator that applies the lambda function to each element of list1. To see the actual squared values, we need to convert the map object to a list using the list() function, as shown in the previous line where we created square_list.        

# print (square_list)

# sort1 = sorted(list1 , reverse=True) # This will create a new list called sort1 that contains the elements of list1 sorted in descending order because we are using the sorted() function with the reverse=True argument, which sorts the elements in reverse (descending) order. The original list1 remains unchanged.
# print (set(sort1)) # This will print the sorted version of list1, which is [1, 2, 3, 4, 5] because the sorted() function returns a new sorted list from the elements of the original list.
# print (sort1)

list2 = [("num1", "40"), ("num2", "20"), ("num3", "30")]
sort4=sorted (list2, key=lambda X: X[1], reverse=True) # This will sort the list of tuples list2 based on the second element of each tuple (the string values "40", "20", "30") in descending order because we are using the sorted() function with a lambda function as the key argument to specify that we want to sort based on the second element of each tuple (X[1]), and we are also using the reverse=True argument to sort in descending order. The resulting order will be [("num1", "40"), ("num3", "30"), ("num2", "20")] because "40" comes before "30" and "20" in descending lexicographical order.
print (sort4) # This will print the sorted list of tuples, which is [("


# sort1 = sorted (list2) # This will sort the list of tuples list2 based on the first element of each tuple (the string values "num1", "num2", "num3") because the sorted() function by default sorts based on the first element of the tuples. The resulting order will be [("num1", "40"), ("num2", "20"), ("num3", "30")] because "num1" comes before "num2" and "num3" in lexicographical order.
# sort2

sort2 = sorted (list2, key=lambda X: X[1]) # This will sort the list of tuples list2 based on the second element of each tuple (the string values "40", "20", "30") because we are using the sorted() function with a lambda function as the key argument. The lambda function takes each tuple X and returns the second element (X[1]) for sorting. However, since the second elements are strings, they will be sorted lexicographically, resulting in the order [("num2", "20"), ("num3", "30"), ("num1", "40")].
print ("sorted list" , sort2) # This will print the sorted list of tuples, which is [(" 

dict1 = {"name1": "Alice", "name2": "Reb", "city": "Bet"}

sort3 = sorted (dict1.items(), key=lambda x:x[1]) # This will sort the items of the dictionary dict1 based on the values (the second element of each key-value pair) because we are using the sorted() function with a lambda function as the key argument. The lambda function takes each item (which is a tuple of key and value) and returns the value (x[1]) for sorting. The resulting order will be [("city", "New York"), ("age", 30), ("name", "Alice")] because "New York" comes before 30 and "Alice" in lexicographical order.
print ("sorted dict" , sort3) # This will print the sorted list of key-value pairs from the dictionary, which is [("city", "New York"), ("age", 30), ("name", "Alice")].

list5 = [10,15,20,25,30]

print (list(filter(lambda X:X%10==0,list5))) # This will print a list of elements from list5 that are divisible by 5 because we are using the filter() function with a lambda function that checks if each element X in list5 is divisible by 5 (X % 5 == 0). The resulting list will be [10, 15, 20, 25, 30] because all elements in list5 are divisible by 5.  


def multiparmfunc (**data):
    print (data) # This will print the dictionary data that contains all the keyword arguments passed to the function multiparmfunc. The **data syntax allows us to capture all the keyword arguments as a dictionary inside the function.


multiparmfunc(name="Alice", age=30, city="New York") # This will call the function multiparmfunc with three keyword arguments: name, age, and city. The function will print the dictionary {'name': 'Alice', 'age': 30, 'city': 'New York'} because the **data syntax captures all the keyword arguments as a dictionary inside the function.