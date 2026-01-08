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
Ensure that your inner function demonstrates proper scope usage, accessing variables from its outer function if necessary.
Comment your code to explain the purpose and functionality of your inner function.
Create your functions
Have at least 2 people test your code to make sure it works"""

#Goal Function
def savings_goal_calculator():
    #While loop stupid proof
        #Goal is set to user input for save goal
        goal = float(input("Enter your savings goal: "))
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
            #Calculate time to reach goal with monthly savings
            def calculate_months(goal):
                monthly_savings = float(input("Enter your monthly savings amount: "))
                months = goal / monthly_savings
                return months
            print("It will take you", calculate_months(goal), "months to reach your savings goal.")
savings_goal_calculator()
#Compound Interest Calculator Function
def com_int_calc():
#Budget Allocator Function
#Sale Price Calculator Function
#Tip Calculator Function
#Main run function
