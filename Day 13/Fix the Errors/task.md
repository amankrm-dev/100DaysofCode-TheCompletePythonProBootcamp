Fix any errors (red underlines) that show up in the editor before you run your code. The warnings (yellow) are optional fixes, sometimes it will cause a problem down the line other times it's fine and the editor just doesn't understand what you are trying to do.

### Catching Exceptions
You can use a try/except block in Python to catch any exceptions that might occur. For example if you imagine there could be a chance of user error. You can prevent it crashing your code by anticipating it. You trap the dangerous code inside a try block and use an except block to catch any potential errors. Then you define what should happen when that error occurs instead of simply just crashing and stopping the code.

e.g.

```
try:
    print(6 > "five")
except TypeError:
    print("You can't mix integers and strings in a comparison")
```

### PAUSE 1 
Fix the bug so that the print statement displays the correct value of age in the output area.