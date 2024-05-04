import pygame
import random

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("Pong")

    clock = pygame.time.Clock()
    started = False
    score = 0 

    paddle_1_rect = pygame.Rect(30, SCREEN_HEIGHT/2 - 50, 7, 100)
    paddle_2_rect = pygame.Rect(SCREEN_WIDTH - 50, SCREEN_HEIGHT/2 - 50, 7, 100)

    paddle_1_move = 0
    paddle_2_move = 0

    ball_rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 25, 25)

    ball_accel_x = random.randint(2, 4) * 0.1
    ball_accel_y = random.randint(2, 4) * 0.1

    if random.randint(1, 2) == 1:
        ball_accel_x *= -1
    if random.randint(1, 2) == 1:
        ball_accel_y *= -1

    while True:
        screen.fill(COLOR_BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            # Contrôles du jeu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    started = True
                if event.key == pygame.K_z:
                    paddle_1_move = -0.5
                if event.key == pygame.K_s:
                    paddle_1_move = 0.5
                if event.key == pygame.K_UP:
                    paddle_2_move = -0.5
                if event.key == pygame.K_DOWN:
                    paddle_2_move = 0.5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_z or event.key == pygame.K_s:
                    paddle_1_move = 0.0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    paddle_2_move = 0.0

        if not started:
            font = pygame.font.SysFont('Consolas', 30)
            text = font.render('Press Space to Start', True, COLOR_WHITE)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text, text_rect)
            # Afficher le score même lorsque le jeu n'a pas démarré
            font = pygame.font.SysFont('Consolas', 24)
            score_text = font.render(f'Score: {score}', True, COLOR_WHITE)
            screen.blit(score_text, (10, 10))
            # Réinitialiser le score lorsque le jeu n'a pas démarré
            score = 0
        else:
            pygame.draw.rect(screen, COLOR_WHITE, paddle_1_rect)
            pygame.draw.rect(screen, COLOR_WHITE, paddle_2_rect)
            pygame.draw.rect(screen, COLOR_WHITE, ball_rect)

            if ball_rect.left <= 0 or ball_rect.right >= SCREEN_WIDTH:
                ball_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                paddle_1_rect.center = (30, SCREEN_HEIGHT / 2)
                paddle_2_rect.center = (SCREEN_WIDTH - 50, SCREEN_HEIGHT / 2)
                started = False
                score = 0

            if ball_rect.top <= 0 or ball_rect.bottom >= SCREEN_HEIGHT:
                ball_accel_y *= -1

            if paddle_1_rect.colliderect(ball_rect) or paddle_2_rect.colliderect(ball_rect):
                ball_accel_x *= -1
                score += 1 
                

            ball_rect.left += ball_accel_x * clock.get_time()
            ball_rect.top += ball_accel_y * clock.get_time()

            paddle_1_rect.top += paddle_1_move * clock.get_time()
            paddle_2_rect.top += paddle_2_move * clock.get_time()

            if paddle_1_rect.top < 0:
                paddle_1_rect.top = 0
            if paddle_1_rect.bottom > SCREEN_HEIGHT:
                paddle_1_rect.bottom = SCREEN_HEIGHT

            if paddle_2_rect.top < 0:
                paddle_2_rect.top = 0
            if paddle_2_rect.bottom > SCREEN_HEIGHT:
                paddle_2_rect.bottom = SCREEN_HEIGHT

        font = pygame.font.SysFont('Consolas', 24)
        score_text = font.render(f'Score: {score}', True, COLOR_WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()

