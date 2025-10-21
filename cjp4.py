Code Journal Prompt #4
import sys

#Create the class
class Penguin:

	def print(self):
		print("Galapagos penguins are my favorite animal!")
		print(f"Length of the arms: {self.arm_length}")
		print(f"Length of the legs: {self.leg_length}")
		print(f"Number of eyes: {self.num_eyes}")
		print(f"Tail?: {self.tail}")
		print(f"Furry?:{self.furry}")

	def __init__(self, arm_length, leg_length, num_eyes, tail, furry):
		self.arm_length = arm_length
		self.leg_length = leg_length
		self.num_eyes = num_eyes
		self.tail = tail
		self.furry = furry

#Define the main function
def main(): 
	arm_length = 5.3
	leg_length = 7.0
	num_eyes = 2
	tail = True
	furry = False

	my_penguin = Penguin(arm_length=arm_length, leg_length=leg_length, num_eyes=num_eyes, tail=tail, furry=furry)
	my_penguin.print()

if __name__ == "__main__":
	main()
