import random

wlc_msg = "Hello in paper, rock, scissors game. \n1. Start a new game \n2. Show results \n3. Quit \n Rules:\n paper beats rock \n rock beats scissors \n scissors beats paper."
print(wlc_msg)


options = ["paper", "rock", "scissors"]
player_score = 0
computer_score = 0
draws = 0
while True:
    chosen_option = input("What do you want to do? ")
    games = 0
    if chosen_option == "1":
        try:
            game_limit = int(input("How many games do you wish to play? "))
        except:
            print("Please input a number")
            continue
        player_score = 0
        computer_score = 0
        draws = 0
        while games < game_limit:
            print("p - paper \nr - rock \ns - scissors \nq - quit to menu")
            player_choice = input("What option do you choose ").lower()
            computer_choice = random.choice(options)
            if player_choice == "r":
                player_choice = "rock"
            elif player_choice == "p":
                player_choice = "paper"
            elif player_choice == "s":
                player_choice = "scissors"  
            elif player_choice == "q":
                print("")
                print(f"Your score is {player_score}, computer score is {computer_score}, draw number {draws}.")
                break 
            else: 
                print("It's not a viable option.")
                continue
            print(f"Your choice is {player_choice} and computer choice is {computer_choice}")
            if player_choice == computer_choice:
                draws +=1
                games +=1
                print(f"No one wins. Game no {games}")
            elif player_choice == "rock" and computer_choice == "paper":
                computer_score +=1
                games +=1
                print(f"Computer wins. Game no {games}")
            elif player_choice == "paper" and computer_choice == "scissors":
                computer_score +=1
                games +=1
                print(f"Computer wins. Game no {games}")
            elif player_choice == "scissors" and computer_choice == "rock":
                computer_score +=1
                games +=1
                print(f"Computer wins. Game no {games}")
            elif player_choice == "scissors" and computer_choice == "paper":
                player_score +=1
                games +=1
                print(f"Player wins. Game no {games}")
            elif player_choice == "rock" and computer_choice == "scissors":
                player_score +=1
                games +=1
                print(f"Player wins. Game no {games}")
            elif player_choice == "paper" and computer_choice == "rock":
                player_score +=1
                games +=1
                print(f"Player wins. Game no {games}")
        if games >= game_limit:
            print(f"Game ended in {games} rounds. \nYour score is {player_score}, computer score is {computer_score}, draw number {draws}.")
            continue
    elif chosen_option == "2":
        print(f"Your score is {player_score}, computer score is {computer_score}, draw number {draws}.")
    elif chosen_option == "3":
        break
    else:
        print("Wrong option")
        continue
