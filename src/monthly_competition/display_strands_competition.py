import pandas as pd
import streamlit as st

def display_strands_competition(
    monthly_data: pd.DataFrame
):
    """
    Displays wordle competition
    """
    wordle_data = monthly_data[monthly_data['Game'] == 'Strands']

    # Convert 'Date' column to datetime for grouping
    wordle_data['Date'] = pd.to_datetime(wordle_data['Date'])

    # Group by date to find daily winners
    daily_winners = wordle_data.groupby('Date').apply(find_daily_wordle_winners)

    # Aggregate points by player
    competition_scores = daily_winners.groupby('Player').sum().reset_index()

    # Rename columns for clarity
    competition_scores.columns = ['Player', 'Points']

    competition_scores = competition_scores.sort_values(by = "Points", ascending = False)
    competition_scores.index = [1,2,3]

    st.table(competition_scores)


def find_daily_wordle_winners(daily_data):
    """
    Identify the players with the lowest Wordle score for a given day.

    Args:
        daily_data (pd.DataFrame): DataFrame containing scores for a single day.

    Returns:
        pd.DataFrame: DataFrame with players who scored lowest on that day.
    """
    # Find the minimum score for the day
    min_score = daily_data['Spanagram Score'].min()

    # Award 1 point to each player with the minimum score
    winners = daily_data[daily_data['Spanagram Score'] == min_score].copy()
    winners['Points'] = 1

    return winners[['Player', 'Points']]