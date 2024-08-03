import streamlit as st

# local imports
from steps.enter_daily_scores import (
    input_data,
    display_todays_scores
)
from src.utils import load_player_data

def enter_daily_scores(
    app_config: dict
):
    """
    Loads in pre-existing player data (.csv) and allows users to add scores for the day
    
    Args:
        app_config (dict): dictionary with app configs/inputs
    """
    st.subheader("Enter Daily Scores")
    st.subheader("Still a work in progress! Please don't use this feature yet :)")
    
    # load player data
    player_data = load_player_data(app_config)

    # input data
    player_data = input_data(app_config, player_data)

    # display todays scores
    display_todays_scores(player_data)