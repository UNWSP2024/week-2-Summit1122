    # Luis Amador
    # 9/12/24
    # Title: Cost of groceries
def average_age():
    # Get User Input
    friend_1 = int(input("Enter 1st friend's age: "))
    friend_2 = int(input("Enter 2nd's: "))
    friend_3 = int(input("Enter 3rd's: "))
    friend_4 = int(input("Enter 4th's: "))
    friend_5 = int(input("Enter 5th's: "))

    # Sum ages
    prompt_1 = "Sum of friend's ages:" #simple set up for showing what the number given represents
    sums = (friend_1 + friend_2 + friend_3 + friend_4 + friend_5)

    # Average the ages
    prompt_2 = "Average of the ages:"
    Avg_1 = ((friend_1 + friend_2 + friend_3 + friend_4 + friend_5)/5)
    # Print the results
    print(prompt_1)
    print(sums)
    print(prompt_2)
    print(Avg_1)
# Line which calls the above function.
average_age()