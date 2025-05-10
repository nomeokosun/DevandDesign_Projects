import numpy as np
import pandas as pd
import csv
import os

filePath1 = os.path.join(os.getcwd(), '..' , '_WEEK 7 EXERCISE' , 'epl_player_data.csv') 

player_df = pd.read_csv(filePath1)
team_df = pd.read_csv('../_WEEK 7 EXERCISE/epl_team_data.csv')

print(player_df)
print(team_df)

# print(os.getcwd())