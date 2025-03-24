friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
import random

# -------------------------*********************__________________________________
Draw_Card=random.randint(0,4)
# if Draw_Card==0:
#     print(friends[0]+"Pays the Bill")
# elif Draw_Card==1:
#     print("Bob Pays the Bill")
# elif Draw_Card==2:
#     print(friends[2]+" Pays the Bill")
# elif Draw_Card==3:
#     print(friends[3]+" Pays the Bill")
# else:
#     print(friends[4]+" Pays the Bill")


# ---------------------------*******************----------------------------------------
# print(random.choice(friends))
# --------------------------***********************--------------------------------------

print(friends[Draw_Card])