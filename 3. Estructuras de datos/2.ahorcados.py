
import random

# Constantes
IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]


def random_word():
	return random.choice(WORDS)


def display_board(hidden_word, tries):
	print(IMAGES[tries])
	print('')
	print(hidden_word)
	print('--- * --- * --- * --- * --- * ---')


def run():
	word = random_word()
	hidden_word = ['-'] * len(word)
	tries = 0

	while True:
		display_board(hidden_word, tries)
		current_letter = str(input('Escoge una letra: '))

		letter_indexes = []
		
		# Almacena los indices de la palabra en donde ocurre la letra presionada
		for i in range(len(word)):
			if word[i] == current_letter:
				letter_indexes.append(i)

		# si la letra presionada no esta en la palabra
		if len(letter_indexes) == 0:
			tries += 1

			# si falla con 7 intentos, perdiste.
			if tries == 7:
				display_board(hidden_word, tries)
				print('')
				print('¡Perdiste! La palabra correcta era: {}'.format(word))
				break

		# si la letra presionada si esta en la palabra
		else:
			# sustituye los simbolos de la palabra escondida
			# por las occurrencias de la letra encontrada
			for i in letter_indexes:
				hidden_word[i] = current_letter

			letter_indexes = []

			# si ya no quedan letras ocultas por descubrir, ganaste.
			try:
				hidden_word.index('-')
			except ValueError:
				print('')
				print('¡Felicidades! Ganaste. La palabra es: {}'.format(word))
				break



if __name__ == '__main__':
	print('B I E N V E N I D O S  A  A H O R C A D O S')
	run()