def change():
    expense = float(input("Type in the expense: "))
    money = float(input("Type in the money recieved: "))

    change = money - expense

    dollars = int(change)
    cents = round((change - dollars) * 100)


    print("\n\nChange:\n\nf")
    print("Dollars:")
    print(dollars)
    print("Cents")
    print(cents)

change()

