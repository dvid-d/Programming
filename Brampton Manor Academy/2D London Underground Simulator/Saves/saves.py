import sys
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\RunTime")

import button, pygame, os

class Saves():
    def LoadMenu(screen, SCREEN_WIDTH, SCREEN_HEIGHT, path):
        screen.fill((58,208,241))
        save_rect = pygame.image.load(f"{path}\\Icons\\save_rect.png") # loads the background for each button
        save_1_button = button.Button(screen, SCREEN_WIDTH/4, SCREEN_HEIGHT/3.2, save_rect, 1) # creates the first, second and third buttons respectivelly
        save_2_button = button.Button(screen, SCREEN_WIDTH/4, SCREEN_HEIGHT/2.4, save_rect, 1)
        save_3_button = button.Button(screen, SCREEN_WIDTH/4, SCREEN_HEIGHT/1.9, save_rect, 1)

        save_surface = pygame.font.Font(f"{path}\\Fonts\\Lora-VariableFont_wght.ttf", 40)
        save_1_surface = save_surface.render("Save 1", True, "black")
        save_2_surface = save_surface.render("Save 2", True, "black")
        save_3_surface = save_surface.render("Save 3", True, "black")

        screen.blit(save_1_surface, (SCREEN_WIDTH/4 + 10, SCREEN_HEIGHT/3))
        screen.blit(save_2_surface, (SCREEN_WIDTH/4 + 10, SCREEN_HEIGHT/3 + 120))
        screen.blit(save_3_surface, (SCREEN_WIDTH/4 + 10, SCREEN_HEIGHT/3 + 260))

        back_button_image = pygame.image.load(f"{path}\\Icons\\back_button.png")
        back_button = button.Button(screen, x=SCREEN_WIDTH-190, y=SCREEN_HEIGHT/10+70, image=back_button_image, scale=0.3)
        return back_button, save_1_button, save_2_button, save_3_button

    def ChangeFileName(screen, path, save_name):
        name = ""
        done = False
        dialogue_box = pygame.Rect(400,500,800,200)
        pygame.draw.rect(screen, (0,0,0), dialogue_box, 5)
        font = pygame.font.Font(f"{path}\\Fonts\\Lora-VariableFont_wght.ttf", 30)
        layer = font.render(name,False,(0,0,0))
        screen.blit(layer, (dialogue_box.x+3,dialogue_box.y + 3))
        while not done:
            for event in pygame.event.get():
                if not done:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            name = name[:-1]
                            layer = font.render(name,True,(0,0,0))
                            screen.blit(layer, (dialogue_box.x+3,dialogue_box.y + 5))
                        elif event.key == pygame.K_RETURN:
                            done = True
                        else:
                            name += event.unicode
                            layer = font.render(name,True,(0,0,0))
                            screen.blit(layer, (dialogue_box.x+3,dialogue_box.y + 5))
                pygame.display.update()
        file = path + "\\Saves\\"+ save_name
        os.rename(file, path+"\\Saves\\"+name+".txt")
        print("slay2")
        return name

    def GetSaveInfo(screen, path, save_name):
        print("slay1")
        print("slay3")
        import time
        time.sleep(1)
        temporary_file = open(f"{path}\\Saves\\{save_name}", "r")
        temp_lines = temporary_file.readlines()
        no_lines = len(temp_lines)
        game_file = open(f"{path}\\Saves\\{save_name}", "r")

        lines = []
        
        for line_no in range(no_lines):
            line = game_file.readline()[:-2]
            lines.append(line)

        map = lines[0][6:]
        gameLevels = lines[1][13:]
        level = lines[2][8:]
        time = lines[3][7:]
        difficulty = lines[4][13:]
        customerSatisfaction = lines[5][24:]
        customers_at_stations = lines[6][25:]
        money = lines[7][8:]
        debt = lines[8][7:]
        save_data = [map, gameLevels, level, time, difficulty, customerSatisfaction, customers_at_stations, money, debt]

        return save_data