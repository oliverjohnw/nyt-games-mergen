import pandas as pd
import streamlit as st

def display_total_score_competition(
    monthly_data: pd.DataFrame
):
    """
    Displays wordle competition
    """
    # Convert 'Date' column to datetime for grouping
    monthly_data['Date'] = pd.to_datetime(monthly_data['Date'])

    # Group by date to find daily winners
    wordle_daily_winners = monthly_data.groupby('Date').apply(find_daily_wordle_winners)
    connections_daily_winners = monthly_data.groupby('Date').apply(find_daily_connections_winners)
    mini_daily_winners = monthly_data.groupby('Date').apply(find_daily_wordle_winners)
    strands_daily_winners = monthly_data.groupby('Date').apply(find_daily_wordle_winners)

    # Aggregate points by player
    wordle_daily_winners = wordle_daily_winners.groupby('Player').sum().reset_index()
    connections_daily_winners = connections_daily_winners.groupby('Player').sum().reset_index()
    mini_daily_winners = mini_daily_winners.groupby('Player').sum().reset_index()
    strands_daily_winners = strands_daily_winners.groupby('Player').sum().reset_index()

    # Rename columns for clarity
    wordle_daily_winners.columns = ['Player', 'Points']
    connections_daily_winners.columns = ['Player', 'Points']
    mini_daily_winners.columns = ['Player', 'Points']
    strands_daily_winners.columns = ['Player', 'Points']

    # competition_scores = competition_scores.sort_values(by = "Points", ascending = False)

    # st.table(competition_scores)

def find_daily_connections_winners(daily_data):
    """
    Identify the players with the lowest Wordle score for a given day.

    Args:
        daily_data (pd.DataFrame): DataFrame containing scores for a single day.

    Returns:
        pd.DataFrame: DataFrame with players who scored lowest on that day.
    """
    # Find the minimum score for the day
    min_score = daily_data['Score'].min()

    # Award 1 point to each player with the minimum score
    winners = daily_data[daily_data['Score'] == min_score].copy()
    winners['Points'] = 1

    return winners[['Player', 'Points']]