import pygame


class Button:
    def __init__(self, text, callback, x, y):
        self.text = text
        self.callback = callback
        self.font = pygame.font.Font(None, 36)
        self.width = 200
        self.height = 50
        self.colour = (0, 127, 0)
        self.on_hover_colour = (0, 200, 0)
        self.text_rendered = self.font.render(self.text, True, (255, 255, 255))
        self.text_width = self.text_rendered.get_width()
        self.text_height = self.text_rendered.get_height()
        self.x = x
        self.y = y

    def draw(self, canvas):
        if self.is_hovered():
            pygame.draw.rect(canvas, self.on_hover_colour, (self.x, self.y, self.width, self.height), border_radius=10)
        else:
            pygame.draw.rect(canvas, self.colour, (self.x, self.y, self.width, self.height), border_radius=10)
        canvas.blit(self.text_rendered, (self.x + self.width // 2 - self.text_width // 2, self.y + self.height // 2 - self.text_height // 2))

    def is_hovered(self):
        x, y = pygame.mouse.get_pos()
        return self.x < x < self.x + self.width and self.y < y < self.y + self.height

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered():
                self.on_click()

    def on_click(self):
        self.callback()