# ask user to input their purchase amount as float
# if the purchase is 100 cedis or more apply 20% discount and print amount to pay
#if the purchase is 50 cedis or more apply 10% discount and print amount to pay
#if the purchase is less than 50 cedis apply no discount and print amount to pay

purchase_amount = float(input("enter your purchase amount\n"))
if purchase_amount >= 100:
     discount = 0.2 * purchase_amount
     amount_to_pay = purchase_amount - discount
     print(f"you have to pay:{amount_to_pay}")
elif purchase_amount >= 50:
     discount = 0.1 *purchase_amount
     amount_to_pay = purchase_amount - discount
     print(f"you to pay: {amount_to_pay}")
else:
     print(f"you have to pay:{purchase_amount}")