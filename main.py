import operator

Auct = {}
def bidprice():
    choice = input("Do you want to bid, yes or no: ").lower()
    if choice in ("y","yes"):
        print('\n'*30)
        for i in range(1):
           biddername = input("Please enter your name: ")
           bidprices = int(input("please enter the bid price: "))
           Auct[biddername.title()] = bidprices
        bidprice()
    elif choice in ("no","n"):
        maximumbidder = max(Auct.items(), key=operator.itemgetter(1))[0]
        maximumbid=max(Auct.items(), key=operator.itemgetter(1))[1]
        print(f"the winner is: {maximumbidder}, with the highest bid: {maximumbid}")
        print(Auct)
    else:
        print("please enter a valid value")
        bidprice()

bidprice()
