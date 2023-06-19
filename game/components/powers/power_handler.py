import pygame
import random
from game.components.powers.shield import Shield
from game.components.powers.gun import Gun
from game.utils.constants import SPACESHIP_SHIELD ,GUN_TYPE , SHIELD_TYPE, SCREEN_HEIGHT, GET_POWER_SOUND, SPACESHIP
from game.components.powers.power import Power


class PowerHandler:
    def __init__(self):
        self.powers = []
        self.when_appers = random.randint(4000,7000)
        self.duration = random.randint(5,15)


    def generate_power(self):
        self.random_power = random.randint(1,2)
        if self.random_power == 1:
            power = Shield()
        elif self.random_power == 2:
            power = Gun()
        self.powers.append(power)
        self.when_appers += random.randint(4000,7000)


    def update(self,player):
        current_tipe = pygame.time.get_ticks()
        if len(self.powers) == 0 or current_tipe >= self.when_appers:
            self.generate_power()
        self.power_use(player)
        
    
    def draw(self,screen):
        for power in self.powers:
            power.draw(screen)

    def delete_power_image(self,power,player):
        if power.rect.y >= SCREEN_HEIGHT or power.rect.colliderect(player.rect):
            power = self.powers.remove(power)

    
    def power_use(self,player):
        for power in self.powers:
            power.update()
            self.delete_power_image(power,player)
            if player.rect.colliderect(power.rect):
                power.star_time = pygame.time.get_ticks()
                player.power_type = power.type  
                player.has_power = True
                player.power_time = power.star_time + (self.duration * 1000)
                if power.type == SHIELD_TYPE:
                    player.set_power_image(SPACESHIP_SHIELD)
                    self.sound = pygame.mixer.Sound(GET_POWER_SOUND)
                    self.sound.play()
                    self.sound.set_volume(0.3)
                elif power.type == GUN_TYPE:
                    player.SHOOTING_TIME = 1
                    player.set_power_image(SPACESHIP)
                    self.sound = pygame.mixer.Sound(GET_POWER_SOUND)
                    self.sound.play()
                    self.sound.set_volume(0.3)
                    
    def reset(self):
        self.powers = []        