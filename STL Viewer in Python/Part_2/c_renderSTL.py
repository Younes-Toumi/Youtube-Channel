import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from stl import mesh, Mode


# Initializing our GL scene #

pygame.init()

FPS = 60 
clock = pygame.time.Clock()

display = pygame.display.set_mode( (1200, 800), DOUBLEBUF|OPENGL, 24)

gluPerspective(45, 1, 1, 500)
glClearColor(0.0, 0.5, 0.5, 1.0)

glTranslatef(0.0, 0.0, -400)


# Defining our STL Model

stl_path = "STL Files//Sphere.stl"
stl_model = mesh.Mesh.from_file(stl_path)

vectors = stl_model.vectors
normals = stl_model.normals


glLineWidth(2)

# Main Loop #


running = True

while running:
    # Events to check for every Frame #

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    glClear(GL_COLOR_BUFFER_BIT)
    glRotatef(1, 1, 0, 0)
    # Drawing our objects here

    # Filled triangle
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    glBegin(GL_TRIANGLES)
    # Rendering our Triangle here
    glColor3f(1.0, 1.0, 1.0)

    for triangle in vectors:
        for vertex in triangle:
            glVertex3fv(vertex)

    glEnd()

    # Outlined triangle

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    glBegin(GL_TRIANGLES)
    # Rendering our Triangle here
    glColor3f(0.0, 0.0, 0.0)

    for triangle in vectors:
        for vertex in triangle:
            glVertex3fv(vertex)

    glEnd()

    pygame.display.flip()
    pygame.display.set_caption(str(clock.get_fps()))
    clock.tick(FPS)
    