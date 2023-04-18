from higher_lower_art import logo,vs
import random
from higher_lower_game_data import data
import os

def format_data(account):
    acc_name = account["name"]
    acc_descr = account["description"]
    acc_country =account["country"]
    return f"{acc_name}, a {acc_descr} from {acc_country}"

def check_answer(guess, a_follwers, b_followers):
    if a_follwers > b_followers:
        return guess== "a"
    else:
        return guess == "b"
    
print (logo)
score = 0
account_b = random.choice(data)
game_should_continue = True
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    
    while account_a == account_b:
        
        account_b=random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")

    guess = input("Who has more followers ? Type A or B:").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct=check_answer(guess , a_follower_count, b_follower_count)
    os.system('cls')
    print(logo)

    if is_correct:
        score +=1
        print(f"You're right. current score: {score}")
    else:
        game_should_continue = False 
           
        print(f"That's wrong. final score : {score}")  
    