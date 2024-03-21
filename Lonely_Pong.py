import pygame, sys, random

pygame.init()

WIDTH, HEIGHT = 1280, 720

FONT = pygame.font.SysFont("Consolas", int(WIDTH/20))

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lonely Pong")

CLOCK = pygame.time.Clock()

#Paddles

player = pygame.Rect(WIDTH-110,HEIGHT/2-50, 10, 100 )
opponent = pygame.Rect(110, HEIGHT/2 - 50, 10, 100 )

A_score, B_score = 0, 0
# ball

ball = pygame.Rect(WIDTH/2-10, HEIGHT/2-10, 20, 20)
x_speed , y_speed= 1, 1

while True:

    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_UP]:
        if player.top > 0:
            player.top -=2

        if opponent.bottom < HEIGHT:
            opponent.bottom +=2
            
    elif key_pressed[pygame.K_DOWN]:
        if player.bottom < HEIGHT:
            player.bottom +=2

        if opponent.top > 0:
            opponent.top -=2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    #ball logic

    if ball.y >= HEIGHT:
        y_speed = -1
    if ball.y <= 0:
        y_speed = 1
    if ball.x <= 0:
        A_score =0
        ball.center =(WIDTH/2, HEIGHT/2)
        x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
    if ball.x >= WIDTH:
        A_score =0
        ball.center =(WIDTH/2, HEIGHT/2)
        x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])

    if player.x - ball.width <= ball.x <= player.x and ball.y in range (player.top - ball.width, player.bottom + ball.width):
        x_speed = -1
        A_score +=1
    
    if opponent.x - ball.width <= ball.x <= opponent.x and ball.y in range (opponent.top - ball.width, opponent.bottom + ball.width):
        x_speed = 1
        A_score +=1 

    ball.x +=x_speed * 2
    ball.y += y_speed * 2
    SCREEN.fill("black")
    
    player_A_score = FONT.render(str(A_score), True, "white")
    game_name = FONT.render(str('Lonely Pong'), True, "pink")

    pygame.draw.rect(SCREEN, "white", player)
    pygame.draw.rect(SCREEN, "red", opponent)
    pygame.draw.circle(SCREEN, "green", ball.center, 10)

    SCREEN.blit(player_A_score, (WIDTH/2 , 100))
    SCREEN.blit(game_name, (WIDTH/2 - 180 , 20))

    pygame.display.update()
    CLOCK.tick(300)