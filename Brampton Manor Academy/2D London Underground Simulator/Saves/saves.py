import sys, json, time

from button import *
import pygame, os

class Saves():
    def LoadMenu(screen, SCREEN_WIDTH, SCREEN_HEIGHT, path):
        screen.fill((58,208,241))
        save_rect = pygame.image.load(f"{path}\\Icons\\save_rect.png") # loads the background for each button
        save_1_button = Button(screen, SCREEN_WIDTH/4, SCREEN_HEIGHT/3.2, save_rect, 1)
        save_2_button = Button(screen, SCREEN_WIDTH/4, SCREEN_HEIGHT/2.4, save_rect, 1)
        save_3_button = Button(screen, SCREEN_WIDTH/4, SCREEN_HEIGHT/1.9, save_rect, 1)

        save_surface = pygame.font.Font(f"{path}\\Fonts\\Lora-VariableFont_wght.ttf", 40)
        save_1_surface = save_surface.render("Save 1", True, "black")
        save_2_surface = save_surface.render("Save 2", True, "black")
        save_3_surface = save_surface.render("Save 3", True, "black")

        screen.blit(save_1_surface, (SCREEN_WIDTH/4 + 10, SCREEN_HEIGHT/3))
        screen.blit(save_2_surface, (SCREEN_WIDTH/4 + 10, SCREEN_HEIGHT/3 + 120))
        screen.blit(save_3_surface, (SCREEN_WIDTH/4 + 10, SCREEN_HEIGHT/3 + 260))

        back_button_image = pygame.image.load(f"{path}\\Icons\\back_button.png")
        back_button = Button(screen, x=SCREEN_WIDTH-190, y=SCREEN_HEIGHT/10+70, image=back_button_image, scale=0.3)
        return back_button, save_1_button, save_2_button, save_3_button

    def ChangeSaveName(screen, path, save, save_data):
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
        
        save_data["name"] = name
        with open(save, "w") as f:
            f.write(json.dumps(save_data))

    def GetSaveInfo(save, path):
        time.sleep(1)
        with open(f"{path}\\Saves\\{save}", 'r') as save_file:
            save_data = json.load(save_file)
        return save_data
    
    def Save():
        pass