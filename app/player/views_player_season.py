import soccerdata as sd
import pandas as pd
import matplotlib as mpl
import matplotsoccer as mps

# Importing necessary classes from soccerdata package
from soccerdata import FBref
from soccerdata import ClubElo
from soccerdata import WhoScored

# Instantiating objects to access football data
fbref = sd.FBref(no_cache=True)  # Object to access FBref data
WhoScored = sd.WhoScored(no_cache=True)  # Object to access WhoScored data
ClubElo = sd.ClubElo(no_cache=True)  # Object to access ClubElo data

# Prompting user for input
player_name = input("Player Name: ")  # Getting the player's name
season = int(input("Enter Season(e.g. 23-24): "))  # Getting the season
stat_type = input("Stat type(standard/shooting/passing/defense): ")  # Getting the type of statistics

# Retrieving player season statistics based on user input
player_stat = fbref.read_player_season_stats(player_name, season, stat_type)

# Printing the retrieved player statistics
print(player_stat)
