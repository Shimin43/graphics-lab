from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def bresenham_circle(xc, yc, r):
    x = 0
    y = r
    d = 1 - r

    glBegin(GL_POINTS)
    plot_points(xc, yc, x, y)

    while x < y:
        x += 1
        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1
            d += 2 * (x - y) + 1

        plot_points(xc, yc, x, y)

    glEnd()

def plot_points(xc, yc, x, y):
    glVertex2f(xc + x, yc + y)
    glVertex2f(xc - x, yc + y)
    glVertex2f(xc + x, yc - y)
    glVertex2f(xc - x, yc - y)
    glVertex2f(xc + y, yc + x)
    glVertex2f(xc - y, yc + x)
    glVertex2f(xc + y, yc - x)
    glVertex2f(xc - y, yc - x)

def main():
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(2)
    bresenham_circle(250, 250, 120)   # ← indent ঠিক করা হয়েছে
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
glutCreateWindow(b"Bresenham Circle")
glutDisplayFunc(showScreen)
glutMainLoop()
