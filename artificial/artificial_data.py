import random

# create artificial DNA strings of length k 
def randomDNA(k):
	dna = ''
	for i in range(k):
		dna = dna + random.choice('ATCG')
	return dna
	
# provide a DNA sequence and probability p that each base in DNA sequence mutates and return a new sequence
def mutateDNA(s,p):
	new = ''
	for i in range(len(s)):
		prob = random.random()
		if prob <= p:
			new = new + random.choice('ATCG')
		else:
			new = new + s[i]
	return new
	
# return list of n mutated strings starting with a DNA sequence s with probability p that each base in the DNA string mutates
def mutateDNAlist(s, p, n):
    dna  = s
    list = []
    list.append(s)
    for i in range(n):
        dna = mutateDNA(dna,p)
        list.append(dna)
    return list

# provide a list of DNAs and probability p that each base in a DNA sequence mutates and return new list of DNAs
def mutatelist(dnalist, p):
    newlist =[]
    for i in range(len(dnalist)):
        s = dnalist[i]
        newlist.append(mutateDNA(s,p))
    return newlist
            
# find consensus sequence given list of DNAs assuming all DNAs are equal length (may be slow for large inputs)
def consensusDNA(dnalist):
    consensus = ''
    for i in range(len(dnalist[0])):
        # dict to count number of ATCGs in each ith position of the current DNA
        counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        for k in range(len(dnalist)):
            current = dnalist[k]
            for j in 'ATCG':
                if current[i] == j:
                    counts[j] = counts[j] + 1
        for char in 'ATCG':
            if counts[char] == max(counts.values()):
                consensus = consensus + char
    return consensus
                
            
   
        
	
	


  
