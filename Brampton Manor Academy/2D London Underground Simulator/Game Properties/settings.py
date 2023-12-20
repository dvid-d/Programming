import sys

sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Game Properties")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Fonts")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Maps")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\RunTime")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Saves")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Trains")


import pygame, button, main, shop

class Settings():
    def __init__(self, volume, difficulty):
        self.volume = volume
        self.difficulty = difficulty

    def InGameSettings(self, screen, game_settings, path):
        inSettings = True
        while inSettings is True:
            quit_button, back_button = game_settings.Display(screen, path) #add shop_button
            if back_button.wasClicked():
                inSettings = False
            elif quit_button.wasClicked():
                #ask user if they want to save
                #save if they want to
                main.Quit()
                pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        inSettings = False
                    
            pygame.display.update()

    def Display(self,screen, path):
        background = pygame.Rect(400,250,1000,700)
        pygame.draw.rect(screen, (255,255,255), background)

        border = pygame.Rect(300,250,1000,700)
        pygame.draw.rect(screen,(0,0,0),border,2)

        quit_button_icon = pygame.image.load(f'{path}\\icons\\quit_button.png')
        quit_button = button.Button(screen, 700, 840, quit_button_icon, 0.35)

        back_button_icon = pygame.image.load(f"{path}\\icons\\back_button.png")
        back_button = button.Button(screen, 1190, 260, back_button_icon, 0.2)



        #controls sub section
        return quit_button, back_button
