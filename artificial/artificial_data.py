import random

# create artificial DNA strings of length k 
def randomDNA(k):
	dna = ''
	for i in range(k):
		dna = dna + random.choice('ATCG')
	return dna
	
# provide a string s and probability p that each base in s mutates and return a new string
def mutateDNA(s,p):
	new = ''
	for i in range(len(s)):
		prob = random.random()
		if prob <= p:
			new = new + random.choice('ATCG')
		else:
			new = new + s[i]
	return new
	


  
