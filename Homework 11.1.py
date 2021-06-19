import datetime
import json
import random

secret = random.randint(1, 50)
attempts = 0
wrong_guesses = []

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

for score_dict in score_list:
    score_text = "Player {0} had {1} attempts on {2}. The secret number was {3}.".format(score_dict.get("player_name"),
                  str(score_dict.get("attempts")),
                  score_dict.get("date"),
                  score_dict.get("secret_number")),
                  score_dict.get("wrong_guesses")),

    print(score_text)

    wrong_guesses = []

while True:
    guess = int(input("Guess the secret number (between 1 and 50): "))
    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "wrong guesses": wrong_guesses, "date": str(datetime.datetime.now()),
                           "secret_number": secret})

        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("Congratulations, you won!")
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Wrong, try a smaller number")
    elif guess < secret:
        print("Wrong, try a bigger number")

        wrong_guesses.append(guess)