import soccerdata as sd
from soccerdata import FBref
from soccerdata import ClubElo
from soccerdata import WhoScored

fbref = sd.FBref()
WhoScored = sd.WhoScored()
ClubElo = sd.ClubElo()

def scrape_player_stats(player_id):
    player_stats_whoScored = WhoScored.player_stats(player_id)

    # Perform data processing
    processed_stats = {
        'whoScored_stats': process_whoScored_stats(player_stats_whoScored),
        'cleaned_stats': clean_player_stats(processed_stats),
        'normalized_stats': normalize_player_stats(processed_stats),
        'formatted_stats': format_player_stats(processed_stats)
    }

    return processed_stats

def scrape_team_stats(team_id):
    team_stats_whoScored = WhoScored.team_stats(team_id)

    # Perform data processing
    processed_stats = {
        'whoScored_stats': process_whoScored_stats(team_stats_whoScored),
        'cleaned_stats': clean_team_stats(processed_stats),
        'normalized_stats': normalize_team_stats(processed_stats),
        'formatted_stats': format_team_stats(processed_stats)
    }

    return processed_stats

def scrape_league_stats(league_id):
    league_stats_whoScored = WhoScored.league_stats(league_id)

    # Perform data processing
    processed_stats = {
        'whoScored_stats': process_whoScored_stats(league_stats_whoScored),
        'cleaned_stats': clean_league_stats(processed_stats),
        'normalized_stats': normalize_league_stats(processed_stats),
        'formatted_stats': format_league_stats(processed_stats)
    }

    return processed_stats

def process_whoScored_stats(stats):
    # Extract relevant fields
    relevant_fields = {
        'Goals': stats.get('Goals', 0),
        'Assists': stats.get('Assists', 0),
        # Add other relevant fields
    }

    # Data cleaning
    cleaned_data = clean_data(relevant_fields)

    # Normalization/Scaling
    normalized_data = normalize_data(cleaned_data)

    # Formatting
    formatted_data = format_data(normalized_data)

    return formatted_data

def clean_data(data):
    # Add your custom data cleaning logic here
    # Example: Handle missing values, remove outliers, etc.
    cleaned_data = {key: value for key, value in data.items() if value is not None}
    return cleaned_data

def normalize_data(data):
    # Add your custom normalization/scaling logic here
    # Example: Use Min-Max scaling, Z-score normalization, etc.
    normalized_data = {key: value / max(data.values()) for key, value in data.items()}
    return normalized_data

def format_data(data):
    # Add your custom formatting logic here
    # Example: Format numerical values, convert units, etc.
    formatted_data = {key.replace('_', ' '): value for key, value in data.items()}
    return formatted_data

# Additional functions for player, team, and league
def clean_player_stats(stats):
    # Add your custom player data cleaning logic here
    cleaned_stats = stats  # Placeholder, replace with actual logic
    return cleaned_stats

def normalize_player_stats(stats):
    # Add your custom player normalization/scaling logic here
    normalized_stats = stats  # Placeholder, replace with actual logic
    return normalized_stats

def format_player_stats(stats):
    # Add your custom player formatting logic here
    formatted_stats = stats  # Placeholder, replace with actual logic
    return formatted_stats

def clean_team_stats(stats):
    # Add your custom team data cleaning logic here
    cleaned_stats = stats  # Placeholder, replace with actual logic
    return cleaned_stats

def normalize_team_stats(stats):
    # Add your custom team normalization/scaling logic here
    normalized_stats = stats  # Placeholder, replace with actual logic
    return normalized_stats

def format_team_stats(stats):
    # Add your custom team formatting logic here
    formatted_stats = stats  # Placeholder, replace with actual logic
    return formatted_stats

def clean_league_stats(stats):
    # Add your custom league data cleaning logic here
    cleaned_stats = stats  # Placeholder, replace with actual logic
    return cleaned_stats

def normalize_league_stats(stats):
    # Add your custom league normalization/scaling logic here
    normalized_stats = stats  # Placeholder, replace with actual logic
    return normalized_stats

def format_league_stats(stats):
    # Add your custom league formatting logic here
    formatted_stats = stats  # Placeholder, replace with actual logic
    return formatted_stats
