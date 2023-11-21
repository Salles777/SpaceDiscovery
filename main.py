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
size = (1000,516)
clock = pygame.time.Clock()
icon = pygame.image.load("space.png")
pygame.display.set_icon(icon)
screan = pygame.display.set_mode(size)
background = pygame.image.load("bg.jpg")
pygame.display.set_caption("Space Marker")
running = True
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

    screan.blit(background,(0,0))

    pygame.display.update()
    clock.tick(60)