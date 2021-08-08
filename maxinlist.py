class Readnum:
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

num = Readnum.numbers
num.sort()
print("Largest number in list {} is {}".format(num, num[-1]))
print("Largest number in list {} is {}".format(num, max(num)))
mx = num[0]
for i in range(1, len(num)):
    if mx < num[i]:
        mx = num[i]
print("Largest number in list {} is {}".format(num, mx))
