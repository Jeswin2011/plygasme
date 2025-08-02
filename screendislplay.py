import pygame

pygame.init()
width,height=500,500
d=pygame.display.set_mode((width,height))
#bg=pygame.image.load("images.png")
bg_transform=pygame.transform.scale(pygame.image.load("images.png").convert(),(width,height))
free=pygame.transform.scale(pygame.image.load("free.png").convert(),(250,250))
free_rect=free.get_rect(center=(250,250))
done=False
f=pygame.font.SysFont(None,45).render("Hello",True,pygame.Color("blue"))
while not done:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True

    d.blit(bg_transform,(0,0))
    d.blit(free,free_rect)
    d.blit(f,(250,50))
    pygame.display.flip()