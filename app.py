import streamlit as st
import pandas as pd
from PIL import Image

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
header_col1, header_col2 = st.columns([3, 1])

with header_col1:
    st.title("NYT Daily Games Tracker")

with header_col2:
    image_path = "img/nyt.png"  # Update this path to your image file
    logo_image = Image.open(image_path)
    st.image(logo_image, use_column_width=True)

# two columns (left = dropdown, right = content)
left_column, spacer, right_column = st.columns([1, 0.6, 2])

# dropdown menu
with left_column:
    option = st.selectbox(
        "Choose An Option",
        ["Monthly Competitions", "Enter Daily Scores", "Player Statistics"]
    )

    # if option == "Enter Daily Scores":
    #     image_path1 = "img/tucker.jpeg"  
    #     st.image(image_path1, use_column_width=True)  

    # elif option == "Monthly Competitions":
    #     image_path2 = "img/sufi.jpeg"
    #     image2 = Image.open(image_path2)
    #     rotated_image2 = image2.rotate(270, expand=True)
    #     st.image(rotated_image2, use_column_width=True)

with spacer:
    st.empty()

# content
with right_column:
    if option == "Enter Daily Scores":
        enter_daily_scores(app_config)

        st.write("")
        st.write("")
        image_path1 = "img/tucker.jpeg"  
        st.image(image_path1, use_column_width=True)

    elif option == "Monthly Competitions":
        monthly_competition(app_config)

        st.write("")
        st.write("")
        image_path2 = "img/sufi.jpeg"
        image2 = Image.open(image_path2)
        rotated_image2 = image2.rotate(270, expand=True)
        st.image(rotated_image2, use_column_width=True)

    elif option == "Player Statistics":
        player_statistics(app_config)

