import pandas as pd
import streamlit as st
from datetime import date

def display_todays_scores(
    player_data: pd.DataFrame
):
    """
    Displays todays scores
    
    Args:
        player_data (pd.DataFrame): dataframe with player scores
    """
    # filter for todays data
    today = date.today()
    today_scores = player_data[player_data['Date'] == str(today)]

    # map scores
    today_scores['Score'] = today_scores.apply(reverse_score_mapping, axis=1)

    # Display the current scores
    st.header("Today's Scores:")
    st.table(today_scores)

def reverse_score_mapping(row):
    """
    Reverse the mapped score to its original representation
    """
    wordle_reverse_mapping = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "Failed"}
    connections_reverse_mapping = {0: "0 Mistakes", 1: "1 Mistake", 2: "2 Mistakes", 3: "3 Mistakes", 4: "Failed"}
    spanagram_reverse_mapping = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "Failed"}
    hint_reverse_mapping = {0: "No", 1: "Yes"}

    game = row['Game']
    if game == 'Wordle':
        return wordle_reverse_mapping.get(row['Score'], row['Score'])
    elif game == 'Connections':
        return connections_reverse_mapping.get(row['Score'], row['Score'])
    elif game == 'Mini':
        minutes, seconds = divmod(row['Score'], 60)
        return f"{minutes}:{seconds:02d}"
    elif game == 'Strands':
        # Handle both Spanagram and Hint
        spanagram_score = spanagram_reverse_mapping.get(row.get('Spanagram Score', row['Score']), row['Score'])
        hint_score = hint_reverse_mapping.get(row.get('Hint Used', row['Score']), row['Score'])
        return f"Spanagram: {spanagram_score}, Hint: {hint_score}"
    return row['Score']