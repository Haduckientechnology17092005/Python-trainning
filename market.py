customer_money = float(input("How much money do you have? "))
discount = 0
if customer_money >= 20000000 and customer_money <= 50000000:
    discount = 0.04*customer_money
elif customer_money > 50000000 and customer_money <= 100000000:
    discount = 0.055*customer_money
elif customer_money < 20000000:
    discount = 0
else:
    discount = 0.065*customer_money
money_must_be_checked = customer_money - discount
print("money checked: ", money_must_be_checked)
print("discount: ",discount)