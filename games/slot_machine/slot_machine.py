MAX_LINES = 3   #capitals becuase (global constant) - convention in python - this is constant value, something that won't change.
MAX_BET = 100
MIN_BET = 1

def deposit():       # function respoinsibile for getting user input.
    while True:     # continously ask user to enter a deposit amount until they give valid amount.
        amount = input("What would you like to deposit? $")
        if amount.isdigit(): # is digit will tell us if this is a valid whole number --> if it's negative it won't be true #method to use on strings to check if number is valid.
            amount = int(amount) # this converts the above to integer AFTER it's been confirmed above that it's actually a number
            if amount > 0:
                break
            else:
                print("Amount must be greated than 0.")
        else:
            print("Please enter a number.")

    return amount

deposit() # will execute the function

def get_number_of_lines():
    while True:     
        lines = input("Enter the number of lines to bet on? (1-" + str(MAX_LINES) +")? ") #added max lines inside the string, convert it into a string
        if lines.isdigit(): # is digit will tell us if this is a valid whole number --> if it's negative it won't be true #method to use on strings to check if number is valid.
            lines = int(lines) # this converts the above to integer AFTER it's been confirmed above that it's actually a number
            if 1 <= lines <= MAX_LINES: # if my line is greater to or equal to 1, and is less than or equal to the maximum line
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")

    return lines    

def get_bet():
    while True:     # continously ask user to enter a deposit amount until they give valid amount.
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit(): # is digit will tell us if this is a valid whole number --> if it's negative it won't be true #method to use on strings to check if number is valid.
            amount = int(amount) # this converts the above to integer AFTER it's been confirmed above that it's actually a number
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount
    

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

main()      # The main function in Python acts as the point of execution for any program    