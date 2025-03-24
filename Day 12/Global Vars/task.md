You can force the code allow you to modify something with global if you use the global keyword before you use it.

e.g. This will give you an error

```
a = 1
def my_function():
    a += 1
    print(a)
```

But this will work
```
a = 1
def my_function():
    global a
    a += 1
    print(a)
```