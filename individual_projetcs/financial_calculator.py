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
        goal = int(input("Enter your savings goal: "))
        if goal 
       # User input to choose if they want to save weekly or monthly
        week_or_mon = input("Do you want to save weekly or monthly? ")
        #IF week_or_mon is 'weekly'
        if week_or_mon == 'weekly':
            def calculate_weeks(goal):
                weekly_savings = float(input("Enter your weekly savings amount: "))
                weeks = goal / weekly_savings
                return weeks
            print("It will take you", calculate_weeks(goal), "weeks to reach your savings goal.")
        #ELSE IF week_or_mon is 'monthly
        elif week_or_mon == 'monthly':
            def calculate_months(goal):
                monthly_savings = float(input("Enter your monthly savings amount: "))
                months = goal / monthly_savings
                return months
            #Calculate time to reach goal with monthly savings
            print("It will take you", calculate_months(goal), "months to reach your savings goal.") 
#Calculate compound interest
def compound_interest():
    #Start amount is set to a float input
    start_amount = float(input("Enter your starting amount: "))
    #rate is set to a float input asking for interest rate
    rate = float(input("Enter the interest rate: "))
    #years is set to a float input asking for number of years
    years = float(input("Enter the number of years: "))
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
    #categories for budget
    categories = input("Enter how many categories do you have: ")
    #Convert categories to integer
    categories = int(categories)
    #budget input
    budget = float(input("Enter your monthly income: "))
    #allocation dictionary
    allocation = {}
    #for loop to get all category allocations
    for i in range(categories):
        #category name input
        category_name = input("Enter the name of category {}: ".format(i + 1))
        #percentage input
        percentage = float(input("Enter the percentage for {}: ".format(category_name)))
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
    #original price input asking for original price
    original_price = float(input("Enter the original price: "))
    #percentage input asking for sale percent
    percent_off = float(input("Enter the percentage off: "))
    #sale price is set to original price times (1 - percent_off / 100)
    sale_price = original_price * (1 - percent_off / 100)
    #format print statement showing saleprice
    print(f"The sale price is: ${sale_price:.2f}")
#Tip Calculator Function
def tip_calculator():
    #Bill is set to input aking for the bill
    bill = float(input("Enter the bill amount: "))
    #percent tip is set to input asking for percent tip.
    percent_tip = float(input("Enter the tip percentage: "))
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
