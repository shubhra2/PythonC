import streamlit as st
import math
import random
choices = list(range(100))
random.shuffle(choices)
r = choices.pop()
def add() :
    numarr = []
    for i in range(2) :
        n1 = st.number_input('Enter Number(s) : ', key=str(r))
        numarr.append(n1)
    st.write("{} + {} = {}".format(numarr[0], numarr[1], numarr[0] + numarr[1]))

def maxmin() :
    maxminnumary = []
    for i in range(3) :
        n2 = st.number_input('Enter Number(s) : ', key=str(r))
        maxminnumary.append(n2)
        
    st.write("The Maximum and minimun of {} numbers are : {}, {} respectively." .format(maxminnumary, max(maxminnumary), min(maxminnumary)))

def palindrome():
    str = st.text_input("Enter a string : ")
    strrev = ''.join(reversed(str))
    if(str == strrev):
        st.write("{} is a palindrome.".format(str))
    else:
        st.write("{} is not a palindrome.".format(str))

def factorialnonfunc():
    num = int(st.number_input('Enter Number(s) : ', key=str(r)))
    st.write("The factorial of {} is : {}".format(num, math.factorial(num)))

def factorialfunc():
    def factorial(num1):
        if num1 == 1:
            return 1
        else:
            return (num1 * factorial(num1-1))
    st.write(factorial(int(st.number_input('Enter Number(s) : ', key=str(r)))))

def selection():
    seldict = {
        1:'Addition of two numbers.', 
        2:'Maximum and minimum from three numbers', 
        3:'Check wether a given string is a palindrome or not', 
        4:'Factorial of a number without using a function', 
        5:'Factorial of a number using a function'
    }
    st.subheader("Choose from the following : ")
    sel = st.selectbox('', options= (1, 2, 3, 4, 5), format_func=lambda x: seldict.get(x),key=str(r))
    st.write(sel)
    while sel < 7:
        if(sel == 1):
            add()
            selection()
            break
        elif(sel == 2):
            maxmin()
            selection()
            break
        elif(sel == 3):
            palindrome()
            selection()
            break
        elif(sel == 4):
            factorialnonfunc()
            selection()
            break
        elif(sel == 5):
            factorialfunc()
            selection()
            break
        elif(sel == 6):
            break
    else:
        st.write("\n\nPlease choose from 1 to 6.")
        selection()
selection()