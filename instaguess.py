from random import randint
from game_data import data

def higher_or_lower():
    score = 0
    random_number1 = randint(0, len(data) - 1)
    random_number2 = randint(0, len(data) - 1)
    random_user = [data[random_number1]["name"], data[random_number1]["follower_count"], data[random_number1]["description"], data[random_number1]["country"]]
    random_user2 = [data[random_number2]["name"], data[random_number2]["follower_count"], data[random_number2]["description"], data[random_number2]["country"]]
    game_start = True

    while game_start:
        print(f"A:{random_user[0]}, a {random_user[2]} from {random_user[3]}\nB:{random_user2[0]}, a {random_user2[2]} from {random_user2[3]}")
        first_guess = input("Which has more followers? A or B? ").lower()
        if first_guess == "a" and random_user[1] > random_user2[1]:
            score += 1
            new_number = randint(0,len(data) - 1)
            random_user2 = [data[new_number]["name"], data[new_number]["follower_count"], data[new_number]["description"], data[new_number]["country"]]
            print(f"You're right! Your score is {score}")
        elif first_guess == "b" and random_user[1] < random_user2[1]:
            score += 1
            random_user = random_user2
            new_number = randint(0, len(data) - 1)
            random_user2 = [data[new_number]["name"], data[new_number]["follower_count"], data[new_number]["description"], data[new_number]["country"]]
            print(f"You're right! Your score is {score}")
        else:
                game_start = False
    print(f"You lose. Your score is {score}")
higher_or_lower()
