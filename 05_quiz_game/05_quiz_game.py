print("Welcome to the Big Quiz!")

questions = ["More than one animal?", "You drink coffee from it?", "What do you use to wipe your nose?"]
answers = ["llama", "cup", "tissue"]
pos_answ = 0
max_score = len(questions)
score = 0
play_game = 1

while play_game == 1:
        for question in questions:
                print(question)
                answer = answers[pos_answ]
                answ = input("What is your answer? ").lower()
                if answ == answer:
                        print("Good answer")
                        score +=1 
                else:
                        print(f"Wrong answer. Correct is {answer}")
                pos_answ +=1
        print(f"Your score is {score}/{max_score}")
        if score == max_score:
                print("You are the champion")
        elif score > max_score*0.66:
                print("Very good, you are almost there")
        elif score > max_score*0.33:
                print("Not good, not bad. Keep trying")
        else:
                print("Terrible. There is a long way to the top")
        while True:
                retry = input("Play again (y/n) ").lower()
                if retry == "y":
                        pos_answ = 0
                        score = 0
                        break
                elif retry == "n":
                        print("Thank you for playing")
                        play_game = 0 
                        break       
                else:
                        print("There is no such option")
