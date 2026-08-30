from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
 
def main():
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex2f(100, 100)
    glVertex2f(300,300)

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
glutCreateWindow(b"Lab report")
glutDisplayFunc(showScreen)
glutMainLoop()
