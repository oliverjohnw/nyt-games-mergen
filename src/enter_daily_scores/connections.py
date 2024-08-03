import streamlit as st
import pandas as pd

def connections(
    app_config: dict,
    player_data: pd.DataFrame,
    selected_date,
    player: str,
    game: str
):
    """
    Functions for adding connections scores

    Args:
        app_config (dict): dictionary with app configs/inputs
        player_data (pd.DataFrame): dataframe with player scores
        selected_date (datetime): date to enter data for
        player (str): player to enter data for
        game (str): game to enter data for
    """
    # connection scores
    connections_score = st.selectbox("Connections Score", ["0 Mistakes", "1 Mistake", "2 Mistakes", "3 Mistakes", "Failed"])

    # convert to mapping
    score_mapping = {
        "0 Mistakes": 0,
        "1 Mistake": 1,
        "2 Mistakes": 2,
        "3 Mistakes": 3,
        "Failed": 4 
    }
    connections_score = score_mapping[connections_score]

    # submit scores
    if st.button("Submit Score"):
        new_score = pd.DataFrame({
            'Date': [selected_date],
            'Player': [player],
            'Game': [game],
            'Score': [connections_score]
        })
        player_data = pd.concat([player_data, new_score], ignore_index=True)

        # save player data
        player_data_path = app_config["player_data"]
        player_data.to_csv(player_data_path, index=False)
        st.success(f"Score for {game} submitted successfully!")

    return player_data