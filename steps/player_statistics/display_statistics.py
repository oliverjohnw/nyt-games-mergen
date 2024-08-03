import pandas as pd
import streamlit as st

def display_statistics(
    app_config: dict,
    player_data: pd.DataFrame
):
    """
    Displays statistics by player

    Args:
        app_config (dict): dictionary with app configs/inputs
        player_data (pd.DataFrame): dataframe with player scores
    """
    # player options
    player = st.selectbox("Select Player", ["Grace", "John", "Susie"])

    # game options
    game = st.selectbox("Select Game", ["Wordle", "Connections", "Mini", "Strands"])