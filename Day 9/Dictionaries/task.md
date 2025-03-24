A dictionary in Python functions similarly to a dictionary in real life. It's a data structure that allows us to associate a key to a value and pair the two pieces of data together.

This is how you create a dictionary in Python:
```
# An example dictionary
colours = {
    "apple": "red", 
    "pear": "green", 
    "banana": "yellow"
}

```

This is how you retrieve items from a dictionary:
```
print(colours["pear"])
#Will print "green"
```

This is how to create an empty dictionary:
```
my_empty_dictionary = {}
```

This is how you can add new items to an existing dictionary:

```
colours["peach"] = "pink"
```

This is also how you can edit an existing value in a dictionary:
```
colours["apple"] = "green"
```

This is how to loop through a dictionary and print all the keys:
```
for key in colours:
    print(key)
```

This is how to loop through a dictionary and print all the values:
```
for key in colours:
    print(colours[key])
```