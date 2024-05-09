import pyqrcode
from pyqrcode import QRCode
import png
import pygame
import cv2 
import numpy as np
from pyzbar.pyzbar import decode
from tkinter.filedialog import *
# =============================================================================

# =============================================================================
pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Qr Code Scanner')

for x in range(50,650):
    print('')


              
         

def generate():
    word = ""
    generaterun = True

    while generaterun:
        text_font = pygame.font.Font('freesansbold.ttf',40)
        text_font1 = pygame.font.Font('freesansbold.ttf',20)
        enter = 0
        
        screen.fill((0,0,0))
        pygame.draw.rect(screen,(255,255,0), pygame.Rect(1,100,1000,40),3)
        inp = text_font1.render(word,True,(255,255,255))
        screen.blit(inp,(460,110))
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
              generaterun = False
          if event.type == pygame.KEYDOWN:
                  
                  if event.key == pygame.K_BACKSPACE:
                       word = word[:-1]
                  elif event.key == pygame.K_RETURN:
                      enter = 1   
                  elif event.key == pygame.K_ESCAPE:
                      MainGame()      
                  else:     
                       word+=event.unicode     
        if enter == 1:
             url = pyqrcode.create(word)
             photo = f"{word}.png"
             photosvg = f"{word}.svg"
             url.svg(photosvg,scale = 8)
             url.png(photo,scale = 6)
             url.show()
                      
        pygame.display.update()         
                  

def MainGame():
   text_font = pygame.font.Font('freesansbold.ttf',40)
   mainrunning = True

   while mainrunning:
      screen.fill((0,0,0))
      screen.blit(text_font.render("QR Code Scanner",True,(255,255,255)),(300,50))
      pygame.draw.rect(screen,(255,255,0), pygame.Rect(30,150,500,60),3)
      pygame.draw.rect(screen,(255,255,0), pygame.Rect(30,250,500,60),3)
      pygame.draw.rect(screen,(255,255,0), pygame.Rect(30,350,500,60),3)
      challenge1 = text_font.render("Generate QR Code",True,(255,255,255))
      challenge2 = text_font.render("Read QR By Camera",True,(255,255,255))
      challenge3 = text_font.render("Read QR by Image",True,(255,255,255))
      challenge4 = text_font.render("(Press 1)",True,(120, 108, 102))
      challenge5 = text_font.render("(Press 2)",True,(120, 108, 102))
      challenge6 = text_font.render("(Press 3)",True,(120, 108, 102))      
      screen.blit(challenge1,(100,160))
      screen.blit(challenge2,(100,260))
      screen.blit(challenge3,(100,360))
      screen.blit(challenge4,(550,160))
      screen.blit(challenge5,(550,260))
      screen.blit(challenge6,(550,360))
      starter = 0
      
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              mainrunning = False
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_1:
                  generate()  
              if event.key == pygame.K_2:
                  Video()     
              if event.key == pygame.K_3:
                  photo_read()    
     
             
          
      pygame.display.update()  
      
def photo_read():
    photorun = True
    code = ''
    text_font2 = pygame.font.Font('freesansbold.ttf',20)
    while photorun:
        screen.fill((0,0,0))
        datainp = text_font2.render(code,True,(255,255,255))
        screen.blit(datainp,(60,110))
        pygame.draw.rect(screen,(255,255,0), pygame.Rect(50,100,900,40),3)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    photo = askopenfilename()
                    img = cv2.imread(photo)
                    for code_dta in decode(img):
                       code = code_dta.data.decode('utf-8')
                       print(code)
                elif event.key == pygame.K_ESCAPE:
                      MainGame()         
                    
        pygame.display.update()            
          
def Video():
    cap = cv2.VideoCapture(0) 
    cap.set(3,640)
    cap.set(4,480) 
    Videorun = True 
    run = False
    text_font2 = pygame.font.Font('freesansbold.ttf',20)
    
    while not run:     
           success,img = cap.read()
           for data in decode(img):
               code = data.data.decode('utf-8')
               print(code)
               pts = np.array([data.polygon],np.int32)
               pts = pts.reshape((-1,1,2))
               cv2.polylines(img,[pts],True,(0,0,0),2)
               pts2 = data.rect
               cv2.putText(img,data.data.decode('utf-8'),(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,0,0),2)      
           cv2.imshow('Result',img) 
           cv2.waitKey(1)
          
    while Videorun:
        
        
        screen.fill((0,0,0))
        
        datainp = text_font2.render(code,True,(255,255,255))
        screen.blit(datainp,(60,110))
        pygame.draw.rect(screen,(255,255,0), pygame.Rect(50,100,900,40),3)
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
              Videorun = False
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_RETURN:
                  run = True  
              elif event.key == pygame.K_ESCAPE:
                      MainGame()         
            
                
              
        pygame.display.update()            
MainGame()      