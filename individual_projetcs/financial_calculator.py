#Financial Calculator
#Overview
"""Create a program that completes the following basic financial calculations:

How long it will take to save for a goal based on a weekly or monthly deposit
Compound Interest Calculator
Budget Allocator (use set percentages to divide an income into spending categories like savings, entertainment, and food)
Sale Price Calculator (apply discounts to prices)
Tip Calculator"""
#Project Steps:
"""Create a main function that will run the user interface
Using project decomposition to figure out what other functions you need and how they interact with each other
Implement at least one inner function within one of your main calculation functions. This inner function should handle a specific sub-task of the main function.
Ensure that your inner function demonstrates proper scope usage, accessing va   riables from its outer function if necessary.
Comment your code to explain the purpose and functionality of your inner function.
Create your functions
Have at least 2 people test your code to make sure it works"""

#Goal Function
def savings_goal():
    #While loop stupid proof
    while True:
        #Goal is set to user input for save goal
        goal_input = input("Enter your savings goal: ")
        if goal_input.isdigit():
            goal = int(goal_input)
            if goal > 0:
                break
            else:
                print("Goal must be greater than 0.")
        else:
            print("Please enter numbers only.")
        #While True Stupid proof
       # User input to choose if they want to save weekly or monthly
    while True:#Stupid proof loop
        week_or_mon = input("Do you want to save weekly or monthly? ").lower()
        #IF week_or_mon is 'weekly'
        if week_or_mon == 'weekly' or week_or_mon == "monthly":
            break
        else:
            print("Please enter 'weekly' or 'monthly'.")
    if week_or_mon == 'weekly':
            #While loop stupid proof
            def calculate_weeks(goal):
                while True:
                    weekly_input = input("Please enter your weekly savings amount: ")
                    if weekly_input.replace(".", ", 1").isdigit():
                        weekly_savings = float(weekly_input)
                        if weekly_savings > 0:
                            return goal / weekly_savings
                        else:
                            print("Weekly savings must be greater than 0.")
                    else:
                        print("Please enter numbers only.")
            #Calculate time to reach goal with weekly savings
            print("It will take you", calculate_weeks(goal), "weeks to reach your savings goal.")
    
        #ELSE IF week_or_mon is 'monthly
    elif week_or_mon == 'monthly':
            #While loop stupid proof
            def calculate_months(goal):
                while True:
                    monthly_input = input("Please enter your monthly savings amount: ")
                    if monthly_input.replace(".", ", 1").isdigit():
                        monthly_savings = float(monthly_input)
                        if monthly_savings > 0:
                            return goal / monthly_savings
                        else:
                            print("Monthly savings must be greater than 0.")
                    else:
                        print("Please enter numbers only.")                                                                                                                                                             
            #Calculate time to reach goal with monthly savings
            print("It will take you", calculate_months(goal), "months to reach your savings goal.") 
#Calculate compound interest
def compound_interest():
    #While loop stupid proof
    while True:
        #Start amount is set to a float input
        start_input = input("Enter the starting amount: ")
        if start_input.replace(".", "", 1).isdigit():
            start_amount = float(start_input)
            if start_amount > 0:
                break
            else:
                print("Starting amount must be greater than 0.")
        else:
            print("Please enter numbers only.")
    #While loop stupid proof
    while True:
        #rate is set to a float input asking for interest rate
        rate_input = input("Enter the interest rate (as a percentage): ")
        if rate_input.replace(".", "", 1).isdigit():
            rate = float(rate_input)
            if rate > 0:
                break
            else:
                print("Interest rate must be greater than 0.")
        else:
            print("Please enter numbers only.")
        #While loop stupid proof
    while True:
        #years is set to a float input asking for number of years
        years_input = input("Enter the number of years: ")
        if years_input.replace(".", "", 1).isdigit():
            years = float(years_input)
            if years > 0:
                break
            else:
                print("Years must be greater than 0.")
        else:
            print("Please enter numbers only.")

        #Calculate compound interest
        def calc_com_int():
            #amount is set to startmount * (1 + rate / 100) ** years
            amount = start_amount * (1 + rate / 100) ** years
            #compount interest is set to amount - start_amount
            compound_interest = amount - start_amount
            #Return compound interest
            return compound_interest\
            #print compound interest
        print("Your compound interest is:", calc_com_int())
        #print("Total money gained")
        print("The total amount after", years, "years is:", start_amount + calc_com_int())
