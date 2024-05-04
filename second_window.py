import pygame
from main_elements import *
pygame.init()







def second_window():
    welcome_text = font.render('Choose Your Difficulty Level',True,'Black')
    
    welcome_text_rect  = welcome_text.get_rect(center = (600,50))
    difficulty_level__lst = ["Easy","Medium","Hard"]
    difficulty_level_Y=180
    # screen.blit(background,background_rect)
    screen.blit(welcome_text,welcome_text_rect)
    pygame.draw.rect(screen,(0,255,0),pygame.Rect(360,20,480,50),3)

    for index,value in enumerate(difficulty_level__lst):
        
        
        difficulty_level = font.render(str(value),True,'Red')
        
        classes_rect = difficulty_level.get_rect(topleft = (500,difficulty_level_Y))
        screen.blit(difficulty_level,classes_rect)
        pygame.draw.rect(screen,(0,255,0),pygame.Rect(450,(170*(index+1)),200,50),3)
        difficulty_level_Y+=170