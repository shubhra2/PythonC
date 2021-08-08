class ReadNumber:    
    readnum = 0
    try:
        readnum = int(input("Enter the number of elements to input: "))
    except TypeError:
        print("Please enter a number.")
    numbers = []
    while readnum > 0:
        n = float(input("Enter the numbers : "))
        numbers.append(n)
        readnum -= 1


count = ReadNumber.numbers

result = [str(elem) + " : Even" if elem %
          2 == 0 else str(elem) + " : Odd" for elem in count]
print(result)
