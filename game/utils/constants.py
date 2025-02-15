import pygame
import os



# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield_rm.png'))
HEAVY_MACHINE_GUN = pygame.image.load(os.path.join(IMG_DIR, 'Other/powerH.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))
HEART_LIVE = pygame.image.load(os.path.join(IMG_DIR, 'Other/Heart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
GUN_TYPE = 'gun'

BUTTON_PLAY = pygame.image.load(os.path.join(IMG_DIR, "Other/playGrande.png"))

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))

FONT_DEFAULT = 'freesansbold.ttf'
FONT_IMPACT = 'game/assets/Fonts/GasoekOne-Regular.ttf'
FONT_ARIAL = 'arial.ttf'

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
BLUE_COLOR = (0, 0, 255)

BULLET_ENEMY_TYPE = "enemy"
BULLET_PLAYER_TYPE = "player"

GET_POWER_SOUND = "game/assets/Music/super-mario-coin-sound.wav"
