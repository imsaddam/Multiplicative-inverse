def calculate_euclidian_extended_algorithm(input1, input2):
	if input1 == 0:
		return (input2, 0, 1)
	else:
		gcd, a, b = calculate_euclidian_extended_algorithm(input2 % input1, input1)
		return (gcd, b - (input2//input1) * a, a)

def inverse(input1,n):
  gcd, a, b = calculate_euclidian_extended_algorithm(input1, n)
  if gcd == 1:
    print(a)
  else:
    print(str(input1)+" has no inverse modulo "+ str(n))

input1 = int(input("Enter input One = "))
n = int(input("Enter input Two = "))
print("The Output is = ")

inverse(input1,n)
