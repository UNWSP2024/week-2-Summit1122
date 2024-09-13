def calculate_total_purchase():
    # A customer in a store is purchasing five items.
    # Write a program that asks for each item,
    item_1 = float(input("What is the cost of your first item?: "))
    item_2 = float(input("What's the second?: "))
    item_3 = float(input("The 3rd?: "))
    item_4 = float(input("The 4th?: "))
    item_5 = float(input("The 5th?: "))
    # then displays the subtotal of the sale,
    subtotal = (item_1 + item_2 + item_3 + item_4 + item_5)
    print('Subtotal: ')
    print(subtotal)
    # the amount of sales tax, and the total.
    # Assume the sales tax is 7 percent.
    sales_tax = subtotal * 0.07
    print('Sales Tax: ')
    print(sales_tax)
    #total
    print('Total:')
    print( round(sales_tax + subtotal, 2)) # to make it look normal I learned about the round command



calculate_total_purchase()