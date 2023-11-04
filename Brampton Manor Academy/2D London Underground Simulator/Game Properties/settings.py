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
            game_settings.Display(screen, path)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
            pygame.display.update()
            pygame.time.Clock().tick(60)

    def Display(self,screen, path):
        background = pygame.Rect(400,250,1000,700)
        pygame.draw.rect(screen, (255,255,255), background)

        pygame.draw.line(screen,(0,0,0), (399,250), (399,950))
        pygame.draw.line(screen,(0,0,0), (398,250), (398,950))
        pygame.draw.line(screen,(0,0,0), (397,250), (398,950))

        pygame.draw.line(screen,(0,0,0), (399,250), (1399,250))
        pygame.draw.line(screen,(0,0,0), (399,251), (1399,251))
        pygame.draw.line(screen,(0,0,0), (399,252), (1399,252))

        pygame.draw.line(screen,(0,0,0), (1400,250), (1400,950))
        pygame.draw.line(screen,(0,0,0), (1401,250), (1401,950))
        pygame.draw.line(screen,(0,0,0), (1402,250), (1402,950))

        pygame.draw.line(screen,(0,0,0), (399,951), (1399,951))
        pygame.draw.line(screen,(0,0,0), (399,952), (1399,952))
        pygame.draw.line(screen,(0,0,0), (399,953), (1399,953))

        quit_button_icon = pygame.image.load(f'{path}\\icons\\quit_button.png')
        quit_button = button.Button(screen, 750, 800, quit_button_icon, 1/2)

        back_button_icon = pygame.image.load(f"{path}\\icons\\back_button.png")
        back_button = button.Button(screen, 750, 200, back_button_icon, 1)
        #controls sub section
        
        if quit_button.wasClicked():
            main.Quit()