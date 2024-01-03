# class StackCalc: a class that extends (inherit) the functionalities
# of the class Stack 

from Stack import *
import copy
import numpy as np  # if you need sin, just do np.sin, etc.


class StackCalc(Stack):
    def __init__(self):
        super().__init__()

    @staticmethod
    def postfix2infix(postfix):
        myqueue = postfix
        infix_stack= []
        while not myqueue.isEmpty():
            token = myqueue.dequeue()

            if token in ('+', '-', '*', '/'):
                rightOperand = infix_stack.pop()
                leftOperand = infix_stack.pop()
                infixSubstring = "(" + leftOperand + token + rightOperand + ")"
                infix_stack.append(infixSubstring)
            elif token == '^':
                rightOperand = infix_stack.pop()
                leftOperand = infix_stack.pop()
                infixSubstring = "(" + leftOperand   + ")**"+ rightOperand
                infix_stack.append(infixSubstring)
            elif token in ('sin', 'cos', 'exp', 'log', 'abs', 'sqrt'):
                operand = infix_stack.pop()
                infixSubstring = token + "(" + operand + ")"
                infix_stack.append(infixSubstring)
            elif token in ('pi', 'e'):
                infix_stack.append(token)
            else:
                infix_stack.append(token)

        return infix_stack[0]


    def rpnCommand(self, prompt):
        if prompt in ('swap', 'copy', 'flush'):
            if prompt == 'swap':
                return self.swap()
            elif prompt == 'copy':
                return self.copy()
            else:
                return self.flush()
        elif prompt in ('+', '-', '*', '/', '^'):
            num_1 = float(self.pop())
            num_2 = float(self.pop())
            if prompt == '+':
                result = np.add(num_2, num_1)
            elif prompt == '-':
                result = np.subtract(num_2, num_1)
            elif prompt == '*':
                result = np.multiply(num_2, num_1)
            elif prompt == '/':
                result = np.divide(num_2, num_1)
            else:
                result = np.power(num_2, num_1)
            return self.push(result)
        elif prompt in ('sin', 'cos', 'exp', 'log', 'abs', 'sqrt'):
            num = float(self.pop())
            if prompt == 'sin':
                result = np.sin(num)
            elif prompt == 'cos':
                result = np.cos(num)
            elif prompt == 'exp':
                result = np.exp(num)
            elif prompt == 'log':
                result = np.log(num)
            elif prompt == 'abs':
                result = np.abs(num)
            else:
                result = np.sqrt(num)
            return self.push(result)
        elif prompt in ('pi', 'e'):
            num = np.pi if prompt == 'pi' else np.e
            return self.push(num)
        else:
            self.push(float(prompt))
