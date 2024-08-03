import streamlit as st
import pandas as pd

def wordle(
    app_config: dict,
    player_data: pd.DataFrame,
    selected_date,
    player: str,
    game: str
):
    """
    Function for adding wordle scores to data

    Args:
        app_config (dict): dictionary with app configs/inputs
        player_data (pd.DataFrame): dataframe with player scores
        selected_date (datetime): date to enter data for
        player (str): player to enter data for
        game (str): game to enter data for
    """
    # wordle scores
    wordle_score = st.selectbox("Wordle Score", [1, 2, 3, 4, 5, 6, "Failed"])

    # convert failed to numerical
    if wordle_score == "Failed":
        wordle_score = 7

    # submit scores
    if st.button("Submit Score"):
        new_score = pd.DataFrame({
            'Date': [selected_date],
            'Player': [player],
            'Game': [game],
            'Score': [wordle_score]
        })
        player_data = pd.concat([player_data, new_score], ignore_index=True)

        # save player data
        player_data_path = app_config["player_data"]
        player_data.to_csv(player_data_path, index=False)
        st.success(f"Score for {game} submitted successfully!")

    return player_data