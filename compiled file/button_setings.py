import pygame
import json
import time
from PIL import Image

def sound_button(screen, event):
    with open("content/data.json", "r") as read_json:
        data_json = json.load(read_json)
    color = ('lightskyblue4')
    myfont = pygame.font.Font("content/Deledda Closed Black.ttf", int(70))
    print("go")
    rect = pygame.Rect(1200, 520, 160, 80)
    run = True
    clock = pygame.time.Clock()
    while run:
        pygame.display.update()
        text_sound = myfont.render(str(data_json["sound"]), True, (0, 0, 0))
        pygame.draw.rect(screen, pygame.Color(color), rect)
        if data_json["sound"] == "100":screen.blit(text_sound, (rect.x+10, rect.y+10))
        elif len(str(data_json["sound"]))==1: screen.blit(text_sound, (rect.x+50, rect.y+10))
        else: screen.blit(text_sound, (rect.x+25, rect.y+10))

        key = pygame.key.get_pressed()
        if (pygame.mouse.get_pressed()[0] and not rect.collidepoint(pygame.mouse.get_pos())) or key[pygame.K_KP_ENTER]:
            print("back")
            if data_json["sound"]!="":
                with open("content/data.json", "w") as write_json:
                    json.dump(data_json, write_json)
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:data_json["sound"] = str(data_json["sound"])[:-1]
                else:
                    s = event.unicode
                    if s in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:

                        if data_json["sound"]=='' or int(data_json["sound"])<=10 and data_json["sound"]!="0":
                            if int(data_json["sound"]+s)<=100:
                                data_json["sound"]= str(data_json["sound"])+s
        clock.tick(30)


def music_button(screen, event):
    with open("content/data.json", "r") as read_json:
        data_json = json.load(read_json)
    color = ('lightskyblue4')
    myfont = pygame.font.Font("content/Deledda Closed Black.ttf", int(70))
    rect = pygame.Rect(1200, 410, 160, 80)
    run = True
    clock = pygame.time.Clock()
    while run:
        pygame.display.update()
        text_music = myfont.render(str(data_json["music"]), True, (0, 0, 0))
        pygame.draw.rect(screen, pygame.Color(color), rect)
        if data_json["music"] == "100":screen.blit(text_music, (rect.x+10, rect.y+10))
        elif len(str(data_json["music"]))==1: screen.blit(text_music, (rect.x+50, rect.y+10))
        else: screen.blit(text_music, (rect.x+25, rect.y+10))

        if pygame.mouse.get_pressed()[0] and not rect.collidepoint(pygame.mouse.get_pos()):
            print("back")
            if data_json["music"]!="":
                with open("content/data.json", "w") as write_json:
                    json.dump(data_json, write_json)
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:data_json["music"] = str(data_json["music"])[:-1]
                else:
                    s = event.unicode
                    if s in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:

                        if data_json["music"]=='' or int(data_json["music"])<=10 and data_json["music"]!="0":
                            if int(data_json["music"]+s)<=100:
                                data_json["music"]= str(data_json["music"])+s
        clock.tick(30)


