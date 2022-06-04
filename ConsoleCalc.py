import decimal

# Programmed by ViolentCalm
# violent_calm on Twitter 
# ConsoleCalc V2.0 ( Pre - Release Version ) [ nearly perfect ]
 

# CALCULATOR LOGIC
# First we start off with a while True loop to encapsulate the entire functionality of the program.
# ( hopefully .. )

while True:

    # Defining what fNumb , sNumb etc are, kWestion is defined just as a safety net, 
    # it is probably useless to include, but it is a holdover and will be removed shortly.

    BreakValue = decimal.Decimal()
    fNumb = decimal.Decimal(input("\n  Enter First Number. \n \n " ))
    sNumb = decimal.Decimal(input("\n  Enter Second Number \n \n "))
    fOp = str(input("\n  Enter operation add, sub, mult, div, \n  Make sure to use lowercase! \n \n"))
    kWestion = str()

    # if fOp ( function Operation ) is equal to any of the string values explicitly stated,
    # then execute the code below it, which is to define what the RESULT is, define lastCalculation
    # as the current RESULT for later, print the RESULT with newlines, and ask the question to continue or quit.

    # I do this for every possible function operation because they are all nested within the function operation if statement.

    if fOp == str("add" or " add" or "add " or " add " or "addition" or " addition" or " addition " or "addition "):
        RESULT = fNumb + sNumb

        lastCalculation = RESULT
    
        print("\n" , RESULT , "\n")

        question = str(input("\n  Press 1 to do an entirely new calculation, \n  press 2 to calculate this against a new number, \n  and press 3 to end. \n \n"))
        
        if question == str("1"):
            continue

        if question == str("3"):
            break

        if question == str("2"):
            kWestion = "2"

    if fOp  == str("subtract" or " subtract" or " subtract " or "subtract " or "sub" or " sub" or " sub " or "sub "):
        RESULT = fNumb - sNumb

        lastCalculation = RESULT
    
        print("\n" , RESULT , "\n")

        question = str(input("\n  Press 1 to do an entirely new calculation, \n  press 2 to calculate this against a new number, \n  and press 3 to end. \n \n"))
        
        if question == str("1"):
            continue

        if question == str("3"):
            break

        if question == str("2"):
            kWestion = "2"

    if fOp == str("mult" or " mult" or "mult " or " mult " or "multiply" or " multiply" or "multiply " or " multiply "):
        RESULT = fNumb * sNumb

        lastCalculation = RESULT
    
        print("\n" , RESULT , "\n")

        question = str(input("\n  Press 1 to do an entirely new calculation, \n  press 2 to calculate this against a new number, \n  and press 3 to end. \n \n"))
        
        if question == str("1"):
            continue

        if question == str("3"):
            break

        if question == str("2"):
            kWestion = "2"


    if fOp == str("div" or " div " or " div" or "div " or "divide" or " divide" or " divide " or "divide "):
        RESULT = fNumb / sNumb
        
        lastCalculation = RESULT
    
        print("\n" , RESULT , "\n")
        
        question = str(input("\n  Press 1 to do an entirely new calculation, \n  press 2 to calculate this against a new number, \n  and press 3 to end. \n \n"))
        
        if question == str("1"):
            continue

        # if the question answer is 1, then continue ( loop back to beginning ) , and if it is 3, then break out of this loop? ( might be redundant )
        # im not sure if I needed to break out of a main loop just to access the inner loop in an isolated way or not,
        # regardless it seems to be working at the moment so I wont mess around with it at the moment LOL

        if question == str("3"):
            break

        if question == str("2"):
            kWestion = "2"
    
    # This is the part where kWestion becomes redundant I believe, because this if statement handled that for me without errors.
    # This if question == 2 is also what starts the second While True: loop that handles calculations against previous numbers.
    # A slight alteration to the above calculation formula, just including lastCalculation as the new global variable thingy.
    
    if question == str("2"):

        while True:
     
     

            

                sNumb = decimal.Decimal(input("\n  Enter new number \n \n"))
                fOp = str(input("\n  Enter operation add, subtract, mult, div, \n  Make sure to use lowercase! \n \n"))

    
                if fOp == str("add" or " add" or "add " or " add " or "addition" or " addition" or " addition " or "addition "):
                    RESULT2 = lastCalculation + sNumb
        
                    lastCalculation = RESULT2
        
                if fOp  == str("subtract" or " subtract" or " subtract " or "subtract " or "sub" or " sub" or "sub " or " sub "):
                    RESULT2 = lastCalculation - sNumb
        
                    lastCalculation = RESULT2
        
        
                if fOp == str("mult" or " mult" or "mult " or " mult " or "multiply" or " multiply" or "multiply " or " multiply "):
                    RESULT2 = lastCalculation * sNumb
        
                    lastCalculation = RESULT2
        
                if fOp == str("div" or " div " or " div" or "div " or "divide" or " divide" or " divide " or "divide "):
                    RESULT2 = lastCalculation / sNumb
        
                    lastCalculation = RESULT2
    
                print("\n" , RESULT2 , "\n")

                question = str(input("\n  Press 1 to do an entirely new calculation, \n  press 2 to calculate this against a new number, \n  and press 3 to end. \n \n"))

                if question == str("1"):
                    break

                if question == str("2"):
                    continue
                
                # Just for my own peace of mind, I create a custom BreakValue variable and define it as 1, it only gets created at this moment.
                # After that we break out of this inner while True loop.

                if question == str("3"):
                    BreakValue = decimal.Decimal(1)
                    break

    # Here I check the value of BreakValue just to be sure we are still within the main loop and haven't left the solar system yet,
    # and if we are still alive, break out again to the exit statement.

    if BreakValue == decimal.Decimal(1):
        break

exit("  Have a nice day!  ")