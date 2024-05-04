import pygame
from main_elements import *
pygame.init()





def third_window():
    welcome_text = font.render('Choose The Number Of Questions',True,'Black')
    welcome_text_rect  = welcome_text.get_rect(center = (600,50))

    questions__lst = ["10 Questions","15 Questions","20 Questions"]
    questions_Y=180
    
    # screen.blit(background,background_rect)
    screen.blit(welcome_text,welcome_text_rect)

    pygame.draw.rect(screen,(0,255,0),pygame.Rect(360,20,480,50),3)

    for index,value in enumerate(questions__lst):
        
        
        questions = font.render(str(value),True,'Red')
        
        questions_rect = questions.get_rect(topleft = (500,questions_Y))
        screen.blit(questions,questions_rect)
        pygame.draw.rect(screen,(0,255,0),pygame.Rect(470,(170*(index+1)),270,50),3)
        questions_Y+=170