from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

def triangle_fan_circle(xc, yc, r, segments=100):
    glColor3f(0, 0.5, 0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(xc, yc)
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        x = xc + r * math.cos(angle)
        y = yc + r * math.sin(angle)
        glVertex2f(x, y)
    glEnd()

def main():
    triangle_fan_circle(250, 250, 120)
    glFlush()

def showScreen():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
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
glutCreateWindow(b"Circle Using Triangle Fan")
glutDisplayFunc(showScreen)
glutMainLoop()