
from game.utils.constants import SHIELD_TYPE
class Bullet:

    def __init__(self,image,type, center):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.is_active = True

    def update(self, object):
        if self.rect.colliderect(object.rect):
                object.is_alive = False
                self.is_active = False
                

    
    def draw(self,screen):
        screen.blit(self.image,self.rect)
