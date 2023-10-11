'''
Write a method (or function, depending on the language) that converts a string 
to camelCase, that is, all words must have their first letter capitalized 
and spaces must be removed.

Examples (input --> output):

"hello case" --> "HelloCase"
"camel case word" --> "CamelCaseWord"
'''

def camel_case(s):
    return ''.join([char for char in s.title() if not char.isspace()])

print(camel_case("test TEST test test"))
print(camel_case("The greatest 9 things in life"))
print(camel_case("two things to do this weekend"))
print(camel_case("Something WICKED this way comes"))
print(camel_case("I need 18 spoons. Now!"))
print(camel_case(""))