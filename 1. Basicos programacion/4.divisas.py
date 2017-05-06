"""
Calculadora de divisas que convierte de pesos mexicanos a pesos colombianos.
"""
# -- coding: utf-8 -*-

def foreign_exchange_calculator(amount):
	mex_to_col_rate = 145.97

	return mex_to_col_rate * amount

def run():
	print('C A L C U L A D O R A  D E  D I V I S A S')
	print('Convierte pesos mexicanos en pesos colombianos.')
	print('')

	amount = float(input('Ingresa la cantidad de pesos mexicanos que quieres convertir: '))

	result = foreign_exchange_calculator(amount)

	print('${} pesos mexicanos son ${} pesos colombianos'.format(amount, result))
	print('')

# Nuestro programa empieza aqui.
if __name__ == '__main__':
	run()
	print('El programa termina aqui.')
	print('')