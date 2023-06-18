import pygame
import random
from game.components.powers.shield import Shield
from game.components.powers.gun import Gun
from game.utils.constants import SPACESHIP_SHIELD ,GUN_TYPE , SHIELD_TYPE, SCREEN_HEIGHT
from game.components.powers.power import Power


class PowerHandler:
    def __init__(self):
        self.powers = []
        self.when_appers = random.randint(4000,7000)
        self.duration = random.randint(5,15)


    def generate_power(self):
        self.powers.append(Shield())
        self.powers.append(Gun())
        self.when_appers += random.randint(4000,7000)


    def update(self,player):
        current_tipe = pygame.time.get_ticks()
        if len(self.powers) == 0 or current_tipe >= self.when_appers:
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
                if power.type == GUN_TYPE:
                    player.SHOOTING_TIME = 1
                elif power.type == SHIELD_TYPE:
                    player.set_power_image(SPACESHIP_SHIELD)
                    
    def reset(self):
        self.powers = []