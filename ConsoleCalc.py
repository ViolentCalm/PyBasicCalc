import decimal
import sys

 
RESULT = decimal.Decimal()
RESULT2 = decimal.Decimal()

print("  Welcome to the most basic calculator ever!  ")
print("00000000")
print("0XX00XX0")
print("0xx00xx0")
print("00000000")
print("0x0000x0")
print("00x00x00")
print("000xx000")
print("00000000")

fNumb = decimal.Decimal(input("  Enter First Number.  "))
fNumbTwo = decimal.Decimal(input("  Enter Second Number  "))
fOperand = str(input("  Enter Operation + - * /  "))

if fOperand == "+":
    RESULT = (fNumb + fNumbTwo)  
if fOperand == "-":
    RESULT =(fNumb - fNumbTwo) 
if fOperand == "*":
    RESULT = (fNumb * fNumbTwo) 
if fOperand == "/":
    RESULT = (fNumb / fNumbTwo)

print(RESULT)

question = str(input("  Do you want to calculate this against a new number? Y or N  "))




if question == str("y" or "Y"):
    fNumbThree = decimal.Decimal(input("  Enter Third Number  "))
    fOperand2 = str(input(" Enter Second Operation + - * /  "))
    
    if fOperand2 == "+":
        RESULT2 = (RESULT + fNumbThree)  
    if fOperand2 == "-":
        RESULT2 =(RESULT - fNumbThree) 
    if fOperand2 == "*":
        RESULT2 = (RESULT * fNumbThree) 
    if fOperand2 == "/":
        RESULT2 = (RESULT / fNumbThree)

print("  " , RESULT2)

if question != "y" or "Y":
    exit(" Have a nice day! ")


