actual_cost = float(input("Enter the actual cost of the iteam:"))
selling_price = float(input("Enter the selling price:"))
if selling_price > actual_cost:
    print("Your in profit!",selling_price - actual_cost)
else:
    print("Your in loss!",actual_cost - selling_price)
