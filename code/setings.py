import pygame
import json
import time
from button_setings import sound_button, music_button, select_menu, view_button, color_button, clear_button
# import main
def setings(data):
    screen = data.screen
    text = create_text()
    count = 0
    myfont = pygame.font.Font("content/Deledda Closed Black.ttf", int(200))
    text_setings = myfont.render("Настройки", True, (255, 130, 13))
    des_font = pygame.font.Font("content/Deledda Closed Black.ttf", 35)
    text_description1 = des_font.render("esc - выйти из настроек",True, (245, 175, 71))
    text_description2 = des_font.render("click в свободное",True, (245, 175, 71))
    text_description3 = des_font.render("пространство - cохранить",True, (245, 175, 71))    
    text_description4 = des_font.render("изменения",True, (245, 175, 71))
    
    run = True
    color_bg = {"r":48, "g":101, "b":117}
    while run:
        screen.fill((color_bg["r"], color_bg["g"], color_bg["b"]))
        screen.blit(text_setings, (400, 20))
        screen.blit(text_description1, (800, 230))
        screen.blit(text_description2, (800, 265))
        screen.blit(text_description3, (800, 300))
        screen.blit(text_description4, (800, 335))
        with open("content/data.json", "r") as read_json:
            data_json = json.load(read_json)
        t = str(data_json["color"][0])+", "+ str(data_json["color"][1])+", "+ str(data_json["color"][2])
        t = pygame.font.Font("content/Deledda Closed Black.ttf", int(80)).render(t, True, (245, 175, 71))
        text["color_btn"].w = t.get_width()+45
        add_text(data.screen, text)
        view_button(data, text)

        pygame.display.update()

        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            return data
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text["sound_btn"].collidepoint(event.pos):
                    sound_button(screen,event)
                if text["music_btn"].collidepoint(event.pos):
                    music_button(screen, event)
                if text["speed_btn"].collidepoint(event.pos):
                    select_menu(data, ["easy", "normal", "hard"], 1200, 630, "speed")
                if text["obstacle_btn"].collidepoint(event.pos):
                    select_menu(data, ["easy", "normal", "hard"], 1200, 740, "obstacle")
                if text["eat_btn"].collidepoint(event.pos):
                    select_menu(data, ["apple", "cherry", "banana"], 1200, 600, "eat")
                if text["color_btn"].collidepoint(event.pos):
                    color_button(data)
                if text["clear_btn"].collidepoint(event.pos):
                    clear_button(data)
            
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
        count+=1
        data.clock.tick(30)
    setings(data)




def create_text():
    myfont = pygame.font.Font("content/Deledda Closed Black.ttf", int(80))
    text={
    "sound": myfont.render("Громкость звука", True, (245, 175, 71)),
    "music": myfont.render("Громкость музыки", True, (245, 175, 71)),
    #"resolution": myfont.render("Разрешение экрана",True, (245, 175, 71)),
    "size": myfont.render("Размер уровня", True, (245, 175, 71)),
    "speed": myfont.render("Скорость змейки", True, (245, 175, 71)),
    "eat": myfont.render("Еда змейки", True, (245, 175, 71)),
    "color": myfont.render("Цвет змейки RGB", True, (245, 175, 71)),
    "obstacle": myfont.render("Кол-во перпятствий", True, (245, 175, 71)),
    "language": myfont.render("Язык", True, (245, 175, 71))
    }
    text["sound_btn"] = pygame.Rect(1200, 520, 160, 80)
    text["music_btn"] = pygame.Rect(1200, 410, 160, 80)
    text["size_field_btn"] = pygame.Rect(1200, 520, 350, 80)
    text["speed_btn"] = pygame.Rect(1200, 630, 350, 80)
    text["obstacle_btn"] = pygame.Rect(1200, 740, 350, 80)
    text["eat_btn"] = pygame.Rect(1200, 850, 350, 80)
    text["clear_btn"] = pygame.Rect(300, 250, 410, 80)
    print(text["color"])
    with open("content/data.json", "r") as read_json:
        data_json = json.load(read_json)
    t = str(data_json["color"][0])+", "+ str(data_json["color"][1])+", "+ str(data_json["color"][2])
    text["t"] = myfont.render(t, True, (245, 175, 71))
    print(f"{(text['t'].get_width()+45)=}")
    text["color_btn"] = pygame.Rect(1200, 960, text["t"].get_width()+45, 80)
    return text



def add_text(screen, text):
    screen.blit(text["sound"], (300,520))
    screen.blit(text["music"], (300, 410))
    screen.blit(text["speed"], (300, 630))
    screen.blit(text["obstacle"], (300, 740))
    screen.blit(text["eat"], (300, 850))
    screen.blit(text["color"], (300, 960))