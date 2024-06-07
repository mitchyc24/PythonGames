from game_manager.game_manager import PygameManager
from games.pang.pang import PangGame


if __name__ == "__main__":
    manager = PygameManager(800, 600)
    game1 = PangGame()
    manager.add_game(game1, "Pang Game")
    manager.run()