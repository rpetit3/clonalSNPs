import random

# create artificial DNA strings of length k 
def randomDNA(k):
	dna = ''
	for i in range(k):
		dna = dna + random.choice('ATCG')
	return dna


  
