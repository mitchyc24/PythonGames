import os
import pygame
from ui.button import Button


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


    def draw(self):
        self.window.fill((255, 0, 0))

    def get_games_list(self):
        return os.listdir("games")
    
    def start_pang(self):
        from games.pang.pang import PANG
        self.current_window = PANG()
        print("Pang started")



class Menu:
    def __init__(self, game_manager: GameManager):
        self.game_manager = game_manager
        self.font = pygame.font.Font(None, 36)
        self.buttons = [
            Button("Start Lang", self.game_manager.start_pang, 300, 300)
        ]
        self.running = True

    def get_canvas(self, size):
        self.draw(size)
        return self.canvas
    
    def draw(self, canvas: pygame.Surface):
        canvas.fill((0, 0, 0))
        self.draw_title(canvas)
        self.draw_buttons(canvas)

    def draw_title(self, canvas: pygame.Surface):
        text = self.font.render("Menu", True, (255, 255, 255))
        canvas.blit(text, (10, 10))

    def draw_buttons(self, canvas):
        for button in self.buttons:
            button.draw(canvas)

    def update(self):
        pass

    def check_event(self, event):
        for button in self.buttons:
            button.check_click(event)



