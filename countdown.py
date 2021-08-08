import time

def ReadNumber(num):
    check = False
    positive_num = ""
    while check != True:
        positive_num = input(num)
        try:
            positive_num = int(positive_num)
            if (positive_num <= 0):
                check = False
            else:
                check = True
        except:
            print("Enter Integer Number")
    return positive_num

countdown = ReadNumber("Enter any positive integer to start the countdown: ")
print(countdown)
while(countdown > 0):
    time.sleep(1)
    countdown -= 1
    print(countdown, end="\n")