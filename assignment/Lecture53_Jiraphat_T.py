def taxCalculate(totalPrice):
    result = f"Vat included price: {totalPrice+(totalPrice*0.07)} baht"
    return result
oriPrice = int(input("Your original price: "))
print(taxCalculate(oriPrice))