import pygame
import random
from logger import log_event
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random.uniform(20, 50)
            first_vector = self.velocity.rotate(15)
            second_vector = self.velocity.rotate(-15)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            split1 = Asteroid(self.position.x, self.position.y, new_radius)
            split2 = Asteroid(self.position.x, self.position.y, new_radius)
            split1.velocity = first_vector * 1.2
            split2.velocity = second_vector * 1.2
