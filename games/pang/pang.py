
import pygame
import time
from game_manager.game import Game

class PANG(Game):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(None, 36)
        self.running = True

    def draw(self, canvas: pygame.Surface):
        canvas.fill((255, 123, 123))
        self.draw_game_time(canvas)
        

    def update(self):
        self.time_str = time.strftime("%H:%M:%S", time.gmtime(time.time() - self.game_init_time))


    def check_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Game stopping")
                self.running = False
            if event.key == pygame.K_r:
                print("Game restarting")
                self.game_init_time = time.time()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse clicked")
 
        elif event.type == pygame.MOUSEMOTION:
            print(f"Mouse @ {event.pos}")

    def draw_game_time(self, canvas):
        text = self.font.render(self.time_str, True, (255, 255, 255))
        canvas.blit(text, (10, 10))