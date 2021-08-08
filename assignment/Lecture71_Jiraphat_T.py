menulist = []
pricelist = []

def showbill():
    print("My food".center(27, '-'))
    for number in range(len(menulist)):
        print(f"{number + 1}. {menulist[number]}\t {pricelist[number]} THB")
        total = sum(pricelist[0:(number+1)])
    print("".center(27, '-'))
    print(f"Total: {total} THB")

print("This is a program using for adding foodlist and it's price")
while True:
    menuName = input('Please enter menu (If you would like to stop, please enter "Exit"): ')
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("The price: "))
        menulist.append(menuName.capitalize())
        pricelist.append(menuPrice)
showbill()