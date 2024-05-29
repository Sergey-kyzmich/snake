import pygame
from screeninfo import get_monitors
from setings import setings
from play import play
import json

def start_app():#Первый запуск приложения
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN|pygame.SCALED)
    icon = pygame.image.load("img/icon.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption(title="Змейка")
    
    python = pygame.image.load("img/icon.png")# Создание объекта data со всеми картинками
    

    data = cl_data(screen, python)
    main_menu(data)



def main_menu(data):#главное меню
    screen = data.screen
    color_bg = {"r":48, "g":101, "b":117}

    kw = pygame.display.get_surface().get_size()[0]/1920
    kh = pygame.display.get_surface().get_size()[1]/1080

    myfont = pygame.font.Font("content/Deledda Closed Black.ttf", int(200*kw))
    text_main = myfont.render("Змейка", True, (250, 82, 82))
    text_pyt_and_zm = myfont.render("and", True, (250, 82, 82))

    myfont = pygame.font.Font("content/Deledda Closed Black.ttf", int(106*kw))
    text_game = myfont.render("Играть", True, (245, 175, 71))#Текст Сглаживание Цвет Фон
    text_game_rect = text_game.get_rect(topleft=(750*kw,320*kh))

    text_setings = myfont.render("Настройки", True, (245, 175, 71))
    text_setings_rect = text_setings.get_rect(topleft=(750*kw,420*kh))

    text_exit = myfont.render("Выход", True, (245, 175, 71))
    text_exit_rect = text_exit.get_rect(topleft=(750*kw,520*kh))

    zmeika = pygame.image.load("img/zmeika.png"); zmeika = pygame.transform.scale(zmeika, (400*kw, 400*kh))
    python = pygame.image.load("img/python.png");python = pygame.transform.scale(python, (400*kw, 400*kh))


    run = True
    br_play, br_setings, br_me = False, False, False
    while run:
        screen.fill((color_bg["r"], color_bg["g"], color_bg["b"]))

        screen.blit(zmeika, (70*kw, 50*kh))
        screen.blit(python, (70*kw, 600*kh))
        screen.blit(text_pyt_and_zm, (100*kw, 425*kh))

        screen.blit(text_main, (600*kw, 50*kh))
        screen.blit(text_game, (750*kw,320*kh))
        screen.blit(text_setings, (750*kw,420*kh))
        screen.blit(text_exit, (750*kw,520*kh))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
                run = False
            else:
                mouse = pygame.mouse.get_pos()

                if text_game_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                    br_play = True
                    run = False
                if text_setings_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                    br_setings = True
                    run = False
                if text_exit_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                    pygame.quit()
                    run = False
        data.clock.tick(30)
    if br_play: data = play(data)
    elif br_setings: data = setings(data)
    elif br_me: r = me_description(data)
    main_menu(data)



def me_description(data):
    print("I")



class cl_data():
    def __init__(self,screen,python):
        #картинки
        self.screen = screen
        self.python = python
        #другие переменные
        self.monitor_w = pygame.display.get_surface().get_size()[0]
        self.monitor_h = pygame.display.get_surface().get_size()[1]
        self.clock = pygame.time.Clock()



start_app()