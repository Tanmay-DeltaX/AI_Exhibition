import pygame
pygame.init()


font= pygame.font.Font('font.ttf',50)

screen = pygame.display.set_mode((1200,750))

background_size= (1200,750)
background = pygame.transform.scale(pygame.image.load('background.jpg'),background_size).convert_alpha()
background_rect = background.get_rect(center = (600,375))