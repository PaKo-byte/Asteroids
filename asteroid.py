import pygame

import random
import circleshape
import constants
from logger import log_event


class Asteroid(circleshape.CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, width=constants.LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand_ang = random.uniform(20, 50)
            first_new_asteroid_velocity = self.velocity.rotate(rand_ang)
            second_new_asteroid_velocity = self.velocity.rotate(-rand_ang)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            first_asteroid.velocity = first_new_asteroid_velocity * 1.2
            second_asteroid.velocity = second_new_asteroid_velocity * 1.2
