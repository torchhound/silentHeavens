import random

def coordGen():
	"""Returns a random integer between 1 and 70,000"""
	return random.randrange(1, 70000) #10,000 star systems * typical separation of 6.57 light years rounded up to 7 = 70,000

def main():
	print(coordGen())

if __name__ == "__main__":
	main()