import pygame as pg
from figura_class import Rectangulo

#inicializar los modulos de pygame
pg.init()

 #crear la pantalla o sourface
pantalla = pg.display.set_mode( (800,600) )#definición de tamaño de pantalla
pg.display.set_caption( "BOLILLAS  " )#agregar un título a mi ventana

game_over = False

rectangulo1=Rectangulo(400,300)
rectangulo2=Rectangulo(300,200,(192,6,211),30,30)
rectangulo1.velocidad(1,1)
rectangulo2.velocidad(2,2)
"""
x=0
vx=1
y=300
vy=1

x2=780
vx2=1
y2=300
vy2=1
"""
while not game_over:

    for eventos in pg.event.get():#capturar todos los eventos mientras el bucle se ejecute
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = True

    pantalla.fill( (12,222,245) )#asignar color a la pantalla
    
    rectangulo1.mover(800,600)
    rectangulo2.mover(800,600)
    """
    x += vx
    y += vy 
    if x >= 800 or x==0:#los limites en x
        vx *= -1
    if y >= 600 or y==0:#los limites en y
        vy *= -1

    x2 += vx2
    y2 += vy2 
    if x2 >= 800 or x2==0:#los limites en x
        vx2 *= -1
    if y2 >= 600 or y2==0:#los limites en y
        vy2 *= -1
    #y -= 1
    """
    # la pantalla o souface, color en rgb, posiciones(posición ancho, posicion largo,tamaño del rect largo, tamaño de rec ancho)
    pg.draw.rect(pantalla, rectangulo1.color,(rectangulo1.pos_x,rectangulo1.pos_y,rectangulo1.w,rectangulo1.h))#dibujar un rectángulo
    pg.draw.rect(pantalla, rectangulo2.color,(rectangulo2.pos_x,rectangulo2.pos_y,rectangulo2.w,rectangulo2.h))#dibujar un rectángulo


    
    pg.display.flip()#función para cargar toda la configuración que va dentro de pantalla
   
pg.quit()
