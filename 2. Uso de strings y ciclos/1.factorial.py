"""
Programa para determinar un numero factorial.
"""

def factorial(number):
	# casos base
	if number == 0:
		return 1

	# llamada recursiva
	return number * factorial(number - 1)

# Nuestro programa empieza aqui.
if __name__ == '__main__':
	number = int(input('Escribe un número: '))

	result = factorial(number)

	print(result)