#Budget Allocator Function
def budget_allocator():
    #while loop stupid proof
    while True:
        #categories for budget
        categories_input = input("Enter how many categories do you have: ")
        if categories_input.isdigit():
            categories = int(categories_input)
            if categories > 0:
                break
            else:
                print("Categories must be greater than 0.")
        else:
            print("Please enter numbers only.")
            #While loop stupid proof
    while True:
        #budget input
        budget_input = input("Enter your monthly income: ")
        if budget_input.replace(".", "", 1).isdigit():
            budget = float(budget_input)
            if budget > 0:
                break
            else:
                print("Budget must be greater than 0.")
        else:
            print("Please enter numbers only.")
    #allocation dictionary
    allocation = {}
    #for loop to get all category allocations
    for i in range(categories):
        #category name input
        category_name = input(f"Enter the name of category {i + 1}: ")
        #while loop stupid proof
        while True:
            percentage_input = input(f"Enter the percentage for {category_name}: ")
            if percentage_input.replace(".", "", 1).isdigit():
                percentage = float(percentage_input)
                if 0 <= percentage <= 100:
                    break
                else:
                    print("Percentage must be between 0 and 100.")
            else:
                print("Please enter numbers only.")
        #allocation calculation
        allocation[category_name] = budget * (percentage / 100)
        #print statement showing your budget allocation.
    print("Your budget allocation is:")
    #for loop to print each category and its allocated amount
    for category, amount in allocation.items():
        #format print statement showing category and amount
        print(f" - {category}: ${amount:.2f}")
#Sale Price Calculator Function
def sale_price():
    #While loop stupid proof
    while True:
            #original price input asking for original price
        original_price_input = input("Enter the original price: ")
        if original_price_input.replace(".", "", 1).isdigit():
            original_price = float(original_price_input)
            if original_price > 0:
                break
            else:
                print("Original price must be greater than 0.")
        else:
            print("Please enter numbers only.")
    #while loop stupid proof
    while True:
        #percentage input asking for sale percent
        percent_off_input = input("Enter the percentage off: ")
        if percent_off_input.replace(".", "", 1).isdigit():
            percent_off = float(percent_off_input)
            if 0 <= percent_off <= 100:
                break
            else:
                print("Percentage off must be between 0 and 100.")
        else:
            print("Please enter numbers only.")
    #sale price is set to original price times (1 - percent_off / 100)
    sale_price = original_price * (1 - percent_off / 100)
    #format print statement showing saleprice
    print(f"The sale price is: ${sale_price:.2f}")
#Tip Calculator Function
def tip_calculator():
    #while loop stupid proof
    while True:
        #Bill is set to input aking for the bill
        bill_input = input("Enter the bill amount: ")
        if bill_input.replace(".", "", 1).isdigit():
            bill = float(bill_input)
            if bill > 0:
                break
            else:
                print("Bill amount must be greater than 0.")
        else:
            print("Please enter numbers only.")
    #while loop stupid proof
    while True:
        #percent tip is set to input asking for percent tip.
        percent_tip_input = input("Enter the tip percentage: ")
        if percent_tip_input.replace(".", "", 1).isdigit():
            percent_tip = float(percent_tip_input)
            if percent_tip >= 0:
                break
            else:
                print("Tip percentage must be 0 or greater.")
        else:
            print("Please enter numbers only.")
    #tip is set to bill times (percent_tip / 100)
    tip = bill * (percent_tip / 100)
    #format print statement showing tip
    print(f"The tip amount is: ${tip:.2f}")
#Main Loop Function
def main_loop():
    #Display the main menu
    print("Financial Calculator Opened")
    #Display options
    print("1. Savings Goal Calculator")
    print("2. Compound Interest Calculator")
    print("3. Budget Allocator")
    print("4. Sale Price Calculator")
    print("5. Tip Calculator")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        savings_goal()
    elif choice == "2":
        compound_interest()
    elif choice == "3":
        budget_allocator()
    elif choice == "4":
        sale_price()
    elif choice == "5":
        tip_calculator()
    elif choice == "6":
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please try again.")
main_loop()
