# Christian Daniel Pérez De León
# Carne: 19710
# Graficas por Computador

import pygame
from pygame.locals import *
import numpy as np
from gl import Renderer, Model
import shaders



width = 960
height = 540

deltaTime = 0.0

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL )
clock = pygame.time.Clock()

rend = Renderer(screen)
rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)

face = Model('models/model.obj', 'models/model.bmp')
face2 = Model('models/Mario.obj', 'models/mario_fire.png')
face3 = Model('models/Luigi.obj', 'models//luigiD.jpg')
face4 = Model('models/yoshi2.obj', 'models/yoshi color.png')
face5 = Model('models/Koopa.obj', 'models/Koopa.png')
face6 = Model('models/extra_life.obj', 'models/Extra_Life_tex.png')
face7 = Model('models/Suzanne.obj', 'models/white.jpg')

face.position.z = -5
face2.position.z = -5
face3.position.z = -5
face4.position.z = -5
face5.position.z = -5
face6.position.z = -5
face7.position.z = -5

contador = 0
def contador_fun():
    global contador
    contador += 1
    contador = contador % 7
    return contador


rend.scene.append( face )
rend.scene.append( face2 )
rend.scene.append( face3 )
rend.scene.append( face4 )
rend.scene.append( face5 )
rend.scene.append( face6 )
rend.scene.append( face7 )


pygame.mixer.music.load('./SoundTracks/Stellar Wind.mp3')
pygame.mixer.music.play(-1)
isRunning = True

while isRunning:


    keys = pygame.key.get_pressed()

    # Traslacion de camara
    if keys[K_d]:
        # rend.camPosition.x += 2 * deltaTime
        rend.rotateLeft(deltaTime * 20)
    if keys[K_a]:
        # rend.camPosition.x -= 2 * deltaTime
        rend.rotateRight(deltaTime * 20)
    if keys[K_w]:
        # rend.camPosition.z += 2 * deltaTime
        rend.ZoomIn(deltaTime * 20)
    if keys[K_s]:
        # rend.camPosition.z -= 2 * deltaTime
        rend.ZoomOut(deltaTime * 20)
    if keys[K_q]:
        # rend.camPosition.y -= 2 * deltaTime
        rend.rotateUp(deltaTime * 20)
    if keys[K_e]:
        # rend.camPosition.y += 2 * deltaTime
        rend.rotateDown(deltaTime * 20)
    
    if keys[K_LEFT]:
        if rend.valor > 0:
            rend.valor -= 0.1 * deltaTime

    if keys[K_RIGHT]:
        if rend.valor < 0.2:
            rend.valor += 0.1 * deltaTime
    
    



    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isRunning = False

        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                isRunning = False

            if ev.key == K_1:
                rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)
            if ev.key == K_2:
                rend.setShaders(shaders.vertex_toonShader, shaders.fragment_toonShader)
            if ev.key == K_3:
                rend.setShaders(shaders.vertex_Shader2, shaders.fragment_Shader2)
            if ev.key == K_4:
                rend.setShaders(shaders.vertex_Shader3, shaders.fragment_Shader3)
            if ev.key == K_5:
                rend.setShaders(shaders.vertex_Shader4, shaders.fragment_Shader4)
            if ev.key == K_6:
                rend.setShaders(shaders.vertex_Shader5, shaders.fragment_Shader5)
            if ev.key == K_7:
                rend.setShaders(shaders.vertex_Shader6, shaders.fragment_Shader6)
            if ev.key == K_8:
                rend.wireframeMode()
            if ev.key == K_9:
                rend.filledMode()
                
            if ev.key == K_RETURN:
                contador_fun()
                rend.currentModelIndex = contador
            if ev.key == K_SPACE:
                pygame.mixer.music.load('./SoundTracks/Nine Lives.mp3')
                pygame.mixer.music.play(-1)

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 4:
                rend.ZoomIn(4)
            if ev.button == 5:
                rend.ZoomOut(4)

        if pygame.mouse.get_pressed()[0]:
            mouse_movement = pygame.mouse.get_rel()

            if mouse_movement[0] != 0:
                if mouse_movement[0] > 0:
                    target = rend.scene[0].position
                    rend.rotateRight(3)
                elif mouse_movement[0] < 0:
                    target = rend.scene[0].position
                    rend.rotateLeft(3)

            if mouse_movement[1] != 0:
                if mouse_movement[1] > 0:
                    target = rend.scene[0].position
                    rend.rotateDown(3)
                elif mouse_movement[1] < 0:
                    target = rend.scene[0].position
                    rend.rotateUp(3)
                

    rend.tiempo += deltaTime
    deltaTime = clock.tick(60) / 1000

    # rend.update()
    rend.render()

    pygame.display.flip()

pygame.quit()
