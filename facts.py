import random

source="http://randomfactgenerator.net/"

def get_fact():
	with open("facts.txt", "r") as fact_file:
		no=random.randint(0, 2800)
		i=0
		for line in fact_file:
			if len(line)>5:
				i+=1
				if i==no:
					return line, source

#print get_fact()
