import streamlit as st
import pandas as pd

# local imports
from pipelines import (
    enter_daily_scores,
    player_statistics,
    monthly_competition
)
from src.utils import read_file

# read script config
app_config = read_file("config/app.yaml")

# page title
st.title("NYT Daily Games Tracker")

# two columns (left = dropdown, right = content)
left_column, spacer, right_column = st.columns([1, 0.6, 2])

# dropdown menu
with left_column:
    option = st.selectbox(
        "Choose An Option",
        ["Enter Daily Scores", "Monthly Competitions", "Player Statistics"]
    )
with spacer:
    st.empty()

# content
with right_column:
    if option == "Enter Daily Scores":
        enter_daily_scores(app_config)

    elif option == "Monthly Competitions":
        monthly_competition(app_config)

    elif option == "Player Statistics":
        player_statistics(app_config)

