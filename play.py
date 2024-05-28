import pygame
import json
import random
import time
def play(data):
    screen = data.screen
    with open("content/data.json") as read_json:
        data_json = json.load(read_json)
    
    if data_json["size_field"]==1:return level_1(data, data_json)




def level_1(data, jdata):
    size = [20, 13]
    k = 1
    speed = [10, 6, 3][jdata['speed']-1]
    eat = pygame.image.load(f"img/eat/{['apple', 'cherry', 'banana'][jdata['eat']-1]}.png")
    eat =  pygame.transform.scale(eat, (80*k, 80*k))
    head = pygame.image.load(f'img/zmeika/head/{jdata["color"][0]}_{jdata["color"][1]}_{jdata["color"][2]}.png')
    head=  pygame.transform.scale(head, (80*k, 80*k))
    body = pygame.image.load(f'img/zmeika/body/{jdata["color"][0]}_{jdata["color"][1]}_{jdata["color"][2]}.png')
    body =  pygame.transform.scale(body, (80*k, 80*k))
    tail = pygame.image.load(f'img/zmeika/tail/{jdata["color"][0]}_{jdata["color"][1]}_{jdata["color"][2]}.png')
    tail =  pygame.transform.scale(tail, (80*k, 80*k))
    head = pygame.transform.rotate(head, 180)
    screen = data.screen
    color_bg = {"r":48, "g":101, "b":117}
    run = True
    x = 1600/20
    y = 1040/13
    snakex = x
    snakey = y*7
    snaker = 2#0-вверх, 1-налева, 2-вниз, 3-вправа
    head = pygame.transform.rotate(head, 90*snaker)
    body = pygame.transform.rotate(body, 90*snaker)
    tail = pygame.transform.rotate(tail, 90*snaker)
    k=0
    l = 1
    eatx = random.randint(0, 20)*x
    eaty = random.randint(0, 13)*y
    body_cor = [[]]#[x,y,r]
    tail_run=False
    rotate_cor = [[]]#x,y,r
    while run:
        k+=1
        screen.fill((color_bg["r"], color_bg["g"], color_bg["b"]))
        screen.blit(head, (snakex, snakey))
        if tail_run:screen.blit(tail, (tailx, taily))
        screen.blit(eat, (eatx, eaty))
        pygame.display.update()

        
        key = pygame.key.get_pressed()

        if key[pygame.K_ESCAPE]:
            run=False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                   if snaker in (0, 2):
                       head = pygame.transform.rotate(head, (1-snaker)*90)
                       snaker = 1
                       rotate_cor.append([snakex, snakey, 1])
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                   if snaker in (0, 2):
                       head = pygame.transform.rotate(head, (3-snaker)*90)
                       snaker = 3
                       rotate_cor.append([snakex, snakey, 3])
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                   if snaker in (1, 3):
                       head = pygame.transform.rotate(head, (0-snaker)*90)
                       snaker = 0
                       rotate_cor.append([snakex, snakey, 0])
                elif event.key == pygame.K_DOWN or event.key == 115:
                   if snaker in (1, 3):
                       head = pygame.transform.rotate(head, (2-snaker)*90)
                       snaker = 2
                       rotate_cor.append([snakex, snakey, 2])
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
        if k==speed:
            k=0
            #Передвижение змейки
            lastx = snakex
            lasty = snakey

            if snaker==0:snakey-=y
            if snaker==1:snakex-=x
            if snaker==2:snakey+=y
            if snaker==3:snakex+=x
            print(f"go to {snakex} {snakey}")
            if tail_run:
                tailx = lastx
                taily = lasty
            
            if snakex==eatx and snakey==eaty:
                print("eat")
                eatx = random.randint(0, 20)
                eaty = random.randint(0, 13)
                if l == 1:
                    tail_run = True
                    tailx = lastx
                    taily = lasty
                    tail = pygame.transform.rotate(tail, 90*(snaker+1))
        data.clock.tick(30)