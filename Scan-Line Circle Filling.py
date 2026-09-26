from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

def scanline_circle_fill(xc, yc, r):
    glColor3f(0, 0.3, 0.4)

    for y in range(-r, r + 1):
        x_half = int(round(math.sqrt(r * r - y * y)))

        glBegin(GL_LINES)
        glVertex2f(xc - x_half, yc + y)
        glVertex2f(xc + x_half, yc + y)
        glEnd()

def main():
    scanline_circle_fill(250, 250, 120)
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
glutCreateWindow(b"Scan-Line Circle Filling")

glutDisplayFunc(showScreen)

glutMainLoop()