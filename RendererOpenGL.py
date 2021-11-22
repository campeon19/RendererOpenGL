import pygame
from pygame.locals import *
import numpy as np
from gl import Renderer, Model
import shaders


width = 960
height = 540

deltaTime = 0.0

pygame.init()
screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL )
clock = pygame.time.Clock()

rend = Renderer(screen)
rend.setShaders(shaders.vertex_toonShader, shaders.fragment_toonShader)

face = Model('models/model.obj', 'models/model.bmp')
face.position.z = -5

rend.scene.append( face )


isRunning = True
while isRunning:


    keys = pygame.key.get_pressed()

    # Traslacion de camara
    if keys[K_d]:
        rend.camPosition.x += 2 * deltaTime
    if keys[K_a]:
        rend.camPosition.x -= 2 * deltaTime
    if keys[K_w]:
        rend.camPosition.z += 2 * deltaTime
    if keys[K_s]:
        rend.camPosition.z -= 2 * deltaTime
    if keys[K_q]:
        rend.camPosition.y -= 2 * deltaTime
    if keys[K_e]:
        rend.camPosition.y += 2 * deltaTime
    
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

    rend.tiempo += deltaTime
    deltaTime = clock.tick(60) / 1000

    rend.update()
    rend.render()

    pygame.display.flip()

pygame.quit()
