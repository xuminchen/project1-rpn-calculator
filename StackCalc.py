#class StackCalc: a class that extends (inherit) the functionalities
# of the class Stack 

from Stack import *
import copy
import numpy as np # if you need sin, just do np.sin, etc.

class StackCalc(Stack):    
    def __init__(self):        
      super().__init__() 
      
