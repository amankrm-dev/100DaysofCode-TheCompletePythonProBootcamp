# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)

def find_highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for bidder in user_data:
        bid_amount=user_data[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bidding reord of {highest_bid}")




user_data={}
Stop_bid=False
winner=0
while not Stop_bid:
    name=input("Enter your Name\n").lower()
    bid=int(input("Enter the bid Amount $"))
    user_data[name]=bid
    new_bid=input("Are there any other bidders. Type 'yes' or 'no' ").lower()
    if new_bid=="no":
        Stop_bid=True
        find_highest_bidder(user_data)
    else:
        print("\n"*100)


