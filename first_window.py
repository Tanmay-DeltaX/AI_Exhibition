import pygame
from main_elements import *
pygame.init()







def first_window():
    welcome_text = font.render('Human Vs Bot Challenge',True,'Black')
    
    welcome_text_rect  = welcome_text.get_rect(center = (600,50))
    class_lst = ['CLASS 09',"CLASS 10","CLASS 11",'CLASS 12']
    class_Y=150
    screen.blit(background,background_rect)
    screen.blit(welcome_text,welcome_text_rect)
    pygame.draw.rect(screen,(0,255,0),pygame.Rect(360,20,480,50),3)  # draws a rectangle around the text'Human vs bot challenge'

    for index,value in enumerate(class_lst):
        
        
        classes = font.render(str(value),True,'Red')
        
        classes_rect = classes.get_rect(center = (125,class_Y))
        screen.blit(classes,classes_rect)
        pygame.draw.rect(screen,(0,255,0),pygame.Rect(30,(125*(index+1)),270,50),3)
        class_Y+=125 


   
                        
