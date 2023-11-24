import pygame
from tkinter import simpledialog
import ast

star_list = []

def Salvar():
    try:
        file = open("SalvarPontos.txt","w")
        for item in star_list:
            file.write("{0}\n".format(item))
        file.close()
    except:
        print("Erro ao salvar")

pygame.init()
white = (255, 255, 255)
size = (1000,516)
clock = pygame.time.Clock()
icon = pygame.image.load("space.png")
pygame.display.set_icon(icon)
scream = pygame.display.set_mode(size)
background = pygame.image.load("bg.jpg")
pygame.display.set_caption("Space Marker")
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Nome da Estrela: ")
            if item == None or item == "":
                item = "Desconhecido" + str(pos)
            else:
                item = item + str(pos)
            star_list.append((item, pos))

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            Salvar()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            Salvar()
            running = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            try:
                file = open("SalvarPontos.txt","r")
                lines = file.readlines()
                for item in lines:
                    tupla = ast.literal_eval(item)
                    star_list.append(tupla)
            except:
                print("Erro ao carregar os arquivos")

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            file = open("SalvarPontos.txt","w")
            star_list = []
            file.close()
            scream.blit(background,(0,0))

    scream.blit(background,(0,0))
    font = pygame.font.Font("freesansbold.ttf", 15)
    S = font.render("Pressione S para Salvar os Pontos", True , white)
    scream.blit(S, (20,20))
    C = font.render("Pressione C para Carregar os Pontos", True, white)
    scream.blit(C, (20,40))
    D = font.render("Pressione D para Deletar os Pontos", True, white)
    scream.blit(D, (20,60))

    first = True
    point1 = ()
    point2 = ()
    second = True
    distance1 = ()
    distance2 = ()
    for item, pos in star_list:
        star_name = font.render(item, True, white)
        scream.blit(star_name, (pos[0]+10, pos[1]+10))
        pygame.draw.circle(scream, white, pos, 3)
        if first == True:
            point1 = pos
            first = False
        else:
            point2 = pos
            pygame.draw.line(scream, white, point1, point2, 1)
            point1= pos

        if point1 == True:
            distance1 = pos
            point1 = False
        else:
            distance2 = pos
            distance = 0

    pygame.display.update()
    clock.tick(60)
    
pygame.quit