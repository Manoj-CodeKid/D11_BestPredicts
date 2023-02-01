import pandas as pd
read_cols="A:F"
Dataframe1=pd.read_excel('Cricketit.xlsm',usecols=read_cols,nrows=11)
print(Dataframe1)
Team1_name=Dataframe1.columns.values[0]
Team2_name=Dataframe1.columns.values[3]
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
