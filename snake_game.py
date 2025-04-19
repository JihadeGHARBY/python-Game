import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Define display dimensions
WIDTH = 600
HEIGHT = 400

# Create the game window
game_window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Set the clock for controlling frame rate
clock = pygame.time.Clock()

# Define snake block size and speed
BLOCK_SIZE = 10
SNAKE_SPEED = 15

# Define fonts for displaying messages
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def display_score(score):
    """Display the player's score on the screen."""
    value = score_font.render("Your Score: " + str(score), True, YELLOW)
    game_window.blit(value, [0, 0])


def draw_snake(block_size, snake_list):
    """Draw the snake on the screen."""
    for x in snake_list:
        pygame.draw.rect(game_window, GREEN, [x[0], x[1], block_size, block_size])


def message(msg, color):
    """Display a message on the screen."""
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [WIDTH / 6, HEIGHT / 3])


def game_loop():
    """Main game loop."""
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    # Change in position
    x1_change = 0
    y1_change = 0

    # Snake body (list of blocks)
    snake_list = []
    snake_length = 1

    # Food position
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0

    while not game_over:

        while game_close:
            # Display game over message
            game_window.fill(BLUE)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            display_score(snake_length - 1)
            pygame.display.update()

            # Handle quit or restart
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        # Check for boundary collision
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        # Update snake position
        x1 += x1_change
        y1 += y1_change

        # Fill the background
        game_window.fill(BLACK)

        # Draw the food
        pygame.draw.rect(game_window, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # Update snake body
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for collision with itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw the snake
        draw_snake(BLOCK_SIZE, snake_list)

        # Display the score
        display_score(snake_length - 1)

        # Update the display
        pygame.display.update()

        # Check if the snake eats the food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            snake_length += 1

        # Control the game speed
        clock.tick(SNAKE_SPEED)

    # Quit pygame
    pygame.quit()
    quit()


# Start the game
game_loop()