def max(num1, num2):	
	if num1 < num2:
		print(f'{num2} katta')
	elif num1 > num2:
		print(f'{num1} katta')
	else:
		print(f'{num1}={num2}')

print(max(12, 15))