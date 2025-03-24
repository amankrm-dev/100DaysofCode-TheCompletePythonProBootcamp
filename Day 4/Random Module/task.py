import random

# from random import randint
# import my_module
# random_integer=random.randint(1,10)
# print(random_integer)
# print(my_module.my_fav_num)

# random_number_0_to_1=random.random()*10
# print(random_number_0_to_1)
# random_float=random.uniform(1,10)
# print(random_float)
result=random.randint(0,1)
print(result)
if result==0:
    print("Heads")
else:
    print("Tails")