def view_button(data, text):
    myfont = pygame.font.Font("content/Deledda Closed Black.ttf", int(80))
    screen = data.screen
    color = (70, 137, 158)
    with open("content/data.json", "r") as read_json:
            data_json = json.load(read_json)

    text_sound = myfont.render(str(data_json["sound"]), True, (0, 0, 0))
    pygame.draw.rect(screen, pygame.Color(70, 137, 158) , text["sound_btn"])
    if data_json["sound"] == "100":sx,sy =1200+10, 520+5
    elif len(str(data_json["sound"]))==1:sx,sy = 1200+50, 520+5
    else:sx,sy = 1200+25, 520+5
    screen.blit(text_sound, (sx, sy))

    text_music = myfont.render(str(data_json["music"]), True, (0, 0, 0))
    pygame.draw.rect(screen, pygame.Color(70, 137, 158) , text["music_btn"])
    if data_json["music"] == "100":mx,my = 1200+10, 410+5
    elif len(str(data_json["music"]))==1: mx,my=1200+50, 410+5
    else: mx,my=1200+25, 410+5
    screen.blit(text_music, (mx, my))
    
    pygame.draw.rect(screen, (70, 137, 158), text["speed_btn"])
    text_speed = myfont.render(["easy", "normal", "hard"][data_json["speed"]-1], True, (0, 0, 0))
    screen.blit(text_speed, ([1270,1250, 1290][data_json["speed"]-1], [625,635,635][data_json["speed"]-1]))#y = -5 +5 +5

    pygame.draw.rect(screen, (70, 137, 158), text["obstacle_btn"])
    text_obstacle = myfont.render(["easy", "normal", "hard"][data_json["obstacle"]-1], True, (0, 0, 0))
    screen.blit(text_obstacle, ([1270,1250, 1290][data_json["obstacle"]-1], [735,745,745][data_json["obstacle"]-1]))
    
    pygame.draw.rect(screen, (70, 137, 158), text["eat_btn"])
    text_obstacle = myfont.render(["apple", "cherry", "banana"][data_json["eat"]-1], True, (0, 0, 0))
    screen.blit(text_obstacle, ([1280,1250, 1250][data_json["eat"]-1], [845,845,845][data_json["eat"]-1]))

    pygame.draw.rect(screen, (70, 137, 158), text["color_btn"])
    s = str(data_json["color"][0])+", "+ str(data_json["color"][1])+", "+ str(data_json["color"][2])
    text_field = myfont.render(s, True, (0, 0, 0))
    screen.blit(text_field, (1200+25, 960+5))

    pygame.draw.rect(screen, (200, 0, 0), text["clear_btn"])
    text_field = myfont.render("Сбросить", True, (0, 0, 0))
    screen.blit(text_field, (300+25, 250-2))
    

    pygame.display.update()


def select_menu(data,name, w,h, button):
    font = pygame.font.Font("content/Deledda Closed Black.ttf", int(80)) 
    name1 = font.render(name[0], True, (0,0,0))#(255, 93, 0)
    name2 = font.render(name[1], True, (0,0,0))
    name3 = font.render(name[2], True, (0,0,0))
    
    with open("content/data.json", "r") as read_json:
        data_json = json.load(read_json)
    screen = data.screen
    color =(70, 137, 158)
    s=0
    rect = pygame.Rect(w, h, 350, 330)
    if button == "eat":
        rect1 = name1.get_rect(topleft=(w+110, h+5))
        rect2 = name2.get_rect(topleft=(w+40, h+5+80))
        rect3 = name3.get_rect(topleft=(w+90, h+5+160))
    else:
        rect1 = name1.get_rect(topleft=(w+110, h+85))
        rect2 = name2.get_rect(topleft=(w+40, h+5+160))
        rect3 = name3.get_rect(topleft=(w+90, h+5+240))
    while True:
        pygame.draw.rect(screen, color, rect)
        if button == "eat":
            screen.blit(name1, (w+80, h+5))
            screen.blit(name2, (w+50, h+5+80))
            screen.blit(name3, (w+50, h+5+160))
        else:
            screen.blit(name1, (w+85, h+5+80))
            screen.blit(name2, (w+50, h+5+160))
            screen.blit(name3, (w+90, h+5+240))#[1270,1250, 1290]

        mouse = pygame.mouse.get_pos()

        if (pygame.mouse.get_pressed()[0] and not rect.collidepoint(pygame.mouse.get_pos())):
            return True
        for event in pygame.event.get():
            if rect1.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                s = 1
            if rect2.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                s = 2
            if rect3.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                s = 3
            if event.type == pygame.QUIT :
                pygame.quit()
        if s!=0:
            break
        pygame.display.update()
    with open("content/data.json", "r") as read_json:
        d = json.load(read_json)
    d[button]=s
    with open("content/data.json", "w") as write_json:
        json.dump(d, write_json)
    return True


