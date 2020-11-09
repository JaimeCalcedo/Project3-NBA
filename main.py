import pandas as pd
#from pip import _internal
#_internal.main(["list"])
from Src.plotting import *

print("Welcome to my stats generator")
print("What stats would you like to generate?")
print("To generate % Shooting from a single player type 1, to generate a comparative report (Regular Season/ Post Season) of % Shooting from 1 player type 2, to generate a compartive report of % Shooting from 2 different player type 3")

answer = input("Type 1, 2 or 3")
if answer == "1":
    print("Would you like to obtain % Shooting Stats  from Regular or Post Season?")
    print("Type 1 for Regular and 2 for Post")
    answer2  = input("Type 1 or 2")
    print("Now type the player you want Stats from")
    decision = input("Type the player")
    if answer2 == "1":
        plot_regular_season(decision)
        fig.savefig("../Output/Regular_Season_Stats.png")
    if answer2 == "2":
        plot_post_season(decision)
elif answer == "2":
    print("Now type the player you want Stats from")
    decision2 = input("Type the player")
    comparison_player(decision2)
    comparison_player1(decision2)
    comparison_player2(decision2)
elif answer == "3":
    print("Would you like to compare Regular or Post Season Stats?")
    print("Type 1 for Regular and 2 for Post")
    answer3 = input("Type 1 or 2")
    if answer3 == "1":
        print("Now type the players you want stats from")
        decision3 = input("Type player 1")
        decision4 = input("Type player 2")
        comparison_two_player_regular(decision3, decision4)
    elif answer3 == "2":
        print("Now type the players you want stats from")
        decision5 = input("Type player 1")
        decision6 = input("Type player 2")
        comparison_two_player_post(decision5, decision6)

print("Thanks for using my stats generator, hope you found it useful")
