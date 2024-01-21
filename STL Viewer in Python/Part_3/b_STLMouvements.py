import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from stl import mesh
import numpy as np

stl_path = "STL Files//Sphere.stl"
stl_model = mesh.Mesh.from_file(stl_path)

vectors = stl_model.vectors
normals = stl_model.normals

def shift_to_chenter(triangles):
    
    min_p = np.min(triangles, axis=0) # x_min, y_min, z_min
    max_p = np.max(triangles, axis=0) # x_max, y_max, z_max 

    center = (min_p + max_p)/2

    return triangles - center

def draw_stl(triangles):
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_TRIANGLES)
    # Rendering our Triangle here
    glColor3f(1.0, 1.0, 1.0)

    for triangle in triangles:
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

triangles = shift_to_chenter(vectors)

# Main Loop #

running = True

while running:
    # Events to check for every Frame #

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                
                glRotatef(event.rel[0], 0, 1, 0) #Rotation along the y axis, with the x_mouse_position
                glRotatef(event.rel[1], 1, 0, 0) #Rotation along the x axis, with the y_mouse_position

        if event.type == pygame.MOUSEWHEEL:

            scale = event.y/10 + 1 # +1.something, -1.something
            glScalef(scale, scale, scale)



    glClear(GL_COLOR_BUFFER_BIT)

    # Drawing our objects here

    draw_stl(triangles)

    pygame.display.flip()
    pygame.display.set_caption(str(clock.get_fps()))
    clock.tick(FPS)
    







