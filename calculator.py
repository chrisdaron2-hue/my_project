
def single_calculation():
	data = input("Type your calculation in the format <number> <operator> <number>: ")
	parsed = data.split()
	num1 = int(parsed[0])
	num2 = int(parsed[2])
	op = parsed[1]
  
	if op == '+':
		res = num1 + num2
	elif op == '-':
		res = num1 - num2
	elif op == '*':
		res = num1 * num2

	print(f"The answer is {res}")


def main():
	print("Welcome to the Python calculator!")

	n_calculations = int(input("How many calculations do you want to do? "))
	for i in range(n_calculations):
		single_calculation()


if __name__ == "__main__":
	main()
