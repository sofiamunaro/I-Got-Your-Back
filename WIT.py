import pygame
import time

#criando imagens
logo = pygame.image.load('IMG_8900.jpg')
logo = pygame.transform.scale(logo, (300, 150))
fundo1 = pygame.image.load('fundo1ofc.png')
fundo1 = pygame.transform.scale(fundo1, (700,500))
fundo2 = pygame.image.load('fundo2ofc.png')
fundo2 = pygame.transform.scale(fundo2, (700,500))

#criando timer
pygame.font.init()
sysfont = pygame.font.get_default_font()
font = pygame.font.SysFont('aaa', 72)
ligado = False

#tela
tela = pygame.display.set_mode((700,500))
pygame.display.set_caption("I GOT YOUR BACK")

# criando o relógio
clock = pygame.time.Clock()

# inicializando
run = True
pygame.init()
pygame.display.init()

tempoinicial = time.time()

# loop

while run:

    #mouse
    cursor = pygame.mouse.get_pos()
    cursorx = cursor[0]
    cursory = cursor[1]
    if cursorx > 100 and cursorx < 230 and cursory > 350 and cursory <380:
        cursorposicionado = True
    else:
        cursorposicionado = False
    

    #básico
    tela.fill((200,200,200))

    if ligado == False:
        tela.blit(fundo1,(0,0))
    else:
        tela.blit(fundo2,(0,0))

    #imagens
    tela.blit(logo, (100,60))

    #eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if cursorposicionado == True:
                if ligado == False:
                    ligado = True
                    tempoinicial = time.time()
                else:
                    ligado = False
                    
            

    #tempo

    tempofinal = time.time()
    tempo = round(120 - (tempofinal-tempoinicial)) #ajustar tempo !!!!
    if tempo > 0:
        tempo = time.ctime(tempo)
        tempo = tempo.split()
        tempo = tempo[3]
        tempo = tempo[3:8]
    else:
        tempo = '00:00'

    #timer
    timer = font.render(tempo, True, (0,0,0))
    zero = font.render('00:00', True, (0,0,0))
    if ligado == True:
        tela.blit(timer,(115,250))
    else:
        tela.blit(zero,(115,250))


    #update
    pygame.display.update()

    #FPS
    clock.tick(8)

pygame.font.quit()
pygame.quit()