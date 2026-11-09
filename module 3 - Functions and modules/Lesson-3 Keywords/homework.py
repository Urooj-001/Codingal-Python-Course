def calculate_due(bill, paid):
    due = paid - bill
    return due

bill = float(input("Enter the total bill: "))
paid = float(input("Enter the amount paid: "))

change = calculate_due(bill, paid)

print("The shopkeeper should return:", change)