import streamlit as st
import pandas as pd

def mini(
    app_config: dict,
    player_data: pd.DataFrame,
    selected_date,
    player: str,
    game: str
):
    """
    Function for adding mini score

    Args:
        app_config (dict): dictionary with app configs/inputs
        player_data (pd.DataFrame): dataframe with player scores
        selected_date (datetime): date to enter data for
        player (str): player to enter data for
        game (str): game to enter data for
    """
    # mini scores
    mini_time = st.text_input("Mini Time (MM:SS)")

    # conevert time to seconds
    try:
        minutes, seconds = map(int, mini_time.split(":"))
        mini_score = minutes * 60 + seconds

        # submit score
        if st.button("Submit Score"):
            new_score = pd.DataFrame({
                'Date': [selected_date],
                'Player': [player],
                'Game': [game],
                'Score': [mini_score]
            })
            player_data = pd.concat([player_data, new_score], ignore_index=True)

            # save player data
            player_data_path = app_config["player_data"]
            player_data.to_csv(player_data_path, index=False)
            st.success(f"Score for {game} submitted successfully!")

    except ValueError:
        st.error("Please enter the time in MM:SS format.")

    return player_data