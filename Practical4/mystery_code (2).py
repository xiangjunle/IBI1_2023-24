# What does this piece of code do?
# Answer:Select 100 random numbers ranging from 1 to 10 and calculate their sum

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
total_random_number=0
# Cycle 100 times
while progress<100:
	progress+=1
	n = randint(1,10)
	total_random_number = total_random_number+n

print(total_random_number)
