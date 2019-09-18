x=int(input("Enter the number: "))
try:
    quotient = x//0
    remainder = x%0
        print (quotient)
except ZeroDivisionError:
    print ("You can't divide by zero!");