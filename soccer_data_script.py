import soccerdata as sd

# Create scraper class instance
fbref = sd.FBref()

# Read team season stats for shooting
season_stats = fbref.read_team_season_stats(stat_type='shooting')

# Print the obtained data
print(season_stats)