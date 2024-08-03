# local imports
from src.utils import read_file

def load_player_data(
    app_config: dict
):
    """
    Loads player data
    
    Args:
        app_config (dict): dictionary with app configs/inputs
    
    Returns:
        player_data (pd.DataFrame): dataframe with player scores
    """
    # load player data
    player_data_path = app_config["player_data"]
    player_data = read_file(player_data_path)

    return player_data