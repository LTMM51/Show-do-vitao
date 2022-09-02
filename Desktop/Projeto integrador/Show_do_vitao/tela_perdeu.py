def perdeu(respostas,login,senha):
    import pygame
    from tela_comeco import tela_comeco
    from SomarPontos import SomarPontos

    perdeste = True
    fonte= pygame.font.Font(None, 60)
    fundo_perdeu = pygame.image.load(r'tela_perdeste_SDV.jpg')
    screen = pygame.display.set_mode([fundo_perdeu.get_width(), fundo_perdeu.get_height()])
    rect_proximo = pygame.Rect(475,480,325,100)
    clock = pygame.time.Clock()
    pontuacao = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
    SomarPontos(login,pontuacao[respostas])
    texto  = fonte.render(pontuacao[respostas],True,(0,0,0))
    while perdeste == True:
        for event in pygame.event.get():
    
        
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_proximo.collidepoint(event.pos):
                    tela_comeco(login,senha)
                    perdeste = False
                    return


        pygame.draw.rect(screen,(255,255,255),rect_proximo)
        screen.blit(fundo_perdeu,(0,0))
        screen.blit(texto,(510,348))
        pygame.display.flip()
        clock.tick(60)

            
