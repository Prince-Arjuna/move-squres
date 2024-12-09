import pygame  # type: ignore
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = pygame.Rect(300, 250, 50, 50)
player2 = pygame.Rect(400,250,50,50)
font = pygame.font.SysFont('Arial', 30)
text_surface = font.render("Use wasd to move pink square", True, (255, 255, 255))  
text_surface2 = font.render("Use arrow keys to move pink square", True, (155, 155,255))

run = True
while run:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 50, 100), player)
    pygame.draw.rect(screen,(232,153,102),player2)
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]: 
        player2.move_ip(-1, 0)
    elif key[pygame.K_RIGHT]:  
        player2.move_ip(1, 0)
    elif key[pygame.K_UP]:  
        player2.move_ip(0, -1)
    elif key[pygame.K_DOWN]:  
        player2.move_ip(0, 1)
    key = pygame.key.get_pressed()
    if key[pygame.K_a]: 
        player.move_ip(-1, 0)
    elif key[pygame.K_d]:  
        player.move_ip(1, 0)
    elif key[pygame.K_w]:  
        player.move_ip(0, -1)
    elif key[pygame.K_s]:  
        player.move_ip(0, 1)
    if player.x > 748 + (player.height - 50):
        player.x = 748
    if player.x < 0:
        player.x = 0
    if player.y > 352:
        player.y = 352
    if player.y < 0:
        player.y = 0
    if player2.x > 748 + (player.height - 50):
        player2.x = 748
    if player2.x < 0:
        player2.x = 0
    if player2.y > 352:
        player2.y = 352
    if player2.y < 0:
        player2.y = 0
    #screen = pygame.display.set_mode((800, 600))  
    # screen.fill((0, 0, 0)) 
    screen.blit(text_surface, (100, 100))  # Position the text
    screen.blit(text_surface2, (100,200))
    pygame.display.flip()  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
