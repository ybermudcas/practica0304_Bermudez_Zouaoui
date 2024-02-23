import pygame
from random import randint
#Comienzo de la extension pygame
pygame.init()

#Creacion de la pantalla de la superficie
window = pygame.display.set_mode((800,600))#Aqui tenemos las dimensiones que tiene nuestra ventana de juego
pygame.display.set_caption('Arkanoid_Prueba')

#Creacion de la pelota de juego
ball = pygame.image.load("ball.png")

#Tener el rectángulo de la imagen utilizada
ballrect = ball.get_rect()

#Pondremos unos valores que tendra la velocidad inicial nuestra pelota
speed = [4,4]

#Posicion inicial de nuestra pelota que sera en el origen de coordenandas
ballrect.move_ip(400,300)

#Creamos una barra para nuestro juego para el rebote con nuestro pelota y su rectangulo
barra = pygame.image.load ("barra_nuevo.png")
barrarect = barra.get_rect()

#Posicionamiento de nuestra barra
barrarect.move_ip(300,550)

#Creamos un ladrillo en el rectangulo
l1 = pygame.image.load("lad.azul.png")
l1rect = barra.get_rect()

#Escogemos la posición donde queremos que esté nuestro ladrillo
l1rect.move_ip(150,200)

#Bucle principal del arkonaid
jugar = True 
while jugar: #esto hara que mientras jugar sea true este en funcionamiento
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugar = False #Con esto el bucle ira comporbando si el boton de la ventana esta abierto si no es asi se cerrara y se quitara el juego.
    
    #Comprobacion del pulsamiento de una tecla para su movimiento
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:#movimiento para la izquierda y cuanto se mueve
        barrarect = barrarect.move(-2,0)
    if keys [pygame.K_RIGHT]:#movimiento para la derecha y cuanto se mueve
        barrarect = barrarect.move(2,0)
    
    if l1rect.colliderect(ballrect): #Si la bola choca con el rectangulo pasa lo siguiente
        speed[1] = -speed[1]
        # Rompe el ladrillo moviendolo a una posición del eje x fuera de pantalla
        l1rect.x = -1000

    #movimiento de la pelota
    ballrect = ballrect.move(speed)

    #limite para nuestra barra y no se escape de la pantalla
    #Pondremos un comprobador para cuando choque la pelota a los limites de la pantalla o cuando choque con la barra
    if barrarect.colliderect(ballrect):#comprueba si los hitboxs chocan
        speed[1] = -speed[1]
    if ballrect.left < 0 or ballrect.right > window.get_width():
        speed [0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > window.get_height():
        speed [1] = -speed[1]
    if ballrect.bottom > window.get_height():
        window.blit()
    #Pintaremos la ventana de juego de un color que nosotros queramos dentro del bucle lo haremos.
    window.fill((3,100,100))
    #dibujamos la pelota y la barra
    window.blit(barra,barrarect)
    window.blit(ball,ballrect)
    window.blit(l1,l1rect)
    #Los elemntos del juego se redibujan.
    pygame.display.flip()
    #Para tener una tasa de refresco(FPS)
    pygame.time.Clock().tick(60)
    
    import pygame

pygame.quit()

