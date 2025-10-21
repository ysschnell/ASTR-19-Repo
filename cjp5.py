#Code Journal Prompt #5
import numpy as np


def main():
	print("sin(x) vs x")
	print("-"*50)
	x = np.linspace(0.0, 2.0*np.pi, num=1000, dtype=float) #Creates an array from 0.0 to 2pi with 1000 data points
	for item in x:
		print(f"{np.sin(item):>}{item:>}") #Formatting


if __name__=="__main__":
	main()