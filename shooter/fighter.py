import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from constants import FIGHTER_STEP
class Fighter:
    def __init__(self):
        self.image = pygame.image.load('images/fighter.png')
        self.width, self.height = self.image.get_size()
        self.x, self.y = SCREEN_WIDTH / 2 - self.width / 2, SCREEN_HEIGHT - self.height
        self.step = FIGHTER_STEP
        self.goes_left, self.goes_right = False, False

    def move_left(self):
        self.goes_left = True

    def move_right(self):
        self.goes_right = True

    def stop_moving(self):
        self.goes_left = False
        self.goes_right = False

    def update_pos(self):
        if self.goes_left and self.x >= self.step:
            self.x -= self.step

        if self.goes_right and self.x <= SCREEN_WIDTH - self.width - self.step:
            self.x += self.step