from models.player import Player
from manager import Manager


def main():
    """
    initiate a player or tournament manager and store the data

    """
    player_manager = Manager(item_type=Player)
    player_manager.load_from_json("./JASON/players.json")
    print(player_manager.items)


if __name__ == "__main__":
    main()
