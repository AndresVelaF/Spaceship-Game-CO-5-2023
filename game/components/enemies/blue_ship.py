import pygame

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2

class BlueShip(Enemy):
    WIDTH = 40
    HEIGHT = 60

    def __init__(self):
        self.image = ENEMY_2
        self.live = 1
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
        self.SPEED_X = 3
        self.SPEED_Y = 5
        self.INTERVAL = 50