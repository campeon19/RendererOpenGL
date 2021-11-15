import pygame
from gl import Renderer, Model
import numpy as np
import shaders

width = 960
height = 540

pygame.init()
screen = pygame.display.set_mode(
    (width, height), pygame.DOUBLEBUF | pygame.OPENGL)

clock = pygame.time.Clock()

rend = Renderer(screen)
rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)
vertex_data = np.array([-0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
                        0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
                        0.0, 0.5, 0.0, 0.0, 0.0, 1.0], dtype=np.float32)

rend.scene.append(Model(vertex_data))

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

    rend.render()

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
