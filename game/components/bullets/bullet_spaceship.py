import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET, BULLET_PLAYER_TYPE

class BulletPlayer(Bullet):
    WIDTH = 9 
    HEIGTH = 32
    SPEED = 20

    def __init__(self, center):
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        self.type = BULLET_PLAYER_TYPE
        super().__init__(self.image,self.type, center)
        self.sound = pygame.mixer.Sound("game/assets/Music/shoot.wav")
        self.sound.play()
        self.sound.set_volume(0.1)

    def update(self,enemy):
        self.rect.y -= self.SPEED
        if self.rect.y <= 0:
            self.is_active = False
        super().update(enemy)
        if not enemy.is_alive:
            enemy.is_destroyed = True

    