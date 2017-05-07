
def binary_search(numbers, number_to_find, low, high):
	# primer caso base: si el indice bajo es mas alto que el indice alto
	# el numero no se encuentra en la lista actual
	if low > high:
		return False

	mid = (low + high) // 2

	# segundo caso base: si el numero del medio de la lista
	# es el numero que estamos buscando, el numero fue encontrado
	if numbers[mid] == number_to_find:
		return True

	# primera llamada recursiva: si el numero del medio es mayor que el numero
	# que queremos encontrar, se hace la llamada recursiva ajustando los indices
	# hacia la parte inferior que toca buscar
	elif numbers[mid] > number_to_find:
		return binary_search(numbers, number_to_find, low, mid - 1)
	
	# segunda llamada recursiva: si el numero del medio es menor que el numero
	# que queremos encontrar, se hace la llamada recursiva ajustando los indices
	# hacia la parte superior que toca buscar
	else:
		return binary_search(numbers, number_to_find, mid + 1, high)


if __name__ == '__main__':
	numbers = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]

	number_to_find = int(input('Ingresa un número: '))

	result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)

	if result is True:
		print('El número {} Sí está en la lista.'.format(number_to_find))
	else:
		print('El número {} NO está en la lista.'.format(number_to_find))