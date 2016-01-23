import pull
import game

data = pull.data()['results']['collection1']
def organize():
    current_games = []
    for collection in data:
        current_games.append(game.Game(collection))
    return current_games
