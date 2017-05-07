"""
Programa que determina su una palabra es palindromo.
"""

def palindrome(word):
	# genera un string desde atras hacia adelante
	reversed_word = word[::-1]

	if reversed_word == word:
		return True
	else:
		return False

if __name__ == '__main__':
	word = str(input('Escribe una palabra: '))

	result = palindrome(word)

	if result is True:
		print('{} sí es un palindromo.'.format(word))
	else:
		print('{} NO es un palindromo.'.format(word))