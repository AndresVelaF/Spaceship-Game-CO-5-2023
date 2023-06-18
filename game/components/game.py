import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, WHITE_COLOR ,BLUE_COLOR, DEFAULT_TYPE, FONT_IMPACT
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.bullets.bullet_handler import BulletHandler
from game.components.powers.power_handler import PowerHandler
from game.components import text_utils

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_handler = EnemyHandler()
        self.bullet_handler = BulletHandler()
        self.PowerHandler = PowerHandler()
        self.score = 0
        self.number_death = 0
        self.max_score = 0


    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                self.reset()

    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.player.update(user_input,self.bullet_handler)
            self.enemy_handler.update(self.bullet_handler)
            self.bullet_handler.update(self.player,self.enemy_handler.enemies)
            self.score = self.enemy_handler.number_enemy_destroyed
            self.PowerHandler.update(self.player)
            if not self.player.is_alive:
                pygame.time.delay(500)
                self.playing = False
                self.number_death += 1



    def draw(self):
        self.draw_background()
        if self.playing:
            self.clock.tick(FPS)
            self.player.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.PowerHandler.draw(self.screen)
            self.draw_score()
            self.draw_power_time()
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_menu(self):
        if self.number_death == 0:
            textr, text_rectr = text_utils.get_message("Welcome to Spaceship", 40, WHITE_COLOR,height= SCREEN_HEIGHT//2 - 50,FONT_TYPE=FONT_IMPACT)
            text, text_rect = text_utils.get_message("Press any Key to Start", 30, WHITE_COLOR)
            self.screen.blit(textr, text_rectr)
            self.screen.blit(text, text_rect)
        else:
            if self.max_score < self.score:
                self.max_score = self.score
            text,text_rect = text_utils.get_message("press Any Key to Restar",30,WHITE_COLOR)
            score,score_rect = text_utils.get_message(f"your score is: {self.score}",30,WHITE_COLOR,height= SCREEN_HEIGHT//2 +50)
            number_death,number_death_rect = text_utils.get_message(f"you have died {self.number_death} times",30,WHITE_COLOR,height= SCREEN_HEIGHT//2 +100)
            max_score,max_score_rect = text_utils.get_message(f"your max score is :{self.max_score}",30,BLUE_COLOR,height= SCREEN_HEIGHT//2 - 50)
            self.screen.blit(max_score,max_score_rect)
            self.screen.blit(number_death,number_death_rect)
            self.screen.blit(text,text_rect)
            self.screen.blit(score,score_rect)

    def draw_score(self):
        score, score_rect = text_utils.get_message(f'Your score is {self.score}', 20, WHITE_COLOR, 1000, 40)
        self.screen.blit(score, score_rect)

    def draw_power_time(self):
        if self.player.has_power:
            power_time = round((self.player.power_time - pygame.time.get_ticks())/1000,1)
            if power_time >= 0:
                text,text_rect = text_utils.get_message(f"{self.player.power_type.capitalize()} is enable for : {power_time} ", 15, WHITE_COLOR, 150, 50)
                self.screen.blit(text,text_rect)
            else:
                self.player.has_power = False
                self.player.power_type = DEFAULT_TYPE
                self.player.set_default_image()


    def reset(self):
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        self.PowerHandler.reset()
