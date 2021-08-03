def login():
    username = input("Username :")
    password = input("Password :")
    if username == "admin" and password == "1234":
        print("---Login success---")
        return True
    else:
        print("---Login failed---")
        return False

def showMenu():
    print("-------iShop-------")
    print("1. Vat calculator")
    print("2. Price calculator")

def menuSelect():
    userSelected = int(input(">>"))
    return userSelected

def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice +(totalPrice*vat/100)
    return result

def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1+price2)

if login():
    showMenu()
    process = menuSelect()
    if process == 1:
        print("Price: ",vatCalculate(int(input("Please enter your total price : "))))
    elif process == 2:
        print(f"Total(Vax included) : {priceCalculate()}")