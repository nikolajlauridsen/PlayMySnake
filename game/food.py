import pygame
import random

class Food(pygame.sprite.Sprite):
    """Class representing a food object in the game"""

    def __init__(self, screen, settings):
        super().__init__()

        self.screen = screen
        self.settings = settings

        # Load graphic
        self.image = pygame.Surface([10, 10])
        self.image.fill(self.settings.colors["green"])
        self.rect = self.image.get_rect()

        x_cord = random.randint(10, self.settings.screen_size[0]-10)
        y_cord = random.randint(10+self.settings.overlay_width,
                                self.settings.screen_size[1]-10)
        self.rect.centerx = x_cord
        self.rect.centery = y_cord

    def collision_detect(self, player, food_sprite):
        """Check if player has collided with food and thus "eaten" it"""
        hit_list = pygame.sprite.spritecollide(self, player.player_sprites, False)
        if len(hit_list) > 0:
            self.kill()  # Kill the food
            self.settings.score += 1  # Increase score
            player.add_segment()  # Add a segment to the player
            # create a new food
            food_sprite.add(Food(self.screen, self.settings))
