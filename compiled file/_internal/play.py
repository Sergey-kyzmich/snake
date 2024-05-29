import pygame
import json
import random
import time
from end_screen import *
def play(data):
    screen = data.screen
    with open("content/data.json") as read_json:
        data_json = json.load(read_json)
    
    if data_json["size_field"]==1:return level_1(data, data_json)

import pygame
import json
import random
import time
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
    body_rot = pygame.image.load(f'img/zmeika/tail_rotate/{jdata["color"][0]}_{jdata["color"][1]}_{jdata["color"][2]}.png')
    body_rot =  pygame.transform.scale(body_rot, (80*k, 80*k))
    baricade = pygame.image.load(f'img/zmeika/baricade.png')
    baricade =  pygame.transform.scale(baricade, (80*k, 80*k))
    head = pygame.transform.rotate(head, 180)
    screen = data.screen
    color_bg = {"r":48, "g":101, "b":117}
    run = True
    x = 1920/24
    y = 960/12
    global snakex, snakey
    snakex = x*8
    snakey = y*7+40
    snaker = 2#0-вверх, 1-налева, 2-вниз, 3-вправа
    head = pygame.transform.rotate(head, 90*snaker)
    body = pygame.transform.rotate(body, 90*snaker)
    tail = pygame.transform.rotate(tail, 90*snaker+180)
    k=0
    l = 0
    max_l = jdata["record"]
    eatx = 10*x#random.randint(0, 20)*x
    eaty = 7*y+40#random.randint(0, 13)*y
    body_cor = []#x, y, r, body
    tail_run=False
    tailr = 0
    event_list = []
    rotate_cor = []#[x,y,r]
    clock = pygame.time.Clock()
    pygame.mixer.init()
    pygame.mixer.music.load("content/font_music.mp3")
    pygame.mixer.music.set_volume(int(jdata['music'])/200)
    pygame.mixer.music.play(-1)
    sound_eat = pygame.mixer.Sound("content/Eating_Snake.mp3")
    sound_eat.play
    pygame.mixer.Sound.set_volume(sound_eat,int(jdata["sound"])/100)
    
    tailx = 0
    taily=0
    while run:
        k+=1
        screen.fill((color_bg["r"], color_bg["g"], color_bg["b"]))
        screen.blit(eat, (eatx, eaty))

        
        key = pygame.key.get_pressed()

        if key[pygame.K_ESCAPE]:
            run=False
            pygame.mixer.music.pause()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                event_list.append(int(event.key))
            if event.type == pygame.QUIT:
                pygame.mixer.music.pause()
                pygame.quit()
                run = False

        if event_list!=[] and k==speed:
            event_key = event_list[-1]
            event_list = []

            if event_key == pygame.K_LEFT or event_key == pygame.K_a:
                if snaker in (0, 2):
                    if l<2: tailr = 1;tail = pygame.transform.rotate(tail, (1-snaker)*90)
                    else: rotate_cor.append([snakex, snakey, 1, snaker])
                    head = pygame.transform.rotate(head, (1-snaker)*90)
                    snaker = 1
            elif event_key == pygame.K_RIGHT or event_key == pygame.K_d:
                if snaker in (0, 2):
                    if l<2: tailr = 3;tail = pygame.transform.rotate(tail, (3-snaker)*90)
                    else: rotate_cor.append([snakex, snakey, 3, snaker])
                    head = pygame.transform.rotate(head, (3-snaker)*90)
                    snaker = 3
            elif event_key == pygame.K_UP or event_key == pygame.K_w:
                if snaker in (1, 3):
                    if l<2: tailr = 0;tail = pygame.transform.rotate(tail, (0-snaker)*90)
                    else: rotate_cor.append([snakex, snakey, 0, snaker])
                    head = pygame.transform.rotate(head, (0-snaker)*90)
                    snaker = 0
                    
            elif event_key == pygame.K_DOWN or event_key == 115:
                if snaker in (1, 3):
                    if l<2: tailr = 2;tail = pygame.transform.rotate(tail, (2-snaker)*90)
                    else: rotate_cor.append([snakex, snakey, 2, snaker])
                    head = pygame.transform.rotate(head, (2-snaker)*90)
                    snaker = 2
                    

        if k==speed:
            
            #Передвижение змейки

            lastx = int(snakex)
            lasty = int(snakey)
            
            eat_true=(snaker==0 and snakex==eatx and snakey-y==eaty)or\
                (snaker==1 and snakex-x==eatx and snakey==eaty)or\
                (snaker==2 and snakex==eatx and snakey+y==eaty)or\
                (snaker==3 and snakex+x==eatx and snakey==eaty)
            if tail_run:
                if l<2:
                    if not(eat_true):
                        tailx = lastx
                        taily = lasty
                        screen.blit(tail, (tailx, taily))
            if eat_true:
                sound_eat.play()
                print("eat")
                l+=1
                eatx = random.randint(2, 24)*x-x
                eaty = random.randint(2, 12)*y-y+40
                while [eatx, eaty] in crash_cor(tailx,taily, body_cor, 1,jdata["obstacle"],x,y) or [eatx, eaty]==[snakex, snakey]:
                    eatx = random.randint(1, 24)*x-x
                    eaty = random.randint(2, 12)*y-y+40
                if l == 1:
                    tail_run = True
                    tailx = lastx
                    taily = lasty
                else:
                    body_cor.append([lastx, lasty, snaker, body])
                    body_cor[-1][3] = pygame.transform.rotate(body_cor[-1][3], 90*(snaker%2))

            if l>1:
                if not(eat_true):tailx, taily = body_cor[-1][0], body_cor[-1][1]
                body_cor[-1][0], body_cor[-1][1]= snakex, snakey
                if body_cor[-1][2]%2!=snaker%2:#поворот 1 тела
                    body_cor[-1][3] = pygame.transform.rotate(body_cor[-1][3], 90)
                    body_cor[-1][2] = (body_cor[-1][2]+1)%4
                body_cor = [body_cor[-1]]+body_cor[0:-1]


                if rotate_cor!=[] and rotate_cor[0][0]==tailx and rotate_cor[0][1]==taily: 
                    tail = pygame.transform.rotate(tail, (rotate_cor[0][2]-tailr)*90)
                    tailr = rotate_cor[0][2]
                    rotate_cor = rotate_cor[1:]
                    

        if l>1:
            for i in range(0, len(body_cor)):
                screen.blit(body_cor[i][3], (int(body_cor[i][0]), int(body_cor[i][1])))
            screen.blit(tail, (tailx, taily))
        for i in rotate_cor:
            if i[3]==0 and i[2]==1:screen.blit(pygame.transform.rotate(body_rot, 0),(i[0], i[1]))
            if i[3]==0 and i[2]==3:screen.blit(pygame.transform.rotate(body_rot, 90),(i[0], i[1]))
            if i[3]==1 and i[2]==0:screen.blit(pygame.transform.rotate(body_rot, 180),(i[0], i[1]))
            if i[3]==1 and i[2]==2:screen.blit(pygame.transform.rotate(body_rot, 90),(i[0], i[1]))
            if i[3]==2 and i[2]==1:screen.blit(pygame.transform.rotate(body_rot, -90),(i[0], i[1]))
            if i[3]==2 and i[2]==3:screen.blit(pygame.transform.rotate(body_rot, 180),(i[0], i[1]))
            if i[3]==3 and i[2]==0:screen.blit(pygame.transform.rotate(body_rot, -90),(i[0], i[1]))
            if i[3]==3 and i[2]==2:screen.blit(pygame.transform.rotate(body_rot, 0),(i[0], i[1]))
        if k==speed:
            k=0
            if snaker==0:snakey-=y
            if snaker==1:snakex-=x
            if snaker==2:snakey+=y
            if snaker==3:snakex+=x
        if tail_run:screen.blit(tail, (tailx, taily))
        screen.blit(head, (snakex, snakey))
        create_rect(screen, l, max_l, baricade,x,y,jdata["obstacle"],1)


        pygame.display.update()

        crash = crash_cor(tailx,taily, body_cor, 1,jdata["obstacle"],x,y)
        for crashx, crashy in crash:
            if crashx==snakex and crashy==snakey or snakex<0 or snakex>=1920:
                jdata["record"] = max(max_l, l)
                with open("content/data.json", "w") as write_json:
                    json.dump(jdata, write_json)
                pygame.mixer.music.pause()
                if end_game(data, max_l, l):return data
                else:return play(data)

        clock.tick(30)



