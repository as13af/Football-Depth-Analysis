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

league_name =   input("League: ")
league_stat =   fbref.read_leagues()
print(league_stat)