# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it")
# my_function()



# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# The for loop is traversing from index 1 to index 19 in the above code as range (1,20) means that the for loop should move from 1 to (20-1)

# 2. When is the function meant to print "You got it"?
#     While traversing from start to the end if the value of i is equals to 20 then the if condition satisfies

# 3. What are your assumptions about the value of i?
#  If we make the range function (1, 20+1) or simply (1,21) we will get the value of i as 20



# Debugging

def my_function():
    for i in range(1, 20+1):
        if i == 20:
            print("You got it")
my_function()