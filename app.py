import pygame, sys , random

#Functions
def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    #Bounds
    if ball.top <=0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        player_score += 1
        ball_start()
    
    if ball.right >= screen_width:
        opponent_score += 1
        ball_start()

    #Collision
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
def player_animation():
    player.y += player_speed
    if player.top <=0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height     
def opponent_animation():
    opponent.y += opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
def ball_start():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y*= random.choice((1,-1))
    ball_speed_x*= random.choice((1,-1))

# General Setup
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

# Main Window
screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height)) #Screen Size
pygame.display.set_caption('Pong') #Title

#Game Rectangles/Assets
ball = pygame.Rect(screen_width/2 - 10, screen_height/2 - 10,20,20) #position and size
player = pygame.Rect(screen_width - 20, screen_height/2 - 70,10,140)
opponent = pygame.Rect(10, screen_height/2 - 70,10,140)

#Colors
bg_color = (255,250,240)
light_grey = (200,255,255)
ball_color = (0,0,0)
line_color = (0,0,0,2)
primary_color = (255,165,0)
secondary_color = (125,38,205)

#Speed
ball_speed_x = 4 * random.choice((1,-1))
ball_speed_y = 4 * random.choice((1,-1))
player_speed = 0
opponent_speed = 0
speed = 8

#Text Variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font('freesansbold.ttf', 20)

#Gameplay Loop
while True:
    #Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += speed
            if event.key == pygame.K_UP:
                player_speed -= speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= speed
            if event.key == pygame.K_UP:
                player_speed += speed

        #Opponent Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                opponent_speed += speed
            if event.key == pygame.K_s:
                opponent_speed -= speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                opponent_speed -= speed
            if event.key == pygame.K_s:
                opponent_speed += speed
         
    #Game Logic
    ball_animation()
    player_animation()
    opponent_animation()
    
    #Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen,primary_color,player)
    pygame.draw.rect(screen,secondary_color,opponent)
    pygame.draw.ellipse(screen,ball_color,ball)
    pygame.draw.aaline(screen, line_color, (screen_width/2,0), (screen_width/2,screen_height))

    player_text = game_font.render(f"{player_score}", True, ball_color)
    screen.blit(player_text, (380,220))

    opponent_text = game_font.render(f"{opponent_score}", True, ball_color)
    screen.blit(opponent_text, (330,220))
    
    #Updating the window
    pygame.display.flip()
    clock.tick(60) #Frames per second