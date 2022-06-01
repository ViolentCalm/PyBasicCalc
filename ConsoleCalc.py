import decimal


RESULT = decimal.Decimal("0")

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

print("  " , RESULT)

input("  Press Enter To Exit")

