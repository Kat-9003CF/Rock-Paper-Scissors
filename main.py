print("Rock, Paper, Scissors!")
from random import randint
pscore = 0
cscore = 0
while pscore <3 and cscore <3:
    print('Score is player: ',pscore,'computer: ', cscore)
    choice = ''
    player = input('Rock (r), paper (p) or scissors (s)?')
    if player == 'r':
        choice = 'rock'
    elif player == 'p':
        choice = 'paper'
    elif player == 's':
        choice = 'scissors'
    else: player = input('Try again, choose rock (r), paper (p) or scissors (s).')
    print('You have chosen '+choice)
    
    
    computer = randint(1, 3)
    compChoice = ''
    if computer == 1:
        compChoice = 'rock'
    elif computer == 2:
        compChoice = 'paper'
    else:
        compChoice = 'scissors'
        
    print('Computer has chosen '+ compChoice)
    
    if choice == compChoice:
        print("It's a draw!")
    elif choice == 'rock':
        if compChoice == 'scissors':
            print(choice + ' beats '+compChoice + ', you win!')
            pscore+=1
        else:
            print(compChoice + ' beats '+choice + ', you lose!')
            cscore+=1
    elif choice == 'scissors':
        if compChoice == 'paper':
            print(choice + ' beats '+compChoice + ', you win!')
            pscore+=1
        else:
            print(compChoice + ' beats '+choice + ', you lose!')
            cscore+=1
    elif choice == 'paper':
        if compChoice == 'rock':
            print(choice + ' beats '+compChoice + ', you win!')
            pscore+=1
        else:
            print(compChoice + ' beats '+choice + ', you lose')
            cscore+=1

    if pscore == 3:
        print ('Congratulations, you win!  Press the button to play again.')
        break
    if cscore ==3:
        print ('Sorry, you lose!  Press the button to try again.')
        break
