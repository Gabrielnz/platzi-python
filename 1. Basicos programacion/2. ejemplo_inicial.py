"""
Vamos a crear un cuadrado.
Crear un cuadrado significa generar lineas y dar vueltas.
"""

# modulo de python que sirve para generar programas graficos
import turtle

window = turtle.Screen() # instancia de ventana
gabriel = turtle.Turtle() # instancia de tortuga

gabriel.forward(50)
gabriel.left(90)

gabriel.forward(50)
gabriel.left(90)

gabriel.forward(50)
gabriel.left(90)

gabriel.forward(50)
gabriel.left(90)

turtle.mainloop() # previene que turtle cierre la ventana