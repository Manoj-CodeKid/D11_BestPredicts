import pandas as pd
read_cols=range(0,6)
Dataframe1=pd.read_excel('Cricketit.xlsm',usecols=read_cols,nrows=11)
print(Dataframe1)
pitch_input=int(input("Press 1 for Batting, Press 2 for Balanced, Press 3 for Bowling : "))
if pitch_input==1:
    print("User input is Batting Pitch")
elif pitch_input==2:
    print("User input is Balanced Pitch")
else:
    print("User input is Bowling Pitch")
