import pygame
import random
from game.components.powers.shield import Shield
from game.utils.constants import SPACESHIP_SHIELD


class PowerHandler:
    def __init__(self):
        self.powers = []
        self.when_appers = random.randint(3000,7000)
        self.duration = random.randint(5,15)


    def generate_power(self):
        power = Shield()
        self.powers.append(power)
        self.when_appers += random.randint(3000,7000)


    def update(self,player):
        current_tipe = pygame.time.get_ticks()
        if len(self.powers) == 0 and current_tipe >= self.when_appers:
            self.generate_power()
        self.power_use(player)
        
    
    def draw(self,screen):
        for power in self.powers:
            power.draw(screen)

    
    def power_use(self,player):
        for power in self.powers:
            power.update()
            if player.rect.colliderect(power.rect):
                power.star_time = pygame.time.get_ticks()
                player.power_type = power.type  
                player.has_power = True
                player.power_time = power.star_time + (self.duration * 1000)
                player.set_power_image(SPACESHIP_SHIELD)