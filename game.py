import pygame as py
import os
WIDTH,HEIGHT=700,700
WINDOW=py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("Nume joc")
Color=(204,255,255)
BLACK=(0,0,0)
RED=(255,0,255)
FPS=60 # frame per second
VELO=5
dimension=50
bullet_dim_x=20
bullet_dim_y=20

rock=[]


spaceshift_image_yellow=py.image.load(os.path.join("Chestii","Yellow.PNG")).convert()
spaceshift_image_yellow.set_colorkey((255, 255, 255)) #elimate the white color backgraund

bullets =[]
bullet_image=py.image.load(os.path.join("Chestii","bullet1.PNG")).convert()
bullet_image.set_colorkey((255, 255, 255))

s_yellow=py.transform.rotate(py.transform.scale(spaceshift_image_yellow,(dimension,dimension)),90)
bullet_i=py.transform.scale(bullet_image,(bullet_dim_x,bullet_dim_y))





def movement(keys_pressed,yellow):
       
    if keys_pressed[py.K_a] and yellow.x>0:#left
        yellow.x-=VELO
    if keys_pressed[py.K_d] and yellow.x+yellow.width<700:
        yellow.x+=VELO 

    if keys_pressed[py.K_w]and yellow.y>0:
        yellow.y-=VELO
    if keys_pressed[py.K_s] and yellow.y+yellow.height<700:
        yellow.y+=VELO  

def move_bullet(bullets):
    for b in bullets:
        b.y-=VELO

             
  


def build_window(yellow,buletts,rock):
     WINDOW.fill(Color)
     WINDOW.blit(s_yellow,(yellow.x,yellow.y))
   
     for b in buletts:
         WINDOW.blit(bullet_i,(b))

     for r in rock:
        py.draw.rect(WINDOW, RED, r, width=0, border_radius=0)
     #for i in range(7):
            

     py.display.update()


def collision(bullets,rock):
    for b in bullets:
        for target in rock:
            if b.colliderect(target):
                rock.remove(target)
def main():
    yellow=py.Rect(300,500,dimension,dimension)
    for i in range(7):
        rock_xy=py.Rect(i*100+32,30,30,30)
        rock.append(rock_xy)
    clock=py.time.Clock()
    run=True 
    while run:
        clock.tick(FPS)
        for event in py.event.get():
            if event.type==py.QUIT:
                run=False 
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    bullet_xy=py.Rect(yellow.x,yellow.y,bullet_dim_x+dimension//2,bullet_dim_y+dimension//2)
                    bullets.append(bullet_xy)  
        keys_pressed=py.key.get_pressed()
        movement(keys_pressed,yellow)   
        move_bullet(bullets)
        collision(bullets,rock)
        build_window(yellow,bullets,rock)

    py.quit()
if __name__=="__main__":
    main()
