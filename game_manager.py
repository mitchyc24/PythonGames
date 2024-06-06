import os
import pygame



class GameManager:
    def __init__(self):
        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Python Games")
        pygame.display.set_icon(pygame.image.load(os.path.join("assets", "knight.png")))
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.window.fill((0, 0, 0))
            pygame.display.flip()
            pygame.time.Clock().tick(60)

        pygame.quit()


