# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 13:16:45 2023

@author: mo2a
"""
from calc import *
    
def Calculator ():
    print ("1.Add")
    print ("2.Subtract")
    print ("3.Multiply")
    print ("4.Divide")
    
    Choice = input("Please Enter your Choice (1/2/3/4) : ")
    
    if Choice == '1':
        Num1 , Num2 = take_input()
        print (Num1 , "+", Num2 , "= " , add(Num1,Num2))
        
    elif Choice == '2':
        Num1 , Num2 = take_input()
        print (Num1 , "-", Num2 , "= " , subtract(Num1,Num2))
        
    elif Choice == '3':
        Num1 , Num2 = take_input()
        print (Num1 , "*", Num2 , "= " , multiply(Num1,Num2))
        
    elif Choice == '4':
        Num1 , Num2 = take_input()
        print (Num1 , "/", Num2 , "= " , divide(Num1,Num2))
        
    else : print ("*** Wrong Input ! ***")
    
    Need = input("Do You need another operation ? Yes/No : ")
    if Need == "yes":
        Calculator()
    else : 
        print ("Thank You!")
    
Calculator()   
