import numpy as np
import sys

#Define a function f(x)
def f(x):
	return x**3+8

#Define a main function
def main():
	x = 9
	result = f(x)
	print(result)

	if result > 27:
		print("YAY!")

#Run the main function
if __name__ == "__main__":
	main()