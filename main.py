import pygame
from game_manager import GameManager

pygame.init()

def run():
    game_manager = GameManager()
    game_manager.run()


if __name__ == "__main__":
    run()