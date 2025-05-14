import pygame as pg
from figura_class import Figura
import random

#inicializar los modulos de pygame
pg.init()
 #crear la pantalla o sourface
pantalla = pg.display.set_mode( (800,600) )#definición de tamaño de pantalla
pg.display.set_caption( "BOLILLAS  " )#agregar un título a mi ventana

game_over = False

listaBolillas=[]
for i in range(1,101):
    listaBolillas.append(Figura(random.randint(0,750),random.randint(0,550),random.randint(0,255),random.randint(0,255),random.randint(0,255),radio=random.randint(1,100)))

while not game_over:

    for eventos in pg.event.get():#capturar todos los eventos mientras el bucle se ejecute
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = True

    pantalla.fill( (12,222,245) )#asignar color a la pantalla

    for bolillas in listaBolillas:    
        bolillas.moverCirculo(800,600)
        bolillas.dibujarCirculo(pantalla)

    pg.display.flip()#función para cargar toda la configuración que va dentro de pantalla
   
pg.quit()
