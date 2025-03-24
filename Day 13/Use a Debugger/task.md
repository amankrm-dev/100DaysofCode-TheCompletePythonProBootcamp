Most IDEs (Intelligent Development Environments) such as PyCharm will have built-in tools for debugging. This is normally known as the debugger. In many ways, they are like print statements on steroids.

Debuggers allows us to peek into our code during execution and pause on chosen lines to figure out what is the inner mechanism and where it's going wrong. 

There are a couple of things that are the same in most IDEs which you should be familiar with:

1. **Breakpoint** - You can set a breakpoint by clicking on a line in the gutter of the code (where the line numbers are). This line will be where the program pauses during debug run.

2. **Step Over** - This button will go through the execution of your code line by line and allow you to view the intermediate values of your variables. 
3. **Step Into** - This will enter into any other modules that your code references. e.g. If you use a function from the random module it will show you the original code for that function so you can better understand its functionality and how it relates to your problems.
4. **Step Into My Code** - This does the same thing as Step Into, but it limits the scope to your own project code and ignores library code such as random.


### PAUSE 1
Use the PyCharm debugger to figure out what is the issue in the starting code and fix it.