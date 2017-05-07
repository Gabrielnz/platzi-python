"""
Programa que encuentra el primer caracter que no se repita adentro de un string.

"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""

def first_not_repeating_char(char_sequence):
	seen_letters = {}

	for i, letter in enumerate(char_sequence):
		# si la letra no esta en el diccionario de letras vistas
		# la agrega por primera vez, con la posicion en la que fue vista, y vista 1 vez
		if letter not in seen_letters:
			seen_letters[letter] = (i, 1)

		# si la letra si esta en el diccionario de letras vistas
		# aumenta la cantidad de veces que ha sido vista
		else:
			seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)

	final_letters = []
	for key, value in seen_letters.items():

		# si la letra actual fue vista 1 sola vez, la agrega junto con su indice.
		if value[1] == 1:
			final_letters.append( (key, value[0]) )

	# ordena la lista de letras no repetidas por su indice, usando sorted y lambda
	not_repeated_letters = sorted(final_letters, key=lambda value: value[1])

	# si hay letras que no se repiten, devuelve el valor de la primera.
	if not_repeated_letters:
		return not_repeated_letters[0][0]

	# si no hay letras que no se repiten
	else:
		return '_'

if __name__ == '__main__':
	char_sequence = str(input('Escribe una secuencia de caracteres: '))

	result = first_not_repeating_char(char_sequence)

	if result == '_':
		print('Todos los caracteres se repiten.')
	else:
		print('El primer caracter no repetido es: {}'.format(result))