### TODO-1: 
Import and print the logo from art.py when the program starts.

### TODO-2: 
What happens if the user enters a number/symbol/space that's not in the List `alphabet`?

Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?

e.g. 
```
original_text = "meet me at 3!"
cipher_text = "XXXX XX XX 3!"
```

<div class="hint">
  If it's not a letter in the List alphabet, maybe you can just add it to the end of cipher_text as the unmodified character?
</div>


### TODO-3: 

Can you figure out a way to restart the cipher program?

e.g. 

`Type 'yes' if you want to go again. Otherwise, type 'no'.`

If they type 'yes' then ask them for the direction/text/shift again and call the `caesar()` function again.

<div class="hint">
  Try creating a while loop that continues to execute the program if the user types 'yes'.
</div>
