import pygame
import os
pygame.font.init()
WIDTH,HEIGHT=900,500
RED=(255,0,0)
YELLOW=(255,255,0)
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Second Game")
BLACK=(0,0,0)
WHITE=(255,255,255)

YELLOW_HIT=pygame.USEREVENT+1
RED_HIT=pygame.USEREVENT+2

BORDER=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)

HEALTH_FONT=pygame.font.SysFont("comiscans",40)
WINNER_FONT=pygame.font.SysFont("comiscsans",100)
FPS=60
VELOCITY=5
BULLET_VELOCITY=7
MAX_BULLETS=3

SPCAESHIP_WIDTH,SPACESHIP_HEIGHT=55,40

YELLOW_SPACESHIP_IMAGE=pygame.image.load(os.path.join("images","spaceship_yellow.png"))
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPCAESHIP_WIDTH,SPACESHIP_HEIGHT)),90)

RED_SPACESHIP_IMAGE=pygame.image.load('images/spaceship_red.png')
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPCAESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
SPACE=pygame.transform.scale(pygame.image.load(os.path.join('images','space.png')),(WIDTH,HEIGHT))



def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):

    #WIN.fill(WHITE)
    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN,BLACK,BORDER)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    
    red_health_text=HEALTH_FONT.render("Health: "+str(red_health),1,WHITE)
    yellow_health_text=HEALTH_FONT.render("Health:"+str(yellow_health),1,WHITE)
    WIN.blit(red_health_text,(WIDTH-red_health_text.get_width()-10,10))
    WIN.blit(yellow_health_text,(10,10))
    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW,bullet)
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


def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x+=BULLET_VELOCITY
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x>WIDTH:
            yellow_bullets.remove(bullet)


    for bullet in red_bullets:
        bullet.x-=BULLET_VELOCITY
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x<0:
            red_bullets.remove(bullet)

def draw_winner(text):
    draw_winner_text=WINNER_FONT.render(text,1,WHITE)
    WIN.blit(draw_winner_text,(WIDTH/2-draw_winner_text.get_width()/2,HEIGHT/2-draw_winner_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)
def main():
    red=pygame.Rect(700,300,SPCAESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow=pygame.Rect(100,300,SPCAESHIP_WIDTH,SPACESHIP_HEIGHT)

    red_bullets=[]
    yellow_bullets=[]



    red_health=10
    yellow_health=10
    clock=pygame.time.Clock()

    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LCTRL and len(yellow_bullets)<MAX_BULLETS:
                    bullet=pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2-2,10,5)
                    yellow_bullets.append(bullet)
                if event.key==pygame.K_RCTRL and len(red_bullets)<MAX_BULLETS:
                    bullet=pygame.Rect(red.x,red.y+red.height//2-2,10,5)
                    red_bullets.append(bullet)
            if event.type==RED_HIT:
                red_health-=1
            if event.type ==YELLOW_HIT:
                yellow_health-=1
        winner_text=""   
        if red_health<=0:
            winner_text="YELLOW WINS"
        if yellow_health<=0:
            winner_text="RED WINS"
        if winner_text!="":
            draw_winner(winner_text)
            break
        keys_pressed=pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed,red)
        
        handle_bullets(yellow_bullets,red_bullets,yellow,red)

        draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health)
    pygame.quit()

if __name__=="__main__":
    main()  