def color_button(data):
    with open("content/data.json", "r") as read_json:
        data_json = json.load(read_json)
    color = ('lightskyblue4')
    myfont = pygame.font.Font("content/Deledda Closed Black.ttf", int(70))
    print("go")
    rect = pygame.Rect(1200, 960, 650, 80)
    run = True
    clock = pygame.time.Clock()
    screen = data.screen
    s = str(data_json["color"][0])+", "+ str(data_json["color"][1])+", "+ str(data_json["color"][2])
    q = 0
    while run:
        q+=1
        if q == 3:
            time.sleep(0.5)

        pygame.display.update()
        text_color = myfont.render(str(s), True, (0, 0, 0))
        pygame.draw.rect(screen, pygame.Color(color), rect)
        screen.blit(text_color, (rect.x+10, rect.y+10))

        key = pygame.key.get_pressed()
        if q>3 and (pygame.mouse.get_pressed()[0] and not rect.collidepoint(pygame.mouse.get_pos())) or key[pygame.K_KP_ENTER]:
            print("back")

            #Удаление лишних знаков
            s = s.replace(" ", ",")
            s = s.replace(",,", ",")
            s = s.split(",")
            
            print(f"{s=}")
            def f(q):
                return ((len(q)>1 and q[0]!="0") or len(q)==1)  and int(q)<=255
            if len(s)==3 and sum([f(s[0]), f(s[1]), f(s[2])])==3:
                s = [int(x) for x in s]
                data_json["color"]=s
                with open("content/data.json", "w") as write_json:
                    json.dump(data_json, write_json)
                create_color(s)
            run = False
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:s = s[:-1]
                else:
                    new_el = event.unicode
                    if new_el in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", ","]:
                        s= str(s+new_el).replace(",,", ",").replace("  ", " ")
        rect.w = text_color.get_width()+10

        clock.tick(30)



def create_color(color):
    print(color)
    img = Image.open("img/zmeika/head.png")
    color = (color[0], color[1], color[2])
    def f(img, x, y, color):
        x = x*16
        y = y*16
        for i in range(0, 16):
            for j in range(0, 16):
                img.putpixel((x+i, y+j), color)
        return img

    for i in range(0, 2):f(img, 1,i, color)#изменение цвета головы
    for i in range(0, 4):f(img, 2,i, color)
    for i in range(0, 2):f(img, 3,i, color)

    img.save(f"img/zmeika/head/{color[0]}_{color[1]}_{color[2]}.png")
    img = Image.open("img/zmeika/body.png")
    for i in range(1, 4):#изменение цвета тела
        for j in range(0, 5):
            f(img, i,j, color)

    img.save(f"img/zmeika/body/{color[0]}_{color[1]}_{color[2]}.png")
    img = Image.open("img/zmeika/tail.png")
    for i in range(2, 5):f(img, 1,i, color)#изменение цвета хвоста
    for i in range(1, 5):f(img, 2,i, color)
    for i in range(2, 5):f(img, 3,i, color)

    img.save(f"img/zmeika/tail/{color[0]}_{color[1]}_{color[2]}.png")

    img = Image.open("img/zmeika/tail_rotate.png")
    for i in range(0, 4):#изменение цвета тела
        for j in range(1, 5):
            f(img, i,j, color)
    f(img, 0,4, (0,0,0))
    img.save(f"img/zmeika/tail_rotate/{color[0]}_{color[1]}_{color[2]}.png")

def clear_button(data):
    data = {"sound": "100", 
            "music": "100", 
            "size_field": 1, 
            "speed": 1, 
            "color": [255, 0, 0], 
            "language": "russian", 
            "background": "", 
            "obstacle": 1, 
            "eat": 1,
            "record":0}
    with open("content/data.json", "w") as write_json:
        json.dump(data, write_json)