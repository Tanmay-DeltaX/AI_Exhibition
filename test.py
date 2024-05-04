import pygame
from sys import exit
from first_window import first_window
from second_window import second_window
from third_window import third_window
from main_elements import *

active_one = True
active_two=True
active_three=True



pygame.init()


clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200,750))



pygame.display.set_caption("Human VS Bot Challenge")




while True:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        
                
    if active_one == True:
         first_window()
         for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_1:
                    print('y')
                    active_one=False

           
                elif event.key == pygame.K_2:
                    print('y')
                    active_one=False

            
                elif event.key == pygame.K_3:
                    print('y')
                    active_one=False                
                
                elif event.key == pygame.K_4:
                    print('y')
                    active_one=False 


    elif active_two==True:
        second_window()    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_1:
                    print('y')
                    active_two=False

            
                if event.key == pygame.K_2:
                    print('y')
                    active_two=False
            
                if event.key == pygame.K_3:
                    print('y')
                    active_two=False   

                              
                 
    
    elif active_three==True :
        third_window()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_1:
                    print('y')
                    active_three=False

                
                elif event.key == pygame.K_2:
                    print('y')
                    active_three=False

                
                elif event.key == pygame.K_3:
                    print('y')
                    active_three=False
    

    pygame.display.update()        

    clock.tick(60)
