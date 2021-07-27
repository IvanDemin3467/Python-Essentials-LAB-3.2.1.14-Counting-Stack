# Python-Essentials-LAB-3.2.1.14-Counting-Stack

**Objectives**

•	improve the student's skills in defining classes;

•	using existing classes to create new classes equipped with new functionalities.

**Scenario**

Your task is to extend the Stack class behavior in such a way so that the class is able to count all the elements that are pushed and popped (we assume that counting pops is enough). Use the Stack class we've provided in the editor.

Follow the hints:

•	introduce a property designed to count pop operations and name it in a way which guarantees hiding it;

•	initialize it to zero inside the constructor;

•	provide a method which returns the value currently assigned to the counter (name it get_counter()).

**Complete code includes**
```
class Stack:
    # This class is a stack implementation

    def push(self, val):
        # This method is for pushing the next value onto the stack

    def pop(self):
        # This method is for popping the topmost value from the stack


class CountingStack(Stack):
    # This class is a subclass of the Stack class
    # It implements a new function - counting elements in the stack
    def __init__(self):
        # This method overrides the constructor of the Stack class

    def get_counter(self):
        # This method is for returning private property "__count"

    def push(self, val):
        # This method overrides Stack.push(). It adds nothing

    def pop(self):
        # This method overrides Stack.pop() to implement counting
```
