import pygame
import sys

from game.settings import Settings
from game.player import Player
from game.food import Food
from game.buttons import Button
from game.menu import StringWriter
import game.events as event_handler


def main():
    # --- Set the Stage ---
    pygame.init()

    # Create settings object
    settings = Settings()

    # Create Screen
    screen = pygame.display.set_mode(settings.screen_size)
    pygame.display.set_caption("Danger Noodle")

    # Create clock
    clock = pygame.time.Clock()

    # Running flags
    app_running = True


    # Create initial sprites
    player = Player(screen, settings)
    player.create_snake()
    player.go_down()
    food_sprite = pygame.sprite.GroupSingle(Food(screen, settings))
    # Menu buttons
    play_button_x = settings.screen_size[0]/2
    play_button_y = settings.screen_size[1]/2
    play_button = Button(play_button_x, play_button_y, 200, 50, settings.colors["green"], "Play", screen)
    exit_button = Button(play_button_x, play_button_y+75, 200, 50, settings.colors["green"], "Exit", screen)
    
    # Menu text
    string_writer = StringWriter(screen)

    # Game menu
    while app_running:
        # Game loop
        screen.fill(settings.colors["grey"])
        play_button.draw_button()
        exit_button.draw_button()
        string_writer.draw_string("Danger Noodle", 75,
                                  settings.screen_size[0] // 2,
                                  (settings.screen_size[1] // 2) - 200)
        event_handler.check_menu_events(play_button, exit_button, settings)

        while settings.game_running:
            # Handle events
            event_handler.check_events(player)
            # Fill the screen and redraw objects
            screen.fill(settings.colors["grey"])
            food_sprite.sprite.collision_detect(player, food_sprite)
            player.update()
            player.draw(screen)
            food_sprite.draw(screen)
            settings.render_score(screen)
            # Wait for clock
            clock.tick(10 + (settings.score//4))
            # Refresh the screen
            pygame.display.flip()

        # Limit menu to 60 fps
        clock.tick(60)
        # Draw menu screen
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()