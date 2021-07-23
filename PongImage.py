import pygame  

# 1 initial game
pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Happy Face")
keep_going = True
pic = pygame.image.load("smiley1.png")
color_key = pic.get_at((0,0))  
pic.set_colorkey(color_key) #Set the transparent colorkey
pic_x = 0
pic_y = 0
BLACK = (0,0,0)
WHITE = (255,255,255)
timer = pygame.time.Clock()
speed_x = 5
speed_y = 5

pic_w = pic.get_width()
pic_h = pic.get_height()

points = 0
lives = 5
font = pygame.font.SysFont("Minecraft", 24)


#2 Game loop if keep_going is true
while keep_going:   
    # 3 check event
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            keep_going = False
        
    #4 update pic position  
    # 4.1 update pic x,y with speed         
    pic_x += speed_x
    pic_y += speed_y
    
    # 4.2 check the bouncing 
    if pic_x <= 0 or (pic_x + pic_w) >= 800:
        speed_x = -speed_x
        print("pic_x+pic_w>800: "+str(pic_x + pic_w))
    if pic_y <= 0 or (pic_y + pic_h) >= 600:
        speed_y = -speed_y
        print("pic_y+pic_h>600: "+str(pic_y + pic_h))
     
    # 4.3 draw the picture on the screen    
    screen.fill(BLACK)    
    screen.blit(pic, (pic_x, pic_y))  
    
    # 5 Update Display   
    pygame.display.update()
    timer.tick(60)  # how many frame every sec, https://www.pygame.org/docs/ref/time.html

# Quite/Exit Game    
pygame.quit()  