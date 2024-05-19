import pygame
import time

#criando imagens
logo = pygame.image.load('logoo.png')
logo = pygame.transform.scale(logo, (200, 200))
fundo1 = pygame.image.load('fundo1ofc.png')
fundo1 = pygame.transform.scale(fundo1, (700,500))
fundo2 = pygame.image.load('fundo2ofc.png')
fundo2 = pygame.transform.scale(fundo2, (700,500))
cpessoal = pygame.image.load('cpessoal.png')
cpessoal = pygame.transform.scale(cpessoal, (700,500))
seta = pygame.image.load('seta.png')
seta = pygame.transform.scale(seta, (40,40))
ccontatos = pygame.image.load('ccontatos.png')
ccontatos = pygame.transform.scale(ccontatos, (700,500))
alerta = pygame.image.load('alerta.png')
alerta = pygame.transform.scale(alerta, (700,500))
textinho = pygame.image.load('textinho.png')
textinho = pygame.transform.scale(textinho, (335,200))

#criando timer
pygame.font.init()
sysfont = pygame.font.get_default_font()
font = pygame.font.SysFont('aaa', 72)
ligado = False

#tela
tela = pygame.display.set_mode((700,500))
pygame.display.set_caption("I GOT YOUR BACK")
fundoatual = 'inicial'

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

    if cursorx > 360 and cursorx < 490 and cursory > 350 and cursory <380:
        cursorposicionado2 = True
    else:
        cursorposicionado2 = False
    
    if cursorx > 10 and cursorx < 50 and cursory > 10 and cursory <40:
        cursorposicionado3 = True
    else:
        cursorposicionado3 = False
    
    if cursorx > 520 and cursorx < 650 and cursory > 350 and cursory <380:
        cursorposicionado4 = True
    else:
        cursorposicionado4 = False

    #básico
    tela.fill((200,200,200))

    if fundoatual == 'inicial':
        if ligado == False:
            tela.blit(fundo1,(0,0))
        else:
            tela.blit(fundo2,(0,0))
    if fundoatual == 'cpessoal':
        tela.blit(cpessoal,(0,0))
    if fundoatual == 'ccontatos':
        tela.blit(ccontatos,(0,0))
    if fundoatual == 'alerta':
        tela.blit(alerta,(0,0))


    #eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if fundoatual == 'inicial':
                if cursorposicionado == True:
                    if ligado == False:
                        ligado = True
                        tempoinicial = time.time()
                    else:
                        ligado = False
                if cursorposicionado2 == True:
                    fundoatual = 'cpessoal'
                if cursorposicionado4 == True:
                    fundoatual = 'ccontatos'
            if fundoatual == 'cpessoal':
                if cursorposicionado3 == True:
                    fundoatual = 'inicial'
            if fundoatual == 'ccontatos':
                if cursorposicionado3 == True:
                    fundoatual = 'inicial'
            

    #tempo

    tempofinal = time.time()
    tempo = round(20 - (tempofinal-tempoinicial)) #ajustar tempo !!!!
    if tempo > 0:
        tempo = time.ctime(tempo)
        tempo = tempo.split()
        tempo = tempo[3]
        tempo = tempo[3:8]
    else:
        tempo = '00:00'
        if ligado == True:
            fundoatual = 'alerta'

    #blits
    timer = font.render(tempo, True, (0,0,0))
    zero = font.render('00:00', True, (0,0,0))
    if fundoatual == 'inicial':
        tela.blit(logo, (74,40))
        tela.blit(textinho,(310,80))
        if ligado == True:
            tela.blit(timer,(115,250))
        else:
            tela.blit(zero,(115,250))
    if fundoatual == 'cpessoal' or fundoatual == 'ccontatos':
        tela.blit(seta, (10,10))
    

    #update
    pygame.display.update()

    #FPS
    clock.tick(8)

pygame.font.quit()
pygame.quit()