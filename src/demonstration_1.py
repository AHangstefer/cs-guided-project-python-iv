"""
Given a string, implement a function that returns the string with all lowercase
characters.

Example 1:

Input: "LambdaSchool"
Output: "lambdaschool"

Example 2:

Input: "austen"
Output: "austen"

Example 3:

Input: "LLAMA"
Output: "llama"

*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*

"""
def to_lower_case(string):
    # create empty string or list to add output to
    # Convert each character to number
        #A-Z 65-90
        # if number is between 65-90, convert
        # otherwise leave it alone
    # add 32 
    # convert back
    # A(65) -> a(95)
    # B(66) -> b(98)
    output = ""
    for char in string:
        encoded_num = ord(char)
        if encoded_num >= 65 and encoded_num <= 90:
            encoded_num +=32
        output += chr(encoded_num)
    return output

print(to_lower_case("Hello World"))



