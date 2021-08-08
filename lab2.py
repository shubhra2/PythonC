
def readnum() :
    nm = float(input("Enter Number(s) : "))
    return nm

def add() :
    numarr = []
    for i in range(2) :
        n1 = readnum()
        numarr.append(n1)
    print("{} + {} = {}".format(numarr[0], numarr[1], numarr[0] + numarr[1]))

def maxmin() :
    maxminnumary = []
    for i in range(3) :
        n2 = readnum()
        maxminnumary.append(n2)
        
    print("The Maximum and minimun of {} numbers are : {}, {} respectively." .format(maxminnumary, max(maxminnumary), min(maxminnumary)))

def palindrome():
    str = input("Enter a string : ")
    strrev = ''.join(reversed(str))
    if(str == strrev):
        print("{} is a palindrome.".format(str))
    else:
        print("{} is not a palindrome.".format(str))

def factorialnonfunc():
    import math
    num = int(readnum())
    print("The factorial of {} is : {}".format(num, math.factorial(num)))

def factorialfunc():
    def factorial(num1):
        if num1 == 1:
            return 1
        else:
            return (num1 * factorial(num1-1))
    print(factorial(int(readnum())))

def selection():
    
    sel = int(input('''
    choose from the following : 
    1. Addition of two numbers.
    2. Maximum and minimum from three numbers
    3. Check wether a given string is a palindrome or not
    4. Factorial of a number without using a function
    5. Factorial of a number using a function
    6. Exit
    '''))
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
        print("\n\nPlease choose from 1 to 6.")
        selection()
# selection()
