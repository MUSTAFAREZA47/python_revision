print("Secret Auction Program")

bids = {}

bidding = True
while bidding:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    more_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_bids == "no":
        bidding = False
        for key, value in bids.items():
            if value == max(bids.values()):
                print(f"The winner is {key} with a bid of ${value}")
    else:
        continue

print(bids)