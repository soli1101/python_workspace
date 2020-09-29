import pygame

#[0]
pygame.init()
isRunning = True
screen = pygame.display.set_mode((400,700))
pygame.display.set_caption("Space Battle")

#[0]
while isRunning:
    
    #[0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    #[0]
    pygame.display.update()


#[0]
pygame.quit()

