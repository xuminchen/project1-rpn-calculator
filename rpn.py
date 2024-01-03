import numpy as np

from StackCalc import *
from Queue import *
from numpy import *  # if you need sin, just do sin, etc.
import matplotlib.pyplot as plt

# Menu
print()
print("===============================================")
print("================= Project 1 ===================")
print("===============================================")
print("|                                             |")
print("|         1-Simple  RPN calculator            |")
print("|         2-Fancy   RPN calculator            |")
print("|         3-Fancier RPN calculator            |")
print("|                                             |")
print("===============================================")
print()
choice = input("Your choice: ")

mystack = StackCalc()
myqueue = Queue()

if choice == "1":  # ////////////// Simple RPN calculator

    print("Welcome to the simple RPN calculator (enter 'quit' to quit)");
    while True:
        print("----------------------------------------------------------")
        print(mystack)
        prompt = input(">")
        if prompt == "quit": break
        mystack.rpnCommand(prompt)

if choice == "2":  # ////////////// Fancy RPN calculator

    print("Welcome to the fancy RPN calculator (enter 'quit' to quit)");
    while True:
        print("----------------------------------------------------------")
        print(mystack)
        if not myqueue.isEmpty():  # Display both postfix and infix
            print("Postfix: " + str(myqueue))
            print("Infix: ", StackCalc.postfix2infix(myqueue))
        prompt = input(">")
        if prompt == "quit": break
        mystack.rpnCommand(prompt)
        if prompt != "flush":
            myqueue.enqueue(prompt)
        else:
            myqueue.flush()

if choice == "3":  # ////////////// Fancier RPN calculator

    print("Welcome to the fancier RPN calculator (enter 'quit' to quit)");
    while True:
        print("----------------------------------------------------------")
        # print(mystack)
        tmp_stack = []
        if not myqueue.isEmpty():  # Display both postfix and infix
            infix = StackCalc.postfix2infix(myqueue)
            print(f"Postfix: {myqueue}")
            print(f"Infix: {infix}")
        prompt = input(">")
        if prompt == "quit": break
        # mystack.rpnCommand(prompt)

        if prompt not in ("flush", "run", "plot"):
            myqueue.enqueue(prompt)
        else:
            import re

            if prompt == "run":
                if myqueue.find("x"):
                    x = input("Enter x value: ")
                    infix_result = eval(re.sub('x', str(x), infix))  # replace x with input value
                else:
                    infix_result = eval(infix)
                    x = None
                postfix_result = StackCalc.evaluate_postfix(myqueue, x)
                print(f"Solution using postfix: {postfix_result}")
                print(f"Solution using infix: {infix_result}")
            elif prompt == "plot": # plot figure in canvas with given xmin, xmax, nbp which split by space
                plot_args = input("Enter values of xmin, xmax, nbp: ")
                xmin = float(plot_args.split(" ")[0])
                xmax = float(plot_args.split(" ")[1])
                nbp = int(plot_args.split(" ")[2])
                x = np.linspace(xmin,xmax,nbp)
                y = eval(infix)
                plt.plot(x,y)
                plt.title(f"f(x)={infix}")
                plt.xlabel("x")
                plt.ylabel("f(x)")
                plt.show()
            else:
                myqueue.flush()
print("Thanks for using the RPN calculator")
