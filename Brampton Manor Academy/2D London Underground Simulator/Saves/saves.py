import sys
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\RunTime")

import button, pygame, os

class Saves():
    def LoadMenu(screen, SCREEN_WIDTH, SCREEN_HEIGHT, path):
        screen.fill((58,208,241))
        save_rect = pygame.image.load(f"{path}\\Icons\\save_rect.png") # loads the background for each button
        save_1_button = button.Button(screen, SCREEN_WIDTH/4, SCREEN_HEIGHT/3.2, save_rect, 1)
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

        dialogue_box = pygame.Rect(400,500,800,200)
        font = pygame.font.Font(f"{path}\\Fonts\\Lora-VariableFont_wght.ttf", 30)
        layer = font.render(name,False,(0,0,0))
        screen.blit(layer, (dialogue_box.x+3,dialogue_box.y + 3))

        done = False
        while not done:
            for event in pygame.event.get():
                if not done:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            done = True
                        elif event.key == pygame.K_BACKSPACE:
                            name = name[:-1]
                            layer = font.render(name,True,(0,0,0))
                        else:
                            name += event.unicode
                            layer = font.render(name,True,(0,0,0))
            screen.fill((58,208,241))
            pygame.draw.rect(screen, (255,255,255), dialogue_box)
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(400,500,800,200), 3)
            font = pygame.font.Font(f"{path}\\Fonts\\Lora-VariableFont_wght.ttf", 30)
            screen.blit(layer, (dialogue_box.x+3,dialogue_box.y + 5))
            screen.blit(layer, (dialogue_box.x+3,dialogue_box.y + 5))
            pygame.display.update()
            
        file = path + "\\Saves\\"+ save_name
        os.rename(file, path+"\\Saves\\"+name+".txt")
        return name
    
    def GetSaveName(path, number):
        location = os.fsencode(path + "\\Saves")
        for file in os.listdir(location):
            name = os.fsdecode(file)
            if name.endswith(".txt"):
                file = open(f"{path}\\Saves\\{name}", "r")
                file_no = file.readline()[7]
                if file_no == number:
                    return name[:-4]


    def GetSaveInfo(screen, path, save_name):
        import time
        time.sleep(1)
        temporary_file = open(f"{path}\\Saves\\{save_name}.txt", "r")
        temp_lines = temporary_file.readlines()
        no_lines = len(temp_lines)
        game_file = open(f"{path}\\Saves\\{save_name}.txt", "r")

        lines = []
        
        for line_no in range(no_lines):
            line = game_file.readline()[:-1]
            lines.append(line)

        file = lines[0][7:]
        map = lines[1][6:]
        gameLevels = lines[2][13:] #split string into parts and add into a dictionary
        level = int(lines[3][8:])
        game_time = [lines[4][7:9], lines[4][10:12], lines[4][13:]] #day, month, year. stored as strings.
        difficulty = lines[5][13:]
        customerSatisfaction = int(lines[6][23:])
        customers_at_stations = lines[7][24:] #do similarly like for game_time
        money = float(lines[8][8:])
        debt = float(lines[9][6:])
        trainsPerHour = lines[10][16:] # do similarly like for game_time, customers_at_stations
        save_data = [file, map, gameLevels, level, game_time, difficulty, customerSatisfaction, customers_at_stations, money, debt, trainsPerHour]
        print(save_data)
        return save_data