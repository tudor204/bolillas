import pygame as pg

#inicializar los modulos de pygame
pg.init()

 #crear la pantalla o sourface
pantalla = pg.display.set_mode( (800,600) )#definición de tamaño de pantalla
pg.display.set_caption( "BOLILLAS  " )#agregar un título a mi ventana

game_over = False

x=0
vx=1
y=300
vy=1

x2=780
vx2=1
y2=300
vy2=1

while not game_over:

    for eventos in pg.event.get():#capturar todos los eventos mientras el bucle se ejecute
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = True

    pantalla.fill( (12,222,245) )#asignar color a la pantalla
    
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
    # la pantalla o souface, color en rgb, posiciones(posición ancho, posicion largo,tamaño del rect largo, tamaño de rec ancho)
    pg.draw.rect(pantalla, (243, 96, 12),(x,y,20,20))#dibujar un rectángulo
    pg.draw.rect(pantalla, (243, 12, 138),(x2,y2,20,20))#dibujar un rectángulo


    
    pg.display.flip()#función para cargar toda la configuración que va dentro de pantalla
   
pg.quit()
