"""
Program: programmer_toolkit.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: Demonstrate if statements with a sign up option
"""


# function that gets user input
def sign_up_for_toolkit_box():
    # prompt the user for instructions
    print('Please sign up for Programmer\'s Toolkit Monthly Subscription Box')
    print('Toolkit Options:\n-Platinum\n-Gold\n-Silver\n-Bronze\n-Free Trial')
    # get the user input
    toolkit_choice = input('Please Select a Toolkit Option:')
    # call return string cost of box
    toolkit_cost = return_string_cost_of_box(toolkit_choice)
    # print return value
    return f'Toolkit: {toolkit_choice} cost: {toolkit_cost}'


def return_string_cost_of_box(level):
    # if statement to return cost of toolkit selected
    if level == "Platinum":
        return "$60.00"
    elif level == "Gold":
        return "$50.00"
    elif level == "Silver":
        return "$40.00"
    elif level == "Bronze":
        return "$30.00"
    else:
        return "$0.00"


if __name__ == '__main__':
    print(sign_up_for_toolkit_box())
