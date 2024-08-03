import streamlit as st

# local imports
from steps.player_statistics import (
    display_statistics
)
from src.utils import load_player_data

def player_statistics(
    app_config: dict
):
    """
    Player statistics pipeline
    
    Args:
        app_config (dict): dictionary with app configs/inputs
    """
    st.subheader("Player Statistics")
    st.write("To Be Continued....")

    # load player data
    player_data = load_player_data(app_config)

    # display statistics
    display_statistics(app_config, player_data)