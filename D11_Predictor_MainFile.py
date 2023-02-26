import pandas as pd
import inquirer
from itertools import chain
import numpy as np
read_cols="A:F"
Dataframe1=pd.read_excel('Cricketit.xlsm',usecols=read_cols,nrows=11)
print(Dataframe1)
Dataframe2=pd.read_excel('Cricketit.xlsm',usecols="A",nrows=11,header=0)
Dataframe3=pd.read_excel('Cricketit.xlsm',usecols="D",nrows=11,header=0)
players_list=(np.append(Dataframe2.values,Dataframe3.values))
impact_players_selection_list=players_list
print(type(players_list))
#print(Dataframe3.shape)

Team1_name=Dataframe1.columns.values[0]
Team2_name=Dataframe1.columns.values[3]

#print("Test code {}".format(Dataframe1.iterrows(1)))
pitch_input=int(input("Press 1 for Batting, Press 2 for Balanced, Press 3 for Bowling : "))
if pitch_input==1:
    print("Your input is Batting Pitch")
elif pitch_input==2:
    print("Your input is Balanced Pitch")
else:
    print("Your input is Bowling Pitch")
winner_predictor=int(input("Whom do you predict as winner in this match. Press 1 for {}, 2 for {}: ".format(Team1_name,Team2_name)))
if winner_predictor==1:
    print("Your Winner prediction for this match is {}".format(Team1_name))
else:
    print("Your Winner prediction for this match is {}".format(Team2_name))
match_time=int(input("Press 1 for day game and 2 for day night game : "))
num_of_teams=int(input("Enter the number of teams you want to generate : "))
team_structure=int(input("Press 1 for 7:4 structure, 2 for 10:1 Structure : "))
additional_inputs=int(input("Press 1 to customize your team selection further, 2 to proceed directly for teams generation : "))
if additional_inputs==1:
    impact_player1_response=int(input("Press 1 to select an impact player to have in all your teams : "))
    impact_player_list=[]
else:
    print("Ok")
while impact_player1_response==1:
    impact_player_select=[inquirer.List('Impact Player selection',message="Select your impact player1 : ",choices=impact_players_selection_list.tolist())]
    impact_player1=inquirer.prompt(impact_player_select)
    print("You have added {} as one of impact player to have in all of your teams".format(impact_player1["Impact Player selection"]))
    impact_player_list.append(impact_player1["Impact Player selection"])
    impact_players_selection_list=np.delete(impact_players_selection_list,np.where(impact_players_selection_list==impact_player1["Impact Player selection"]))
    impact_player1_response=int(input("Press 1 to add one more player to your impact list,2 to proceed for team selection:"))

print("Impact player list :",impact_player_list)



