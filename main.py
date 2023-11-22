import pygame
from tkinter import simpledialog
import json

star_list = {}

def inicializated():
    try:
        arquivo = open("star_list.txt","r")
        global star_list
        star_list = json.loads(arquivo.read())
        arquivo.close()
    except:
        arquivo = open("star_list.txt","w")
        arquivo.close()

inicializated()

pygame.init()
black = (0, 0, 0)
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
first = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Nome da Estrela: ")
            print(item)
            if item == None or item == "":
                item = "Desconhecido" + str(pos)
            star_list[item] = pos
            arquivo = open("star_list.txt","w")
            arquivo.write(json.dumps(star_list))
            arquivo.close()
        #elif event.type == pygame.
     
    scream.blit(background,(0,0))
    font = pygame.font.Font("freesansbold.ttf", 15)
    text2 = font.render("Pressione F12 para Deletar os pontos", True, white)
    scream.blit(text2, (20,30))
    text3 = font.render("Após colocar o ponto o salvamento é automático", True, white)
    scream.blit(text3, (20,50))
    arquivo = open("star_list.txt", "r")
    try:
        star_list = json.loads(arquivo.read())
    except:
        star_list = {}
    for nome, pos in star_list.items():
        pygame.draw.circle(scream, white, pos, 7)
        star_name = font.render(nome, True, white)
        scream.blit(star_name,(pos[0]+10,pos[1]+10))
        if first == True:
            back = pos
            first = False
        else:
            pygame.draw.line(scream, white, back, pos, 2)
            back = pos

    pygame.display.update()
    clock.tick(60)