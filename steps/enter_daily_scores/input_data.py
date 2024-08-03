import streamlit as st
from datetime import date
import pandas as pd

# local imports
from src.enter_daily_scores import wordle, connections, mini, strands

def input_data(
    app_config: dict,
    player_data: pd.DataFrame
):
    """
    Allows user to input data for game
    
    Args:
        app_config (dict): dictionary with app configs/inputs
        player_data (pd.DataFrame): dataframe with player scores
    
    Returns:
        player_data (pd.DataFrame): dataframe with player scores
    """
    # player options
    player = st.selectbox("Select Player", ["Grace", "John", "Susie"])

    # input data for a certain date
    selected_date = st.date_input("Select Date", value=date.today())

    # game options
    game = st.selectbox("Select Game", ["Wordle", "Connections", "Mini", "Strands"])

    # if the player has submitted a score for this game, log a warning
    if not player_data[(player_data['Date'] == str(selected_date)) & 
                        (player_data['Player'] == player) & 
                        (player_data['Game'] == game)].empty:
        st.warning(f"{player} has already submitted a score for {game} on {selected_date}.")

    else:
        # wordle
        if game == "Wordle":
            player_data = wordle(app_config, player_data, selected_date, player, game)

        # connections
        if game == "Connections":
            player_data = connections(app_config, player_data, selected_date, player, game)

        # mini
        if game == "Mini":
            player_data = mini(app_config, player_data, selected_date, player, game)

        # strands
        if game == "Strands":
            player_data = strands(app_config, player_data, selected_date, player, game)

    return player_data