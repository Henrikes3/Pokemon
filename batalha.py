import pygame

pygame.init()

pygame.display.set_caption('Barra ded progresso')
barraxp = (0, 0, 255)
barravida = (0, 255, 0)
barravazia  = (0, 0, 0)
largura = 800
altura = 600
relogio = pygame.time.Clock()
tela = pygame.display.set_mode((largura, altura))
fonte = pygame.font.SysFont('Arial', 20, True, False)
rodando = True
henrikes = {
     "nome" : 'h3nrik3s',
     'vida': 100,
     'vida_max' : 100,
     'xp' : 20,
     'xp_max' : 100
     

}

while rodando:
    relogio.tick(120)
    tela.fill((255, 255, 255))
    largura_vida = int((henrikes['vida']/henrikes['vida_max'])* 250)
    pygame.draw.rect(tela, barravazia,(500, 490, 250 , 5))
    pygame.draw.rect(tela, barravida,(500, 490, largura_vida , 5))
    largura_xp = int((henrikes['xp']/henrikes['xp_max'])* 250)
    pygame.draw.rect(tela, barravazia,(500, 540, 250 , 5))
    pygame.draw.rect(tela, barraxp,(500, 540, largura_xp , 5))
    
    nome_texto = fonte.render(f'Nome:  {henrikes['nome']}', False, (0, 0, 0))
    vida_texto = fonte.render(f'Vida: {henrikes['vida']} / {henrikes['vida_max']}', False, (0, 0, 0))
    xp_texto = fonte.render(f'XP: {henrikes['xp']} / {henrikes['xp_max']}', False, (0, 0, 0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    tela.blit(nome_texto, (550, 450))
    tela.blit(vida_texto, (550, 500))
    tela.blit(xp_texto, (550, 550))
    pygame.display.update()
pygame.quit()
