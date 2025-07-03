import random

# Data of social media accounts
data = [
    {'name': 'Instagram', 'follower_count': 346, 'description': 'Social media platform', 'country': 'United States'},
    {'name': 'Cristiano Ronaldo', 'follower_count': 215, 'description': 'Footballer', 'country': 'Portugal'},
    {'name': 'Ariana Grande', 'follower_count': 183, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Dwayne Johnson', 'follower_count': 181, 'description': 'Actor and professional wrestler', 'country': 'United States'},
    {'name': 'Selena Gomez', 'follower_count': 174, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Kylie Jenner', 'follower_count': 172, 'description': 'Reality TV personality and businesswoman', 'country': 'United States'},
    {'name': 'Lionel Messi', 'follower_count': 149, 'description': 'Footballer', 'country': 'Argentina'},
    {'name': 'Beyoncé', 'follower_count': 145, 'description': 'Musician', 'country': 'United States'},
    {'name': 'Neymar', 'follower_count': 138, 'description': 'Footballer', 'country': 'Brazil'},
    {'name': 'National Geographic', 'follower_count': 135, 'description': 'Magazine', 'country': 'United States'},
    {'name': 'Justin Bieber', 'follower_count': 133, 'description': 'Musician', 'country': 'Canada'},
    {'name': 'Taylor Swift', 'follower_count': 131, 'description': 'Musician', 'country': 'United States'},
    {'name': 'Kendall Jenner', 'follower_count': 127, 'description': 'Reality TV personality and model', 'country': 'United States'},
    {'name': 'Jennifer Lopez', 'follower_count': 119, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Nicki Minaj', 'follower_count': 113, 'description': 'Musician', 'country': 'Trinidad and Tobago'},
    {'name': 'Nike', 'follower_count': 109, 'description': 'Sportswear multinational', 'country': 'United States'},
    {'name': 'Khloé Kardashian', 'follower_count': 108, 'description': 'Reality TV personality and businesswoman', 'country': 'United States'},
    {'name': 'Miley Cyrus', 'follower_count': 107, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Katy Perry', 'follower_count': 94, 'description': 'Musician', 'country': 'United States'},
    {'name': 'Zendaya', 'follower_count': 93, 'description': 'Actress and musician', 'country': 'United States'}
]

# Function to format account data
def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

# Function to check if user is correct
def is_correct(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Main game loop
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    # Make sure A and B are not the same
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"\nCompare A: {format_data(account_a)}")
    print("VS")
    print(f"Compare B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    
    correct = is_correct(guess, a_followers, b_followers)

    if correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
