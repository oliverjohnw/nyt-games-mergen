import streamlit as st
import pandas as pd

def strands(
    app_config: dict,
    player_data: pd.DataFrame,
    selected_date,
    player: str,
    game: str
):
    """
    Function for adding strands scores

    Args:
        app_config (dict): dictionary with app configs/inputs
        player_data (pd.DataFrame): dataframe with player scores
        selected_date (datetime): date to enter data for
        player (str): player to enter data for
        game (str): game to enter data for
    """
    # strands scores
    spanagram_score = st.selectbox("Spanagram Score", [1, 2, 3, 4, 5, 6, 7, 8, "Failed"])

    if spanagram_score == "Failed":
        spanagram_score = 9 

    hint_used = st.selectbox("Hint Used", ["Yes", "No"])
    hint_score = 1 if hint_used == "Yes" else 0

    # submit score
    if st.button("Submit Score"):
        new_score = pd.DataFrame({
            'Date': [selected_date],
            'Player': [player],
            'Game': [game],
            'Spanagram Score': [spanagram_score],
            'Hint Used': [hint_score]
        })
        player_data = pd.concat([player_data, new_score], ignore_index=True)

        # save player data
        player_data_path = app_config["player_data"]
        player_data.to_csv(player_data_path, index=False)
        st.success(f"Score for {game} submitted successfully!")

    return player_data