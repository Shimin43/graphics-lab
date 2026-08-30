from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def main():

    glBegin(GL_QUADS)
    glColor3f(1, 0.8, 0.6)
    glVertex2f(150, 150)
    glVertex2f(350, 150)
    glVertex2f(350, 300)
    glVertex2f(150, 300)
    glEnd()


    glBegin(GL_TRIANGLES)
    glColor3f(0.8, 0, 0)
    glVertex2f(150, 300)
    glVertex2f(350, 300)
    glVertex2f(250, 380)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.5, 0.5, 0.5)
    glVertex2f(180, 120)
    glVertex2f(320, 120)
    glVertex2f(320, 150)
    glVertex2f(180, 150)
    glEnd()


    glBegin(GL_QUADS)
    glColor3f(0.6, 0.6, 0.6)
    glVertex2f(190, 100)
    glVertex2f(310, 100)
    glVertex2f(310, 120)
    glVertex2f(190, 120)
    glEnd()

    glFlush()

def showScreen():
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
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutCreateWindow(b"First lab")
glutDisplayFunc(showScreen)
glutMainLoop()
