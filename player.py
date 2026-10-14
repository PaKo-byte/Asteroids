import pygame

import circleshape
import constants


class Player(circleshape.CircleShape):
    def __init__(self, x:float, y:float):
        super().__init__(x, y, radius=constants.PLAYER_RADIUS)
        self.rotation = 0

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), width=constants.LINE_WIDTH)

    def rotate(self, dt:float) -> None:
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def move(self, dt:float) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * constants.PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector


    def update(self, dt: float) -> None:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                return self.rotate(-dt)
            if keys[pygame.K_RIGHT]:
                return self.rotate(dt)
            if keys[pygame.K_UP]:
                return self.move(dt)
            if keys[pygame.K_DOWN]:
                return self.move(-dt)
