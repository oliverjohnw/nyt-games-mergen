import pandas as pd
import streamlit as st

# local imports
from src.monthly_competition import (
    display_wordle_competition,
    display_connections_competition,
    display_mini_competition,
    display_strands_competition,
    display_total_score_competition
)

def display_monthly_competition(
    app_config: dict,
    player_data: pd.DataFrame
):
    """
    Displays monthly competition

    Args:
        app_config (dict): dictionary with app configs/inputs
        player_data (pd.DataFrame): dataframe with player scores
    """
    # add month to dataframe
    player_data['Month'] = pd.to_datetime(player_data['Date']).dt.to_period('M')

    # months
    months = sorted(player_data['Month'].unique(), reverse=True)

    # month dropbox
    month = st.selectbox("Select Month", months, format_func=lambda x: x.strftime('%B %Y'))

    # game options
    game = st.selectbox("Select Game", ["Monthly Totals", "Wordle", "Connections", "Mini", "Strands"])

    # monthly data
    monthly_data = player_data[player_data['Month'] == month]

    if game == "Monthly Totals":
        display_total_score_competition(monthly_data)

    if game == "Wordle":
        display_wordle_competition(monthly_data)

    if game == "Connections":
        display_connections_competition(monthly_data)

    if game == "Mini":
        st.write(f"Selected Game: {game}")
        display_mini_competition(monthly_data)

    if game == "Strands":
        st.write(f"Selected Game: {game}")
        display_strands_competition(monthly_data)