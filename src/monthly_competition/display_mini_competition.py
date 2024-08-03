import pandas as pd
import streamlit as st

def display_mini_competition(
    monthly_data: pd.DataFrame
):
    """
    Displays wordle competition
    """
    mini_data = monthly_data[monthly_data['Game'] == 'Mini']

    # Convert 'Date' column to datetime for grouping
    mini_data['Date'] = pd.to_datetime(mini_data['Date'])

    # Convert time format to total seconds for comparison
    mini_data['TotalSeconds'] = mini_data['Score'].apply(convert_time_to_seconds)

    # Group by date to find daily winners
    daily_winners = mini_data.groupby('Date').apply(find_daily_mini_winners)

    # Aggregate points by player
    competition_scores = daily_winners.groupby('Player').sum().reset_index()

    # Rename columns for clarity
    competition_scores.columns = ['Player', 'Points']

    competition_scores = competition_scores.sort_values(by = "Points", ascending = False)

    st.table(competition_scores)

def convert_time_to_seconds(time_str):
    """
    Convert a time string in MM:SS format to total seconds.

    Args:
        time_str (str): Time string in MM:SS format.

    Returns:
        int: Total seconds.
    """
    try:
        minutes, seconds = map(int, time_str.split(':'))
        return minutes * 60 + seconds
    except ValueError:
        return float('inf')  # Treat invalid time as infinite for comparison

def find_daily_mini_winners(daily_data):
    """
    Identify the players with the lowest Mini time for a given day.

    Args:
        daily_data (pd.DataFrame): DataFrame containing scores for a single day.

    Returns:
        pd.DataFrame: DataFrame with players who had the lowest time on that day.
    """
    # Find the minimum time for the day
    min_time = daily_data['TotalSeconds'].min()

    # Award 1 point to each player with the minimum time
    winners = daily_data[daily_data['TotalSeconds'] == min_time].copy()
    winners['Points'] = 1

    return winners[['Player', 'Points']]