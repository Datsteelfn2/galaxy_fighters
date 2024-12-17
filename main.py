import pygame
import os
WIDTH,HEIGHT=900,500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Second Game")
BLACK=(0,0,0)
WHITE=(255,255,255)


BORDER=pygame.Rect(WIDTH/2-5,0,10,HEIGHT)
FPS=60
VELOCITY=5
SPCAESHIP_WIDTH,SPACESHIP_HEIGHT=55,40

YELLOW_SPACESHIP_IMAGE=pygame.image.load(os.path.join("images","spaceship_yellow.png"))
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPCAESHIP_WIDTH,SPACESHIP_HEIGHT)),90)

RED_SPACESHIP_IMAGE=pygame.image.load('images/spaceship_red.png')
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPCAESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
def draw_window(red,yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN,BLACK,BORDER)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    pygame.display.update()

def yellow_handle_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x-VELOCITY>0:
        yellow.x-=VELOCITY
    if keys_pressed[pygame.K_d] and yellow.x+VELOCITY+yellow.width<BORDER.x:
        yellow.x+=VELOCITY
    if keys_pressed[pygame.K_w] and yellow.y-VELOCITY>0:
        yellow.y-=VELOCITY
    if keys_pressed[pygame.K_s] and yellow.y+yellow.height<HEIGHT-15:
        yellow.y+=VELOCITY
            
def red_handle_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x-VELOCITY>BORDER.x+BORDER.width:
        red.x-=VELOCITY
    if keys_pressed[pygame.K_RIGHT] and red.x+VELOCITY+red.width<WIDTH:
        red.x+=VELOCITY
    if keys_pressed[pygame.K_UP] and red.y-VELOCITY>0:
        red.y-=VELOCITY
    if keys_pressed[pygame.K_DOWN] and red.y+red.height<HEIGHT-15:
        red.y+=VELOCITY
def main():
    red=pygame.Rect(700,300,SPCAESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow=pygame.Rect(100,300,SPCAESHIP_WIDTH,SPACESHIP_HEIGHT)



    clock=pygame.time.Clock()

    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                
        keys_pressed=pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed,red)
        draw_window(red,yellow)

    pygame.quit()

if __name__=="__main__":
    main()