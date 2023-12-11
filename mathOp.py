import random

# List of operations
# Math game that generates random math questions and gives user one chance to get it correct if correct creates another math question if incorrect run out of lives

operations = ["+", "-", "/", "*"]               # Create list to call different operations
lives = 1                                       # Declare lives

def ranNum(start, end):                         # function to create random number 
    return random.randint(start, end)           # return random integer 

def create_Equation():                          # Function to create equation
    randomNum1 = ranNum(1, 100)                 # Random function 1 to get first number in equation between 1 and 100
    randomNum2 = ranNum(1, 100)                 # Random function 2 to get first number in equation between 1 and 100
    ranOp = ranNum(0, 3)                        # variable to get random number between 0 and 3 to pass use in when accessing and array and get a random operation

    if operations[ranOp] == "+":
        soln = round(randomNum1 + randomNum2)   # if operation is this tell it what to perform
    elif operations[ranOp] == "*":
        soln = round(randomNum1 * randomNum2)   # if operation is this tell it what to perform
    elif operations[ranOp] == "-":
        soln = round(randomNum1 - randomNum2)   # if operation is this tell it what to perform
    elif operations[ranOp] == "/":
        soln = round(randomNum1 / randomNum2) if randomNum2 != 0 else None
    else:
        soln = None

    print(f"What is {randomNum1} {operations[ranOp]} {randomNum2} = ?")
    # Print random equation 
    getValue = input("What is your guess: ")      # variable to get and store input from user 

    try:                                          # try section 
        getValue = float(getValue)                # make getValue into float 
        if soln is not None and getValue == soln:
            print("Correct")
            create_Equation()                     # if solution is equal print correct and re run create equation to guess again
        else:
            print("Close!")                       # else close and run prompts to end program 
            print("The correct solution is", soln)
            global lives
            lives -= 1
            print("Lives remaining:", lives)
            if lives > 0:
                create_Equation()
            else:
                print("Out of lives. Game over.")

    except ValueError:
        print("Invalid input, Please enter a number")

# Call the function to create an equation
create_Equation()
