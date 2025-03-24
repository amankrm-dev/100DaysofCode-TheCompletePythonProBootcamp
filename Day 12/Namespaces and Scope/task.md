### Local Scope
Variables (or functions) declared inside functions have local scope (also called function scope). They are only seen by other code within the same block of code.

e.g.
```
def my_function():
    my_local_var = 2
    
# This will cause a NameErrorr
print(my_local_var) 
```

### Global Scope
Variables or functions declared at the top level (unindented) of a code file have global scope. It is accessible anywhere in the code file.

e.g.

```
my_global_var = 3

def my_function():
    # This works no problems
    print(my_global_var)
```