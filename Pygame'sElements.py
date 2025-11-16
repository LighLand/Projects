import pygame
pygame.init()
pygame.font.init()
screenwidth, screenheight = 640,480
sprite_width, sprite_height = 100,50
screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("Pygame's Elements")
screen.fill((255,255,255))
pygame.draw.rect(screen, (255,255,10), ((screenwidth-sprite_width)/2, (screenheight-sprite_height)/2,sprite_width, sprite_height))
Text = pygame.font.Font(None, 36).render("Hello Pygame!", True, (0,0,0))
screen.blit(Text, ((screenwidth-Text.get_width())/2, (screenheight-Text.get_height())/2+60))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()