#rock, paper, scissors - game
#import modules
import random
import sys
import time

#Keep track of wins/losses/ties
Wins = 0
Losses = 0
Ties = 0
Points = 0

#intro
print('Welcome to the game of Rock, Paper, Scissors.')
print('Play to earn points and even have the chance to gamble and score more! You can gain points for winning and lose points for, well... losing!')

#Create the game loop
while True:
    while True:
        print('''These are you stats for this session: \n{} Wins, {} Losses, {} Ties, {}\n\n'''.format(Wins, Losses, Ties, Points))
        print('Enter your move:')
        print('(R)ock, (P)aper, (S)cissors or (Q)uit.')
        PlayerChoice = input('>> ').upper()
        if PlayerChoice == 'Q': 
            print('See you later!')
            sys.exit()
        if PlayerChoice == 'R' or PlayerChoice == 'P' or PlayerChoice =='S': 
            break
#Catch if input does not meet the requirements to play
        else:
            print('Please enter one of the following options to paly: R, P, S or Q to quit. \nTry again!\n\n')


#TODO:Creating an all or nothing mode
        #if Points >= 1:
            #print('Would you like to go all or nothing? Risking all of your points can score you x2 what you have now!')
            #print('But if you lose... You will have to start all over again.\n\nCare to Try?\n(Y)es or (N)o?')
            #DoubleDown = input('>> ').upper()
            #if DoubleDown == 'N':
                #break
            #if DoubleDown == 'Y':
                #print('Let\'s get ready to rumbleeee!')

#Confirm player choice
    if PlayerChoice == 'R':
        print('ROCK VS ...')
        PlayerChoice = 'ROCK'
    elif PlayerChoice == 'P':
        print('PAPER VS ...')
        PlayerChoice = 'PAPER'
    elif PlayerChoice == 'S':
        print('SCISSORS VS ...')
        PlayerChoice = 'SCISSORS'        

#Countdown timer?
    #time.sleep(1)
    print('...1')
    #time.sleep(1)
    print('...2')
    #time.sleep(1)
    print('...3')
    #time.sleep(0.5)
    
#fixing double down
    #while Points >= 1: 
        #print('Before we reveal the answer, would you like to go all or nothing? Risking all of your points can score you x2 what you have now!')
        #print('But if you lose... You will have to start all over again.\n\nCare to Try?\n(Y)es or (N)o?')
        #DoubleDown = input('>> ').upper()
        #if DoubleDown == 'N':
            #break
        #if DoubleDown == 'Y':
            #print('Let\'s get ready to rumbleeee!')
        #break

#Get PC to make a choice
    ComputerChoice = random.randint(1, 3)
    if ComputerChoice == 1:
        ComputerChoice = 'ROCK'
    elif ComputerChoice == 2:
        ComputerChoice = 'PAPER'
    elif ComputerChoice == 3:
        ComputerChoice = 'SCISSORS'
    print(ComputerChoice)

#Record your stats
    #DoubleDown = DoublePoints
    if PlayerChoice == ComputerChoice:
        print('I guess we have a Tie!')
        Ties = Ties + 1
    elif PlayerChoice == 'ROCK' and ComputerChoice == 'SCISSORS':
        print('You are the winner!')
        Wins = Wins + 1
        #if DoubleDown == 'Y':
            #Points = Points * 2
        #if DoubleDown == 'N': 
        Points = Points + 1
    elif PlayerChoice == 'PAPER' and ComputerChoice == 'ROCK':
        print('You are the winner!')
        Wins = Wins + 1
        #if DoubleDown == 'Y':
            #Points = Points * 2
        #if DoubleDown == 'N': 
        Points = Points + 1
    elif PlayerChoice == 'SCISSORS' and ComputerChoice == 'PAPER':
        print('You are the winner!')
        Wins = Wins + 1
        #if DoubleDown == 'Y':
            #Points = Points * 2
        #if DoubleDown == 'N': 
        Points = Points + 1
    elif PlayerChoice == 'ROCK' and ComputerChoice == 'PAPER':
        print('Better luck next time! You lose.')
        Losses = Losses + 1
        #if DoubleDown == 'Y':
            #Points = 0
        #elif DoubleDown == 'N': 
        Points = Points - 1
        if Points <= 0:
            Points = 0
    elif PlayerChoice == 'PAPER' and ComputerChoice == 'SCISSORS':
        print('Better luck next time! You lose.')
        Losses = Losses + 1
        #if DoubleDown == 'Y':
            #Points = 0
        #elif DoubleDown == 'N': 
        Points = Points - 1
        if Points <= 0:
            Points = 0
    elif PlayerChoice == 'SCISSORS' and ComputerChoice == 'ROCK':
        print('Better luck next time! You lose.')
        Losses = Losses + 1
        #if DoubleDown == 'Y':
            #Points = 0
        #elif DoubleDown == 'N': 
        Points = Points - 1
        if Points <= 0:
            Points = 0