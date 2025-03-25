#There is no bock scope in Python!
def is_prime(num):
    count=0
    for loop in range(1,num):
        if num%loop==0:
            count+=1
    if count==2:
        print("IT is a prime number ")
    else:
        print("NOt prime")
is_prime(9)