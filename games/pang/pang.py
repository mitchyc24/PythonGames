import pygame
from pygame.math import Vector2
import time

class PangGame:
    def __init__(self):
        self.running = True
        self.surface = None
        self.bubbles = []
        self.harpoons = []
        self.player_pos = Vector2(400, 550)
        self.player_speed = 200  # pixels per second

    def run(self, screen):
        width, height = screen.get_size()
        self.surface = pygame.Surface((width, height))
        self.bubbles.append(Bubble(Vector2(200, 100), 30, Vector2(100, -150)))  # Initial speed (px/s)
        self.running = True

    def stop(self):
        self.running = False

    def get_surface(self):
        self.draw()
        return self.surface

    def handle_events(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_pos.x -= self.player_speed * dt
        if keys[pygame.K_RIGHT]:
            self.player_pos.x += self.player_speed * dt
        if keys[pygame.K_SPACE]:
            self.shoot_harpoon()
        if keys[pygame.K_ESCAPE]:
            self.stop()

    def shoot_harpoon(self):
        harpoon_pos = self.player_pos.copy()
        self.harpoons.append(harpoon_pos)

    def update(self, dt):
        self.handle_events(dt)
        
        # Update harpoons
        for harpoon in self.harpoons:
            harpoon.y -= 400 * dt  # Harpoon speed (px/s)

        # Remove off-screen harpoons
        self.harpoons = [h for h in self.harpoons if h.y > 0]

        # Update bubbles
        for bubble in self.bubbles:
            bubble.update(dt, self.surface)

        # Check for collisions
        for bubble in self.bubbles[:]:
            for harpoon in self.harpoons:
                if (bubble.pos - harpoon).length() < bubble.radius:
                    self.bubbles.remove(bubble)
                    self.harpoons.remove(harpoon)
                    if bubble.radius > 10:
                        new_radius = bubble.radius // 2
                        self.bubbles.append(Bubble(bubble.pos, new_radius, Vector2(100, -150)))
                        self.bubbles.append(Bubble(bubble.pos, new_radius, Vector2(-100, -150)))
                    break

    def draw(self):
        self.surface.fill((0, 0, 0))
        # Draw player
        pygame.draw.rect(self.surface, (0, 255, 0), (int(self.player_pos.x) - 10, int(self.player_pos.y) - 10, 20, 20))

        # Draw harpoons
        for harpoon in self.harpoons:
            pygame.draw.line(self.surface, (255, 255, 255), (int(harpoon.x), int(harpoon.y)), (int(harpoon.x), int(harpoon.y) - 20), 2)

        # Draw bubbles
        for bubble in self.bubbles:
            bubble.draw(self.surface)


class Bubble:
    def __init__(self, pos, radius, speed):
        self.pos = Vector2(pos)
        self.radius = radius
        self.speed = Vector2(speed)
        self.gravity = Vector2(0, 9.8)  # Gravity acceleration (pixels per second^2)

    def update(self, dt, surface):
        self.speed += self.gravity * dt
        self.pos += self.speed * dt

        # Bounce on the sides
        if self.pos.x - self.radius <= 0 or self.pos.x + self.radius >= surface.get_width():
            self.speed.x = -self.speed.x

        # Bounce on the top and bottom
        if self.pos.y - self.radius <= 0 or self.pos.y + self.radius >= surface.get_height():
            self.speed.y = -self.speed.y
            # Ensure perfect elasticity
            if self.pos.y + self.radius >= surface.get_height():
                self.pos.y = surface.get_height() - self.radius
            elif self.pos.y - self.radius <= 0:
                self.pos.y = self.radius

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), (int(self.pos.x), int(self.pos.y)), self.radius)
