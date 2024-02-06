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
# Get user input for player name, match ID, and stat type
team_name = input("Player Name  : ")
match_id_input = input("Match ID     : ")
stat_type = input("Stat type(standard/shooting/passing/defense): ")

# Convert match_id to int if provided
match_id = int(match_id_input) if match_id_input.isdigit() else None

# Read player match stats based on the provided inputs
team_stat = fbref.read_team_match_stats(team_name, match_id=match_id, stat_type=stat_type)
print(player_stat)