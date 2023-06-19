import pygame
from pygame.font import Font
from game.utils.constants import FONT_DEFAULT, SCREEN_WIDTH, SCREEN_HEIGHT
pygame.font.init()

def get_message(message, size, color, width = SCREEN_WIDTH // 2, height = SCREEN_HEIGHT // 2, FONT_TYPE=FONT_DEFAULT):
    font = Font(FONT_TYPE, size)
    text = font.render(message, True, color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect

def get_image(image, width = SCREEN_WIDTH //2 , height = SCREEN_HEIGHT // 2):
    image = image
    image  = pygame.transform.scale(image, (200,70))
    rect = image.get_rect()
    rect.center = (width,height)
    return image, rect