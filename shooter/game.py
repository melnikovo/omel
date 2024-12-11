import pygame
from fighter import Fighter
from alien import Alien
from rocket import Rocket
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_FILL_COLOR, GAME_CAPTION
import sys

class Game:
    def __init__(self):
        self.screen_width, self.screen_height = SCREEN_WIDTH, SCREEN_HEIGHT
        self.screen_fill_color = SCREEN_FILL_COLOR
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(GAME_CAPTION)
        self.game_font = pygame.font.Font(None, 30)
        self.game_score = 0

        self.fighter = Fighter()
        self.alien = Alien()
        self.rocket = Rocket(self.fighter)

        self.game_is_running = True

    def run(self):
        while self.game_is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                self.handle_key_events(event)
            self.update_game_state()
            self.draw()
        self.show_game_over()
    def handle_key_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.fighter.move_left()
            if event.key == pygame.K_RIGHT:
                self.fighter.move_right()

            if event.key == pygame.K_SPACE:
                self.rocket.fire()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.fighter.stop_moving()

    def update_game_state(self):
        self.fighter.update_pos()
        self.alien.update_pos()
        self.rocket.update_pos()

        if self.rocket.is_out_of_screen():
            self.rocket.reset()

        if self.rocket.is_collision(self.alien):
            self.rocket.reset()
            self.alien.reset()
            self.game_score += 1

        if self.alien.reached_fighter(self.fighter):
            self.game_is_running = False

    def draw(self):
        self.screen.fill(self.screen_fill_color)
        self.screen.blit(self.fighter.image, (self.fighter.x, self.fighter.y))
        self.screen.blit(self.alien.image, (self.alien.x, self.alien.y))
        if self.rocket.was_fired:
            self.screen.blit(self.rocket.image, (self.rocket.x, self.rocket.y))
        self.show_game_score()
        pygame.display.update()

    def show_game_score(self):
        game_score_text = self.game_font.render(f"Ur Gamus Core is: {self.game_score}", True, "white")
        self.screen.blit(game_score_text, (20, 20))

    def show_game_over(self):
        game_over_text = self.game_font.render("Game Over", True, 'white')
        game_over_rectangle = game_over_text.get_rect()
        game_over_rectangle.center = (self.screen_width / 2, self.screen_height / 2)
        self.screen.blit(game_over_text, game_over_rectangle)
        pygame.display.update()
        pygame.time.wait(5000)