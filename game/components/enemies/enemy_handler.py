from game.components.enemies.ship import Ship
from game.components.enemies.ship_2 import Ship_2

class EnemyHandler:
    def __init__(self):
        self.enemies = []

    def update(self, bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if not enemy.is_alive :
                self.remove_enemy(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 2:
            self.enemies.append(Ship())
            self.enemies.append(Ship_2())

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)