import streamlit as st

# local imports
from steps.monthly_competition import display_monthly_competition
from src.utils import load_player_data

def monthly_competition(
    app_config: dict
):
    """
    Monthly competition pipeline
    
    Args:
        app_config (dict): dictionary with app configs/inputs

    """
    st.subheader("Monthly Competitions")

    # load player data
    player_data = load_player_data(app_config)

    # display statistics
    display_monthly_competition(app_config, player_data)