from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

def angle_based_circle(xc, yc, r):
    glColor3f(0.8, 0.0, 0.0)
    glPointSize(2)

    glBegin(GL_POINTS)
    theta = 0.0
    while theta <= 360.0:
        rad = math.radians(theta)
        x = xc + r * math.cos(rad)
        y = yc + r * math.sin(rad)

        glVertex2f(x, y)
        theta += 1.0
    glEnd()

def main():
    angle_based_circle(250, 250, 120)
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
glutCreateWindow(b"Angle-Based Circle Drawing")

glutDisplayFunc(showScreen)

glutMainLoop()