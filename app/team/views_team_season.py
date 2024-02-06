import soccerdata as sd
import pandas as pd
import matplotlib as mpl
import matplotsoccer as mps

from soccerdata import FBref
from soccerdata import ClubElo
from soccerdata import WhoScored

fbref = sd.FBref(no_cache=True)
WhoScored = sd.WhoScored(no_cache=True)
ClubElo = sd.ClubElo(no_cache=True)

player_name =   input("Team Name: ")
season      =   int(input("Enter Season(e.g. 23-24): "))
stat_type   =   input("Stat type(standard/shooting/passing/defense): ")
team_stat =   fbref.read_team_season_stats(team_name, season, stat_type)
print(team_stat)