import random as rd

rock_table = {"rock":"draw","paper":"lose","scissors":"win"}
paper_table = {"rock":"win","paper":"draw","scissors":"lose"}
scissors_table ={"rock":"lose","paper":"win","scissors":"draw"}

game_logic = {"rock":rock_table,"paper":paper_table,"scissors":scissors_table}
choices = ["rock","paper","scissors"]
computer_score = 0
player_score = 0
rounds = 0
status= True

print("Welcome to TicTacToe game\n")
while status:

    while True:

        player = input("Please pick Rock, Paper or Scissors: ").lower()
        if player not in (choices):
            print("Invalid choice")
            continue
        else:
            break
    print("-------------------------------------------------------------------------")
    rounds+=1
    print(f'Round- {rounds}')
    computer = choices[rd.randint(0,2)]
    
    if game_logic[player][computer] == "win":
        print(f"Computer picked: {computer}")
        print("You win!")
        player_score+=1
        print(f"Your score: {player_score} & Computer's score: {computer_score}")
    elif game_logic[player][computer] == "lose":
        print(f"Computer picked: {computer}")
        print("You lost!")
        computer_score+=1
        print(f"Your score: {player_score} & Computer's score: {computer_score}")

    else:
        print(f"Computer picked: {computer}")
        print("Draw")
        print(f"Your score: {player_score} & Computer's score: {computer_score}")
    print("-------------------------------------------------------------------------")

    play_again = input("Play again? Y/N: ").lower()
    if play_again == "y":
        continue
    else:
        status =False   
print("Thank you for playing :)")
    
    