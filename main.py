import subscription

my_subs = subscription.Inventory()

userChoices = "(a) add, (r) remove (t) total (p) print (e) exit"
userInput = ""
while userInput != "e":
    userInput = input(userChoices+"\n")
    if userInput == "a":
        subType = input("monthly(m), yearly(y) or one-time(ot) subscription?:")
        subName = input("What is name of subscription:")
        subCost = int(input("What is the cost:"))
        subDate = "none"
        if subType == "m" or subType == "y":
            subDate = input("When does it renew:")
        sub = subscription.Subscription(subName, subCost, subDate)
        if subType == "m":
            sub = subscription.Monthly(subName, subCost, subDate)
        elif subType == "y":
            sub = subscription.Yearly(subName, subCost, subDate)
        added = my_subs.add(sub)
        if added:
            print(subName + " Added")
        else:
            print(subName + " is already in your list")
    elif userInput == "r":
        subName = input("What subscription do you want to remove")
        removed = my_subs.remove(subName)
        if removed:
            print(subName + " Removed")
        else:
            print(subName + " is not in your list")
    elif userInput == "t":
        my_subs.get_total_cost()
    elif userInput == "p":
        my_subs.print_subs()