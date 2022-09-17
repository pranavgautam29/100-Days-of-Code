from turtle import clear, clearscreen
bids = {}
anymore_bidders = True
while anymore_bidders:
    name = input("Enter your name:")
    bid = int(input("Enter your bid:"))
    bids[name] = bid
    ques = input("Are there any more bidders(yes/no):")
    if ques == 'no':
        anymore_bidders = False
    clear()
highest_bid = 0
for biders in bids:
    temp = bids[biders]
    if temp > highest_bid:
        highest_bid = temp
        winner = biders
print("The winner is",winner,"with a bid of $",highest_bid)

