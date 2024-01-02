# class Stack - the main class for Stack seen in lecture 5.
# Reminder: stack is a private variable
# To complete: *  __str__ method must be included that displays the stack in reverse
# order from the bottom to the top (with index 0 at the bottom)
#             * swap method: two swap the top with top-1 item
#             * copy method: duplicate the top item
#             * flush method: to empty the stack

class Stack:
    # constructor
    def __init__(self):
        self.__stack = []  # create private stack

    # methods

    def __str__(self):
        s = ""
        for i in range(self.getSize()):
            s += f"{i}\t{self.__stack[i]}\n"
        return s

    def swap(self):
        a = self.__stack.pop()
        b = self.__stack.pop()
        self.push(a)
        self.push(b)
        return self.__stack

    def copy(self):
        if self.isEmpty(): return None
        return self.push(self.__stack[-1])

    def flush(self):
        for i in range(self.getSize()):
            self.pop()
        return None

    def pop(self):  # pop the item
        if self.isEmpty(): return None
        return self.__stack.pop()

    def peek(self):  # peek the item (no removal)
        if self.isEmpty(): return None
        return self.__stack[len(self.__stack) - 1]

    def push(self, item):  # push the item
        self.__stack.append(item)

    def getSize(self):  # return stack size
        return len(self.__stack)

    def isEmpty(self):  # check if stack empty
        return self.getSize() == 0


################################
################################

def main():
    mystack = Stack()
    for i in range(1, 4): mystack.push(i * 10)

    print("test __str__")
    print(mystack)

    print("test swap")
    mystack.swap()
    print(mystack)

    print("test copy")
    mystack.copy()
    print(mystack)

    print("test flush")
    mystack.flush()
    mystack.push(11)
    print(mystack)


## call the main function if this file is directly executed
if __name__ == "__main__":
    main()
