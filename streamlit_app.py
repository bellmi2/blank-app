import pygame
import sys
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("벽돌깨기")

clock = pygame.time.Clock()

# 색상
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (50,150,255)
RED = (255,80,80)
GREEN = (80,255,80)
YELLOW = (255,220,0)

font = pygame.font.SysFont("malgungothic", 30)

# 패들
paddle = pygame.Rect(WIDTH//2-60, HEIGHT-40, 120, 15)
paddle_speed = 8

# 공
ball = pygame.Rect(WIDTH//2, HEIGHT//2, 15,15)
ball_dx = random.choice([-5,5])
ball_dy = -5

# 벽돌
brick_rows = 6
brick_cols = 10
brick_width = 70
brick_height = 25

bricks=[]

for row in range(brick_rows):
    for col in range(brick_cols):
        brick = pygame.Rect(
            40+col*(brick_width+5),
            50+row*(brick_height+5),
            brick_width,
            brick_height
        )
        bricks.append(brick)

score = 0

running=True

while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        paddle.x -= paddle_speed

    if keys[pygame.K_RIGHT]:
        paddle.x += paddle_speed

    if paddle.left<0:
        paddle.left=0

    if paddle.right>WIDTH:
        paddle.right=WIDTH

    # 공 이동
    ball.x += ball_dx
    ball.y += ball_dy

    # 벽 충돌
    if ball.left<=0 or ball.right>=WIDTH:
        ball_dx *= -1

    if ball.top<=0:
        ball_dy *= -1

    # 게임오버
    if ball.bottom>=HEIGHT:
        text=font.render("GAME OVER",True,RED)
        screen.fill(BLACK)
        screen.blit(text,(WIDTH//2-90,HEIGHT//2))
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

    # 패들 충돌
    if ball.colliderect(paddle):
        ball_dy = -abs(ball_dy)

        hit_pos=(ball.centerx-paddle.left)/paddle.width
        ball_dx=(hit_pos-0.5)*12

    # 벽돌 충돌
    hit = ball.collidelist(bricks)

    if hit != -1:
        bricks.pop(hit)
        ball_dy *= -1
        score += 10

    # 클리어
    if len(bricks)==0:
        text=font.render("CLEAR!",True,GREEN)
        screen.fill(BLACK)
        screen.blit(text,(WIDTH//2-50,HEIGHT//2))
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

    # 화면
    screen.fill(BLACK)

    pygame.draw.rect(screen,BLUE,paddle)
    pygame.draw.ellipse(screen,WHITE,ball)

    colors=[RED,GREEN,YELLOW]

    for i,brick in enumerate(bricks):
        pygame.draw.rect(screen,colors[(brick.y//30)%3],brick)

    score_text=font.render(f"점수 : {score}",True,WHITE)
    screen.blit(score_text,(10,10))

    pygame.display.flip()
