def placar():
    import pygame
    p = True
    fundo_placar = pygame.image.load(r'tela_placar_SDV.jpg')
    screen = pygame.display.set_mode([fundo_placar.get_width(), fundo_placar.get_height()])
    clock = pygame.time.Clock()
    sair_placar = pygame.Rect(1180,0,100,100)
    while p == True:
        for event in pygame.event.get():
    
        
            if event.type == pygame.QUIT:
                pygame.quit()
                p = False
                return


            if event.type == pygame.MOUSEBUTTONDOWN:
                if sair_placar.collidepoint(event.pos):
                    p = False
                    return
        
        
        pygame.draw.rect(screen,(0,0,0),sair_placar)
        screen.blit(fundo_placar,(0,0))
        pygame.display.flip()  
        clock.tick(60)
if __name__ == '__main__':
    import pygame
    pygame.init()
    placar()
    pygame.quit()