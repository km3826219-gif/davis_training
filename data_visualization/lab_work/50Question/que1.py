
price = float(input("Enter total bill amount: "))
discount_percent = float(input("Enter discount percentage: "))
discount_amount = (price * discount_percent) / 100
final_amount = price - discount_amount
print("Discount Amount:", discount_amount)
print("Final Bill Amount:", final_amount)