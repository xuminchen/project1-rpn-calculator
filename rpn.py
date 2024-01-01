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
choice=input("Your choice: ")


mystack=StackCalc()
myqueue=Queue()


if choice=="1": #////////////// Simple RPN calculator

    print("Welcome to the simple RPN calculator (enter 'quit' to quit)");
    while True:
        print("----------------------------------------------------------")
        print(mystack)
        prompt=input(">")    
        if prompt=="quit": break
        mystack.rpnCommand(prompt)



if choice=="2": #////////////// Fancy RPN calculator

    print("Welcome to the fancy RPN calculator (enter 'quit' to quit)");
    while True:
        print("----------------------------------------------------------")
        print(mystack)
        if not myqueue.isEmpty(): #Display both postfix and infix
            print("Postfix: "+str(myqueue))
            print("Infix: ",StackCalc.postfix2infix(myqueue))
        prompt=input(">")    
        if prompt=="quit": break
        mystack.rpnCommand(prompt)
        if prompt!="flush":
            myqueue.enqueue(prompt)
        else:
            myqueue.flush()

        
if choice=="3": #////////////// Fancier RPN calculator

    print("Welcome to the fancier RPN calculator (enter 'quit' to quit)");















print("Thanks for using the RPN calculator")
