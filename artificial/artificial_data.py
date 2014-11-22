''' 
Functions to generate strings corresponding to artificial DNA sequences, mutate DNA sequences based on given probability, and generate a consensus DNA sequence provided a list of DNA sequences.
'''

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
            
# find consensus sequence given list of DNAs assuming all DNAs are of equal length (may be slow for large inputs)
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
            # add only the left most base in 'ATCG' if more two or more bases have same max count, need to generate list of consensus sequence or use probabilistic method
            if counts[char] == max(counts.values()):
                consensus = consensus + char
                break
    return consensus

# find number of mismatches, Hamming distance, between two DNA sequences x and y of equal length. For Python 3.3 +, Hamming distance has been implemented, use import distance, distance.hamming().
def hamming_distance2(x, y):
    assert len(x) == len(y)
    mismatches = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            mismatches = mismatches + 1
    return mismatches
 
# return a list of Hamming distance between each DNA sequence in a list of DNA sequences
def hamming_distance_list(x, dnalist):
    # list to store distances for each sequence from all sequences in dnalist
    distance_list = []
    for seq in dnalist: 
        # dict to store Hamming distance from current sequence
        distance = {} 
        for i in range(len(dnalist)):
            d = hamming_distance2(x, dnalist[i])  
            distance.setdefault(d,[]).append(dnalist[i])
        distance_list.append(distance)
    k = 0
    for seq in dnalist:
        print 'closest sequences to ' , seq, ' in list are ', distance_list[k]
        k = k + 1
    return distance_list
        
	
	


  
