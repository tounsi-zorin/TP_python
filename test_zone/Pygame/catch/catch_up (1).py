from pygame import *

#create game window
init()
pywin = display.set_mode((700 , 500))
display.set_caption("Catch")


#set scene background
background  = transform.scale(image.load('background.png') , (700 , 500))

#creat 2 sprites and place them on the scene
sprite1 = transform.scale(image.load('sprite1.png'), (100 , 80))
sprite2 = transform.scale(image.load('sprite2.png'), (100 , 80))
#handle "click on the "Close the window"" event 
game = True
while game : 
    pywin.blit(background, (0 , 0))
    pywin.blit(sprite1 , (250 , 300))
    pywin.blit(sprite2 , (50 , 300))
    for e in event.get():
        if e.type == QUIT :
            game = False
    display.update()