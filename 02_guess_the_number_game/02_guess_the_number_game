import random

start_fun = input("Do you want to start 'Guess the number game'? (y/n), choose 'q' to quit ").lower()

if start_fun == "y":
    difficulty_lvl = input("Pick dificulty level: 1, 2, 3. Level 1 is easy, 2 is medium and 3 is hard. ")
    upper_limit = "1"
    if difficulty_lvl == "1":
         upper_limit = 20
    elif difficulty_lvl == "2":
         upper_limit = 100
    elif difficulty_lvl == "3":
         upper_limit = 1000
        
    drawed_number = random.randint(1,int(upper_limit))
    trials = 0
    while True:
        answer = input(f"Guess the number between 1 and {upper_limit}: ")
        if answer.isnumeric():
            answer = int(answer)
            if answer < drawed_number:
                    print("Too small")
                    trials += 1
            elif answer > drawed_number:
                    print("Too big")
                    trials += 1
            elif answer == drawed_number:
                    trials += 1
                    print("Great job! you guessed in",  trials, "tries")
                    start_over = input("Do you want to play again? (y/n)").lower()
                    if start_over == "y":
                        trials = 0
                        drawed_number = random.randint(1,int(upper_limit))
                    elif start_over == "n":
                        print("Thanks for playing, see you next time")
                        break
                    else:
                        print("Choose either y or n")
                        break
        elif answer.lower() =="q":
            print("Are you giving up already? The number was", drawed_number, ".", "See you next time")
            break
        else:
            print("You are guessing numbers not letters")
            trials += 1
elif start_fun == "n":
    print("Let's play another time")
elif start_fun.lower() =="q":
     print("Thanks for playing, see you next time")
else:
    print("Choose either y or n")
