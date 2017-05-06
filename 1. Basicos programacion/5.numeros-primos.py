"""
Programa para determinar si un numero es primo.
"""
# -- coding: utf-8 -*-

def is_prime(number):

	# si el numero es menor que 2, no es primo
	if number < 2:
		result = False

	# si el numero es igual a 2, es primo
	elif number == 2:
		result = True
	
	# si el numero es mayor que 2 y es divisible entre 2, no es primo
	elif number > 2 and number % 2 == 0:
		result = False
	
	# si el numero es mayor que 2 y no es divisible entre 2
	else:
		# toma el valor True antes de iterar en el ciclo
		result = True

		for i in range(3, number):
			# si el numero que estamos evaluando es divisible entre alguno
			# de los numeros contenidos en el mismo, no es primo, se sale del ciclo con valor False
			if number % i == 0:
				result = False
				break

	return result

def run():
	number = int(input('Escribe un numero: '))

	result = is_prime(number)

	if result is True:
		print('Tu numero es primo\n')
	else:
		print('Tu numero NO es primo\n')

# Nuestro programa empieza aqui.
if __name__ == '__main__':
	run()