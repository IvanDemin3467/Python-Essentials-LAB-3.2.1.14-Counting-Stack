#This is the Python Essentials 2 LAB 3.2.1.14 Counting Stack

class Stack:
    # This class is a stack implementation
    def __init__(self):
        self.__stk = []  # This list contains stack values. This is private property

    def push(self, val):
        # This method is for pushing the next value onto the stack
        self.__stk.append(val)

    def pop(self):
        # This method is for popping the topmost value from the stack
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    # This class is a subclass of the Stack class
    # It implements a new function - counting elements in the stack
    def __init__(self):
        # This method overrides the constructor of the Stack class
        Stack.__init__(self)
        self.__count = 0        # a new property to store the number of elements on the stack

    def get_counter(self):
        # This method is for returning private property "__count"
        return self.__count

    def push(self, val):
        # This method overrides Stack.push(). It adds nothing
        Stack.push(self, val)

    def pop(self):
        # This method overrides Stack.pop() to implement counting
        val = Stack.pop(self)
        self.__count += 1
        return val


# Main
if __name__ == "__main__":
    stk = CountingStack()
    for i in range(100):
        stk.push(i)
        stk.pop()
    print(stk.get_counter())    # Should return 100





