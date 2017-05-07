# modulo de python que sirve para generar programas graficos
import turtle

def main():
	window = turtle.Screen()
	gabriel = turtle.Turtle()

	make_square(gabriel)

	turtle.mainloop()

def make_square(gabriel):
	length = int(input('Tamaño de cuadrado: '))

	for i in range(4):
		make_line_and_turn(gabriel, length)

def make_line_and_turn(gabriel, length):
	gabriel.forward(length)
	gabriel.left(90)

# si python determina que este archivo es el main, empieza desde aqui.
if __name__ == '__main__':
	main()