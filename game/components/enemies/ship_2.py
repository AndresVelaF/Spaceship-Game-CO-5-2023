import pygame

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2

class Ship_2(Enemy):
    WIDTH = 40
    HEIGHT = 60

    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
        SPEED_X = 3
        SPEED_Y = 1
        INTERVAL = 50