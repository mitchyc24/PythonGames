import pygame

from ui.button import Button

class Menu:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.font = pygame.font.Font(None, 36)
        self.buttons = [
            Button("Start Lang", self.game_manager.start_pang, 300, 300),
            Button("EXIT", self.game_manager.stop, 300, 400)
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