def crash_cor(tailx,taily, body_cor, size, lvl,x,y):
    crash = []
    crash.append([tailx, taily])
    for i in body_cor:
        crash.append([i[0], i[1]])
    if size==1:
        for i in range(14):
            crash.append([-80.0, i*80.0])
            crash.append([2000.0, i*80.0])
        for i in range(20):
            crash.append([i*80,40.0])
            crash.append([i*80, 1080.0])
        
        if lvl==1:return crash
        if lvl==2:
            b=[]
            b.append([4*x, 4*y+40]);b.append([5*x, 4*y+40]);b.append([4*x, 5*y+40]);b.append([5*x, 5*y+40])
            b.append([4*x, 9*y+40]);b.append([5*x, 9*y+40]);b.append([4*x, 10*y+40]);b.append([5*x, 10*y+40])
            b.append([20*x, 4*y+40]);b.append([21*x, 4*y+40]);b.append([20*x, 5*y+40]);b.append([21*x, 5*y+40])
            b.append([20*x, 9*y+40]);b.append([21*x, 9*y+40]);b.append([20*x, 10*y+40]);b.append([21*x, 10*y+40])
            return crash+b
        elif lvl==3:
            b = []
            print("Crash")
            b.append([3*x,4*y+40]);b.append([4*x,4*y+40]);b.append([5*x,4*y+40]);b.append([6*x,4*y+40]);b.append([7*x,4*y+40])
            b.append([16*x,4*y+40]);b.append([17*x,4*y+40]);b.append([18*x,4*y+40]);b.append([19*x,4*y+40]);b.append([20*x,4*y+40])
            b.append([3*x,7*y+40]);b.append([4*x,7*y+40]);b.append([5*x,7*y+40]);b.append([6*x,7*y+40]);b.append([7*x,7*y+40])
            b.append([16*x,7*y+40]);b.append([17*x,7*y+40]);b.append([18*x,7*y+40]);b.append([19*x,7*y+40]);b.append([20*x,7*y+40])

            b.append([11*x,4*y+40]);b.append([11*x,5*y+40]);b.append([11*x,6*y+40]);b.append([11*x,7*y+40]);b.append([11*x,8*y+40])
            b.append([12*x,4*y+40]);b.append([12*x,5*y+40]);b.append([12*x,6*y+40]);b.append([12*x,7*y+40]);b.append([12*x,8*y+40])
            return crash+b

    else:
        return crash


