import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
BALL_SIZE = 20
BRICK_WIDTH, BRICK_HEIGHT = 80, 30
BRICK_ROWS, BRICK_COLS = 5, 10
BRICK_GAP = 5
BG_COLOR = (0, 0, 0)
PADDLE_COLOR = (255, 255, 255)
BALL_COLOR = (0, 0, 255)

# Paddle speed
PADDLE_SPEED = 8  # Increase this value to make the paddle faster

# Define different brick colors
BRICK_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brick Breaker")

# Create the paddle
paddle = pygame.Rect((SCREEN_WIDTH - PADDLE_WIDTH) // 2, SCREEN_HEIGHT - PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create the ball
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed = [random.choice((1, -1)) * 5, -5]

# Create bricks with random colors and gaps
bricks = []
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        brick_x = col * (BRICK_WIDTH + BRICK_GAP)
        brick_y = row * (BRICK_HEIGHT + BRICK_GAP) + 50
        brick = pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT)
        brick_color = random.choice(BRICK_COLORS)
        bricks.append((brick, brick_color))

# Initialize score
score = 0

# Game over conditions
game_over = False
win = False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        # Move the paddle to the left, but stay within screen boundaries
        paddle.x -= PADDLE_SPEED
        if paddle.left < 0:
            paddle.left = 0
    if keys[pygame.K_RIGHT]:
        # Move the paddle to the right, but stay within screen boundaries
        paddle.x += PADDLE_SPEED
        if paddle.right > SCREEN_WIDTH:
            paddle.right = SCREEN_WIDTH

    if not game_over:
        # Move the ball
        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

        # Ball collisions
        if ball.colliderect(paddle):
            ball_speed[1] = -5

        for brick, brick_color in bricks:
            if ball.colliderect(brick):
                bricks.remove((brick, brick_color))
                ball_speed[1] = 5
                score += 2

        if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
            ball_speed[0] = -ball_speed[0]
        if ball.top <= 0:
            ball_speed[1] = -ball_speed[1]

        if ball.bottom >= SCREEN_HEIGHT:
            game_over = True

    # Check if all bricks are destroyed
    if not bricks:
        game_over = True
        win = True

    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, PADDLE_COLOR, paddle)
    pygame.draw.ellipse(screen, BALL_COLOR, ball)

    for brick, brick_color in bricks:
        pygame.draw.rect(screen, brick_color, brick)

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Display game over text
    if game_over:
        if win:
            game_over_text = font.render("You Win", True, (0, 255, 0))
        else:
            game_over_text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 18))

    pygame.display.update()
    pygame.time.delay(30)

pygame.quit()