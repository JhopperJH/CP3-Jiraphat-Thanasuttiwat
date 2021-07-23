import time
mathBookCost = 320
phyBookCost = 250
chemBookCost = 270
bioBookCost = 400
engBookCost = 300
cost = [mathBookCost, phyBookCost, chemBookCost, bioBookCost, engBookCost]
bookList = ["1","2","3","4","5"]
bookName = ["Calculus Hardcore mode", "Physics for Engineering", "Chemistry for Scientists", "Extra Biology in Laboratory", "English Experience for work"]
selectedBook = []
listcost = []
eachBookAmount = []

def Chulabook():
    user = input("Username : ")
    password = input("Password : ")
    if user == "ComSciStudent" and password == "1234":
        print("\t\tLogin succeed")
        print("\t--- Welcome to Chulabook ---")
        print("These are available books for Com-Sci students")
        for num,thebook,eachcost in zip(bookList, bookName, cost):
            print(f"{num}.{thebook} :\t\t {eachcost} THB")
        print("\t----------------------------")
        time.sleep(0.5)
        selected = input(f"Please enter the booknumber(No.{bookList[0]} to {bookList[-1]}) those you would like to purchase : ")
        for num, thebook, eachcost in zip(bookList, bookName, cost):
            if num in selected:
                try:
                    amount = int(input(f"How many of \'{thebook}\' would you like to buy : "))
                    selectedBook.append(thebook)
                    listcost.append(eachcost)
                    eachBookAmount.append(amount)
                except:
                    print("Oops!  That was no valid number.  Try order again...")
                    break
        if selectedBook != []:
            total = 0
            time.sleep(0.5)
            print("\t    --- Cash Receipt ---")
            for thebook, eachcost, amount in zip(selectedBook, listcost, eachBookAmount):
                print(f"{thebook} :\t\t{eachcost * amount} THB")
                total += (eachcost * amount)
            print("\t----------------------------")
            print(f"Total :\t\t\t\t\t{total}THB")
        else:
            print("Wish you come back to see us again ^-^")
                
    else:
        print("Login failed, Please enter again")
        Chulabook()
Chulabook()