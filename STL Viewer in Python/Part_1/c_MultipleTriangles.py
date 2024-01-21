import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *



# Initializing our GL scene #

pygame.init()

FPS = 60 
clock = pygame.time.Clock()

display = pygame.display.set_mode( (1200, 800), DOUBLEBUF|OPENGL, 24)

gluPerspective(45, 1, 1, 500)
glClearColor(0.0, 0.5, 0.5, 1.0)

# Defining our Tringle

triangles = [
    ((-1.0, -1.0, -5.0), (1.0, -1.0, -5.0), (0.0, 1.0, -5.0)),  # Triangle 1

    ((-1.0, -1.0, -5.0), (-1.0, 1.0, -5.0), (0.0, 1.0, -5.0)),  # Triangle 2

    ((1.0, -1.0, -5.0), (1.0, 1.0, -5.0), (0.0, 1.0, -5.0))     # Triangle 3
]

glLineWidth(5)

# Main Loop #


running = True

while running:
    # Events to check for every Frame #

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    glClear(GL_COLOR_BUFFER_BIT)

    # Drawing our objects here

    # Filled triangle
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    glBegin(GL_TRIANGLES)
    # Rendering our Triangle here
    glColor3f(1.0, 1.0, 1.0)

    for triangle in triangles:
        for vertex in triangle:
            glVertex3fv(vertex)

    glEnd()

    # Outlined triangle

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    glBegin(GL_TRIANGLES)
    # Rendering our Triangle here
    glColor3f(0.0, 0.0, 0.0)

    for triangle in triangles:
        for vertex in triangle:
            glVertex3fv(vertex)

    glEnd()

    pygame.display.flip()
    pygame.display.set_caption(str(clock.get_fps()))
    clock.tick(FPS)
    