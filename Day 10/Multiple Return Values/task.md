Functions terminate at the `return` keyword. If you write code below the return statement that code will not be executed.

However, you can have multiple return statements in one function. So how does that work?

### Conditional Returns

When we have control flow, as in the code will behave differently (go down different execution paths) depending on certain conditional checks, we can end up with multiple endings (returns).

e.g.
```
def canBuyAlcohol(age):
    if age >= 18:
        return True
    else:
        return False
```

### Empty Returns
You can also write return without anything afterwards, and this just tells the function to exit.

e.g.
```
def canBuyAlcohol(age):
    # If the data type of the age input is not a int, then exit.
    if type(age) != int:
        return

    if age >= 18:
        return True
    else:
        return False
```