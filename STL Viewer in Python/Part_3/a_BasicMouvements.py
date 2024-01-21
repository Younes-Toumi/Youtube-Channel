import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def draw_triangle(triangle):

    glBegin(GL_TRIANGLES)
    # Rendering our Triangle here
    glColor3f(1.0, 1.0, 1.0)

    for vertex in triangle:
        glVertex3fv(vertex)

    glEnd()  

# Initializing our GL scene #

pygame.init()

FPS = 30 
clock = pygame.time.Clock()

display = pygame.display.set_mode( (1200, 800), DOUBLEBUF|OPENGL, 24)

gluPerspective(45, 1, 1, 500)
glClearColor(0.0, 0.5, 0.5, 1.0)
glTranslate(0, 0, -5)
# Triangle object we want to render

triangle = [
    (0.0, 1.0, 0.0), # Vertex 1
    (-0.866, -0.5, 0.0),  # Vertex 2
    (0.866, -0.5, 0.0)    # Vertex 3
]


# Main Loop #

running = True

while running:
    # Events to check for every Frame #

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                glRotatef(-event.rel[0], 0, 0, 1)

        if event.type == pygame.MOUSEWHEEL:

            scale = event.y/10 + 1 # +1.something, -1.something
            glScalef(scale, scale, scale)



    glClear(GL_COLOR_BUFFER_BIT)

    # Drawing our objects here

    draw_triangle(triangle)

    pygame.display.flip()
    pygame.display.set_caption(str(clock.get_fps()))
    clock.tick(FPS)
    







