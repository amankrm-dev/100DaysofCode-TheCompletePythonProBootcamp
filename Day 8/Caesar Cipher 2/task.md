### TODO-1: 
Create a function called `decrypt()` that takes `original_text` and `shift_amount` as 2 inputs.

### TODO-2: 
Inside the `decrypt()` function, shift each letter of the `original_text` forwards in the alphabet *backwards* by the `shift_amount` and print the decrypted text.

<div class="hint">
  You can multiply any number by -1 to make it a negative number.
</div>


### TODO-3: 
- Combine the `encrypt()` and `decrypt()` functions into a single function called `caesar()`. 
- Use the value of the user chosen `direction` variable to determine which functionality to use. 
- call the caesar function instead of encrypt/decrypt and pass in all three variables `direction`/`text`/`shift`.

<div class="hint">
  Remember that when you multiply a number by -1 it will reverse its sign.
e.g. <code>3 + ( 5 * -1) </code> is the same as <code>3 - 5</code>.
</div>


<div class="hint">
It should say:  

<code>Here is the encoded result: XXX</code>

or

<code>Here is the decoded result: XXX</code> 

</div>

