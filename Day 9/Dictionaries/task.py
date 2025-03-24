from idlelib.colorizer import prog_group_name_to_tag

programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

# print(programming_dictionary["Bug"])
# programming_dictionary["Loop"]="Hello this is Loop"
# print(programming_dictionary["Loop"])
# # empty_dictionary={}
# # programming_dictionary={}
# print(programming_dictionary)
# print(programming_dictionary["Bug"])
# programming_dictionary["Bug"]="This is an insect"
# print(programming_dictionary["Bug"])
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])