import os

def clear():
    # Clears screen for Windows or Unix/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

print("🏆 Welcome to the Secret Auction Program! 🏆")
print("Please enter your name and your bid in dollars 💵")

bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    
    # Validate numeric bid input
    while True:
        try:
            price = int(input("What is your bid?: $"))
            break
        except ValueError:
            print("❌ Please enter a valid number for your bid.")
    
    bids[name] = price
    
    should_continue = input("Are there any other bidders? Type 'yes' or 'no':\n").lower()
    if should_continue == "no":
        continue_bidding = False
    else:
        clear()

# Function to find highest bidder
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    print("\n🔔 Auction Complete! 🔔")
    print(f"🏅 The winner is **{winner}** with a bid of **${highest_bid}**!")

find_highest_bidder(bids)
