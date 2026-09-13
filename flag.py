from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def main():
    glBegin(GL_QUADS)
    
    glColor3f(0, 0.6, 0)
    glVertex2f(130, 200)
    glVertex2f(430, 200)
    glVertex2f(430, 380)
    glVertex2f(130, 380)
    
    glColor3f(1, 0, 0)
    glVertex2f(235, 245)
    glVertex2f(325, 245)
    glVertex2f(325, 335)
    glVertex2f(235, 335)
    
    glEnd()
    
    glBegin(GL_QUADS)
    
    glColor3f(0.45, 0.22, 0.08)
    glVertex2f(105, 80)
    glVertex2f(125, 80)
    glVertex2f(125, 400)
    glVertex2f(105, 400)
    
    glEnd()
    glFlush()

def showScreen():
    glClearColor(1, 1, 1, 1)
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
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Bangladesh Flag")
glutDisplayFunc(showScreen)
glutMainLoop()