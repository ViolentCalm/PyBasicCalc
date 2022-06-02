import decimal
import sys

# Delaring the RESULT datatype early so it can be accessed by the entire program.
 
RESULT = decimal.Decimal()
RESULT2 = decimal.Decimal()

# Terrible attempt at ASCII art

print("  Welcome to the most basic calculator ever!  ")
print("00000000")
print("0XX00XX0")
print("0xx00xx0")
print("00000000")
print("0x0000x0")
print("00x00x00")
print("000xx000")
print("00000000")

# Declaring the datatypes for fNumb / fNumbTwo / fOperand , and taking an input in those types exclusively.

fNumb = decimal.Decimal(input("  Enter First Number.  "))
fNumbTwo = decimal.Decimal(input("  Enter Second Number  "))
fOperand = str(input("  Enter Operation + - * /  "))

# Logic for the operations, 
# if the operation is X, set RESULT equal to the number inputs with the operation applied.

if fOperand == "+":
    RESULT = (fNumb + fNumbTwo)  
if fOperand == "-":
    RESULT =(fNumb - fNumbTwo) 
if fOperand == "*":
    RESULT = (fNumb * fNumbTwo) 
if fOperand == "/":
    RESULT = (fNumb / fNumbTwo)
  
# Print out the first result THEN gather input for the next operation, in the form of a string.

print("  " , RESULT)

question = str(input("  Do you want to calculate this against a new number? Y or N  "))


# If the question is exactly y or Y, ask about the third number and second operation.

if question == str("y" or "Y"):
    fNumbThree = decimal.Decimal(input("  Enter Third Number  "))
    fOperand2 = str(input(" Enter Second Operation + - * /  "))

# Same operation code as before, 
# just defining that RESULT2 is RESULT in addition to the operation happening with fNumbThree.

    if fOperand2 == "+":
        RESULT2 = (RESULT + fNumbThree)  
    if fOperand2 == "-":
        RESULT2 =(RESULT - fNumbThree) 
    if fOperand2 == "*":
        RESULT2 = (RESULT * fNumbThree) 
    if fOperand2 == "/":
        RESULT2 = (RESULT / fNumbThree)

# Print two spaces AND RESULT2, so it is spaced from the edge.
      
print("  " , RESULT2)

# Function thats says " if the answer to the question was NOT yes, then exit with the message " Have a nice day! " 

if question != "y" or "Y":
    exit(" Have a nice day! ")