def create_rect(screen, l, max_l, baricade,x,y, lvl, size):
    rect = pygame.Rect(0, 0, 1920, 120)
    pygame.draw.rect(screen, pygame.Color(70, 137, 158), rect)
    text_score = pygame.font.Font("content/Deledda Closed Black.ttf", int(100)).render(f"Счет: {l}", True, (0, 0, 0))
    text_max = pygame.font.Font("content/Deledda Closed Black.ttf", int(100)).render(f"Рекорд: {max(max_l, l)}", True, (0, 0, 0))
    screen.blit(text_score, (80, 10))
    screen.blit(text_max, (700, 10))
    print(f"{lvl=} {size=}")


    if lvl==3 and size == 1:
        const_y = 4*y+40;screen.blit(baricade, (3*x, const_y));screen.blit(baricade, (4*x, const_y));screen.blit(baricade, (5*x, const_y));screen.blit(baricade, (6*x, const_y));screen.blit(baricade, (7*x, const_y))
        const_y = 7*y+40;screen.blit(baricade, (3*x, const_y));screen.blit(baricade, (4*x, const_y));screen.blit(baricade, (5*x, const_y));screen.blit(baricade, (6*x, const_y));screen.blit(baricade, (7*x, const_y))
        const_y = 4*y+40;screen.blit(baricade, (16*x, const_y));screen.blit(baricade, (17*x, const_y));screen.blit(baricade, (18*x, const_y));screen.blit(baricade, (19*x, const_y));screen.blit(baricade, (20*x, const_y))
        const_y = 7*y+40;screen.blit(baricade, (16*x, const_y));screen.blit(baricade, (17*x, const_y));screen.blit(baricade, (18*x, const_y));screen.blit(baricade, (19*x, const_y));screen.blit(baricade, (20*x, const_y))

        const_x = 11*x;const_y = 4*y+40;screen.blit(baricade, (const_x, const_y));screen.blit(baricade, (const_x, const_y+y));screen.blit(baricade, (const_x, const_y+2*y));screen.blit(baricade, (const_x, const_y+3*y));screen.blit(baricade, (const_x, const_y+4*y))
        const_x = 12*x;const_y = 4*y+40;screen.blit(baricade, (const_x, const_y));screen.blit(baricade, (const_x, const_y+y));screen.blit(baricade, (const_x, const_y+2*y));screen.blit(baricade, (const_x, const_y+3*y));screen.blit(baricade, (const_x, const_y+4*y))
    
    if lvl==2 and size == 1:
        screen.blit(baricade, (4*x, 4*y+40));screen.blit(baricade, (5*x, 4*y+40));screen.blit(baricade, (4*x, 5*y+40));screen.blit(baricade, (5*x, 5*y+40))
        screen.blit(baricade, (4*x, 9*y+40));screen.blit(baricade, (5*x, 9*y+40));screen.blit(baricade, (4*x, 10*y+40));screen.blit(baricade, (5*x, 10*y+40))
        screen.blit(baricade, (20*x, 4*y+40));screen.blit(baricade, (21*x, 4*y+40));screen.blit(baricade, (20*x, 5*y+40));screen.blit(baricade, (21*x, 5*y+40))
        screen.blit(baricade, (20*x, 9*y+40));screen.blit(baricade, (21*x, 9*y+40));screen.blit(baricade, (20*x, 10*y+40));screen.blit(baricade, (21*x, 10*y+40))