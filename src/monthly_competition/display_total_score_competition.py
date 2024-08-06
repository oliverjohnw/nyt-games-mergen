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

    # daily winners
    wordle_data = monthly_data[monthly_data['Game'] == 'Wordle']
    wordle_data['Date'] = pd.to_datetime(wordle_data['Date'])
    daily_winners = wordle_data.groupby('Date').apply(find_daily_wordle_winners)
    wordle_competition_scores = daily_winners.groupby('Player').sum().reset_index()
    wordle_competition_scores.columns = ['Player', 'Points']
    wordle_competition_scores = wordle_competition_scores.sort_values(by = "Points", ascending = False)

    connections_data = monthly_data[monthly_data['Game'] == 'Connections']
    connections_data['Date'] = pd.to_datetime(connections_data['Date'])
    daily_winners = connections_data.groupby('Date').apply(find_daily_connections_winners)
    connections_competition_scores = daily_winners.groupby('Player').sum().reset_index()
    connections_competition_scores.columns = ['Player', 'Points']
    connections_competition_scores = connections_competition_scores.sort_values(by = "Points", ascending = False)

    mini_data = monthly_data[monthly_data['Game'] == 'Mini']
    mini_data['Date'] = pd.to_datetime(mini_data['Date'])
    mini_data['TotalSeconds'] = mini_data['Score'].apply(convert_time_to_seconds)
    daily_winners = mini_data.groupby('Date').apply(find_daily_mini_winners)
    mini_competition_scores = daily_winners.groupby('Player').sum().reset_index()
    mini_competition_scores.columns = ['Player', 'Points']
    mini_competition_scores = mini_competition_scores.sort_values(by = "Points", ascending = False)

    strands_data = monthly_data[monthly_data['Game'] == 'Strands']
    strands_data['Date'] = pd.to_datetime(strands_data['Date'])
    daily_winners = strands_data.groupby('Date').apply(find_daily_strands_winners)
    strands_competition_scores = daily_winners.groupby('Player').sum().reset_index()
    strands_competition_scores.columns = ['Player', 'Points']
    strands_competition_scores = strands_competition_scores.sort_values(by = "Points", ascending = False)

    # player points
    susie_points = wordle_competition_scores.loc[wordle_competition_scores["Player"] == "Susie", "Points"].iloc[0] \
            + connections_competition_scores.loc[connections_competition_scores["Player"] == "Susie", "Points"].iloc[0] \
            + mini_competition_scores.loc[mini_competition_scores["Player"] == "Susie", "Points"].iloc[0] \
            + strands_competition_scores.loc[strands_competition_scores["Player"] == "Susie", "Points"].iloc[0]

    grace_points = wordle_competition_scores.loc[wordle_competition_scores["Player"] == "Grace", "Points"].iloc[0] \
            + connections_competition_scores.loc[connections_competition_scores["Player"] == "Grace", "Points"].iloc[0] \
            + mini_competition_scores.loc[mini_competition_scores["Player"] == "Grace", "Points"].iloc[0] \
            + strands_competition_scores.loc[strands_competition_scores["Player"] == "Grace", "Points"].iloc[0]
    
    john_points = wordle_competition_scores.loc[wordle_competition_scores["Player"] == "John", "Points"].iloc[0] \
            + connections_competition_scores.loc[connections_competition_scores["Player"] == "John", "Points"].iloc[0] \
            + mini_competition_scores.loc[mini_competition_scores["Player"] == "John", "Points"].iloc[0] \
            + strands_competition_scores.loc[strands_competition_scores["Player"] == "John", "Points"].iloc[0]
    
    player_data = pd.DataFrame({"Player": ["Susie", "Grace", "John"],
                                "Points": [susie_points, grace_points, john_points]},
                                index = [1,2,3]).sort_values(by = "Points", ascending=False)
    player_data.index = [1,2,3]
    
    st.table(player_data)


def find_daily_wordle_winners(daily_data):
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

def find_daily_strands_winners(daily_data):
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