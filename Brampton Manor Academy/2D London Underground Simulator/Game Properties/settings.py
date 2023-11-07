import sys

sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Game Properties")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Fonts")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Maps")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\RunTime")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Saves")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Trains")


import pygame, button, main

class Settings():
    def __init__(self, volume, difficulty):
        self.volume = volume
        self.difficulty = difficulty

    def InGameSettings(self, screen, game_settings, path):
        inSettings = True
        while inSettings is True:
            quit_button, back_button = game_settings.Display(screen, path)
            if back_button.wasClicked():
                inSettings = False
            if quit_button.wasClicked():
                #ask user if they want to save
                #save if they want to
                main.Quit()
                pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
            pygame.display.update()

    def Display(self,screen, path):
        background = pygame.Rect(400,250,1000,700)
        pygame.draw.rect(screen, (255,255,255), background)

        border = pygame.Rect(300,250,1000,700)
        pygame.draw.rect(screen,(0,0,0),border,2)

        quit_button_icon = pygame.image.load(f'{path}\\icons\\quit_button.png')
        quit_button = button.Button(screen, 750, 800, quit_button_icon, 1/2)

        back_button_icon = pygame.image.load(f"{path}\\icons\\back_button.png")
        back_button = button.Button(screen, 750, 200, back_button_icon, 1)
        #controls sub section
        return quit_button, back_button
