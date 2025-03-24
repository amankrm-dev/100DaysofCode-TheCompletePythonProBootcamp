from random import choice

import art

# Functions for Calculator
prev_result=0
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide  (n1,n2):
    return n1/n2

# Dictionary for basic calculator operations
operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def calculator():
    print(art.logo)
    should_accumulate=True

    num1=float(input("Enter the first number:\n"))
    while should_accumulate:
        for operators in operations:
            print(operators)
        operation_symbol=input("Pick a operator to perform desired calculations:\n")
        num2=float(input("Enter the second number:\n"))
        answer=operations[operation_symbol](num1,num2)
        print(f"\n {num1}{operation_symbol}{num2}={answer} \n")
        choice=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if choice=="y":
            num1=answer
        else:
            should_accumulate=False
            print("\n"*20)
            calculator()
calculator()


