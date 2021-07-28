def taxCalculate(totalPrice):
    result = str(totalPrice+(totalPrice*0.07))+" Baht"
    return result
price = int(input("Your price:"))
print(taxCalculate(price))