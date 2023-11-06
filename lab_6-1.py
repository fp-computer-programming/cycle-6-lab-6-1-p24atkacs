"""
Create a Python file named lab_6-1.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***


Create a array that contains the numbers 1 to 5 store it as a variable called my_arr.
Write a statement using the indexing operator that prints the number 3 in my_arr.
Write a statement that prints the length of my_arr.
Write a statement that repeats my_arr 3 times.
Write a statement that converts "string" to an array.


"""

# Author: Andrew Tkacs

# Create an array that contains the numbers 1 to 5

my_arr = [1, 2, 3, 4, 5]

# Write a statement using the indexing operator that prints the number 3

# This will print the third element, which is 3.

print(my_arr[2])

#this will print the length of my_arr, because of the len function

print(len(my_arr))  

# Write a statement that repeats my_arr 3 times.

repeated_arr = my_arr * 3

print(repeated_arr)  # This will print my_arr repeated 3 times.

# Write a statement that converts "string" to an array.

string_to_array = list("string")

print(string_to_array)  # This will convert the string into a list of characters and print it.
