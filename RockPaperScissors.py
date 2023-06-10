#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      anush
#
# Created:     04-06-2023
# Copyright:   (c) anush 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

#Defining a function to play the game
def play_game():

    while True:

        #inputting the user's choice
        choice_user= int(input("Enter the no. corresponding to your choice: \n (1) Rock\n (2) Scissors\n (3) Paper"))

        if choice_user>3 or choice_user<1:
            print("Enter a valid input")

        elif choice_user==1:
            print("You chose ROCK")

        elif choice_user==2:
            print("You chose SCISSORS")

        elif choice_user==3:
            print("You chose PAPER")

        #getting the computer's choice
        choice_comp= random.randint(1,3)

        if choice_comp==1:
            print("Your opponent chose ROCK")

        if choice_comp==2:
            print("Your opponent chose SCISSOR")

        if choice_comp==3:
            print("Your opponent chose PAPER")

        #deciding the winner

        if choice_comp==choice_user:
            print("It's a draw! ")

        if (choice_comp==1 and choice_user==3) or (choice_comp==2 and choice_user==1) or (choice_comp==3 and choice_user==2):
            print("Congrats You WIN <3")


        else:
            print("Ah You Lose :(")


        print("Press 1 to play again and 2 to end the game: ")
        user_next= int(input())
        if user_next ==2:
            print("THANK YOU FOR PLAYING! ")
            break

play_game()







