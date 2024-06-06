import os
import pygame
from game_manager.menu import Menu


WINDOW_SIZE = (800, 600)

class GameManager:
    def __init__(self):
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Python Games")
        pygame.display.set_icon(pygame.image.load(os.path.join("assets", "knight.png")))
        self.running = True
        self.menu = Menu(self)
        self.current_window = self.menu



    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_g:
                        print(self.get_games_list())
                    if event.key == pygame.K_m:
                        self.current_window = self.menu

                if self.current_window:
                    self.current_window.check_event(event)

            if self.current_window:
                if self.current_window.running:
                    self.current_window.update()
                    self.current_window.draw(self.window)
                else:
                    self.current_window = self.menu
            else:
                self.draw()
            pygame.time.Clock().tick(60)
            pygame.display.flip()

        pygame.quit()

    def stop(self):
        self.running = False
        
    def draw(self):
        self.window.fill((255, 0, 0))

    def get_games_list(self):
        return os.listdir("games")
    
    def start_pang(self):
        from games.pang.pang import PANG
        self.current_window = PANG()
        print("Pang started")