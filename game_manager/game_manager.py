import pygame

class PygameManager:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.games = []
        self.selected_game = None
        self.font = pygame.font.Font(None, 36)

    def add_game(self, game, name):
        self.games.append((game, name))

    def run(self):
        while self.running:
            self.show_menu()
            if self.selected_game:
                self.run_game(self.selected_game)

    def show_menu(self):
        menu_running = True
        while menu_running and self.running:
            self.screen.fill((0, 0, 0))
            y_offset = 100
            for index, (game, name) in enumerate(self.games):
                text_surface = self.font.render(f"{index + 1}. {name}", True, (255, 255, 255))
                self.screen.blit(text_surface, (100, y_offset))
                y_offset += 50

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    menu_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        menu_running = False
                    if pygame.K_1 <= event.key <= pygame.K_9:
                        index = event.key - pygame.K_1
                        if 0 <= index < len(self.games):
                            self.selected_game = self.games[index][0]
                            menu_running = False

            self.clock.tick(60)

    def run_game(self, game):
        game.run(self.screen)
        while game.running and self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    game.stop()
                    game.running = False
            self.screen.fill((0, 0, 0))  # Clear the screen
            game.update(self.clock.get_time() / 1000.0)
            game_surface = game.get_surface()
            if game_surface:
                self.screen.blit(game_surface, (0, 0))
            pygame.display.flip()
            self.clock.tick(60)