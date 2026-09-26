from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

def draw_quad(x1, y1, x2, y2, x3, y3, x4, y4, r, g, b):
    glColor3f(r, g, b)
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glVertex2f(x4, y4)
    glEnd()

def draw_circle(xc, yc, r, segments=100):
    glColor3f(1, 0, 0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(xc, yc)
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        x = xc + r * math.cos(angle)
        y = yc + r * math.sin(angle)
        glVertex2f(x, y)
    glEnd()

def main():
    draw_quad(
        145, 100,
        165, 100,
        165, 480,
        145, 480,
        0.4, 0.4, 0.4
    )
    draw_quad(
        120, 60,
        190, 60,
        190, 100,
        120, 100,
        0.25, 0.25, 0.25
    )
    draw_quad(
        165, 300,
        430, 300,
        430, 480,
        165, 480,
        0.0, 0.42, 0.18
    )
    draw_circle(280, 390, 45)
    glFlush()

def showScreen():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 500, 0, 500, 0, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    main()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(200, 200)
glutCreateWindow(b"Bangladesh Flag")
glutDisplayFunc(showScreen)
glutMainLoop()