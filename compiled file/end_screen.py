import pygame
def end_game(data, max_l, l):
    titlefont = pygame.font.Font("content/Deledda Closed Black.ttf", 200)
    myfont = pygame.font.Font("content/Deledda Closed Black.ttf", 130)
    btnfont = pygame.font.Font("content/Deledda Closed Black.ttf", 80)
    screen = data.screen
    color_bg = {"r":48, "g":101, "b":117} 
    run = True
    text_title = titlefont.render("Игра Окончена", True, (255, 130, 13))
    text_new_record = titlefont.render("Новый Рекорд!", True, (255,0, 10))
    text_score = myfont.render(f"Ваш счет: {l}", True, (245, 175, 71))
    text_record = myfont.render(f"Рекорд:    {max(max_l, l)}", True, (245, 175, 71))
    game_btn = pygame.Rect(300, 900, 290, 100)
    menu_btn = pygame.Rect(800,900, 570, 100)
    text_game_btn = btnfont.render("Играть", True, (0,0,0))
    text_menu_btn =  btnfont.render("Главное меню", True, (0,0,0))
    color = (70, 137, 158)
    while run:
        screen.fill((color_bg["r"], color_bg["g"], color_bg["b"]))
        screen.blit(text_title, (200, 20))
        if max_l<l:screen.blit(text_new_record, (215, 300))
        screen.blit(text_score, (300, 500))
        screen.blit(text_record, (300, 650))
        pygame.draw.rect(screen, color, game_btn)
        pygame.draw.rect(screen, color, menu_btn)
        screen.blit(text_game_btn, (310, 910))
        screen.blit(text_menu_btn, (810, 910))
        pygame.display.update()



        key = pygame.key.get_pressed()

        if key[pygame.K_ESCAPE]:
            run=False
            return False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_btn.collidepoint(event.pos):
                    return False
                if menu_btn.collidepoint(event.pos):
                    return True

            if event.type == pygame.QUIT:
                pygame.mixer.music.pause()
                pygame.quit()
                run = False