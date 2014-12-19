''' 
Functions to generate strings corresponding to artificial DNA sequences, mutate DNA sequences based on given probability, and generate a consensus DNA sequence provided a list of DNA sequences.

Copy and paste the following block of text to run a sample test
dna1 = randomDNA(10) # generate 10 bp DNA random sequence
dnalist = mutateDNAlist(dna, 0.5, 5) # generate list of 11 1000 bp DNA sequence (includes dna1). The base of each sequence is generated using the corresponding base in dna1 as a basis with a mutation probability of 0.375 (0.5*0.75). 
newlist = remove_multiple_snps(dnalist) # remove common bases at the same position for all sequences in the list and return a new list
hamming_distance_list(newlist) # for each sequence in the new list, display its distance to other sequences
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
def hamming_distance_list(dnalist):
    # list to store distances for each sequence from all sequences in dnalist
    distance_list = []
    for seq in dnalist: 
        # dict to store Hamming distance from current sequence
        distance = {} 
        for i in range(len(dnalist)):
            d = hamming_distance2(seq, dnalist[i])  
            # setdefault() is similar to get(), but will set dict[key]=default if key is not already in dict
            distance.setdefault(d,[]).append(dnalist[i])
        distance_list.append(distance)
    for k in range(len(distance_list)):
        print 'The sequences in increasing distance from ',distance_list[k][0], ' are :', distance_list[k]
    return distance_list
        
# Given a list of sequences assuming all of equal length, remove common SNPs in all sequence starting from the ith column (start from 1st column by default)
def remove_multiple_snps(dnalist, i = 0):
	# copy list of sequnces
    newlist = dnalist[:]
    # go over all sequences column by column
    while i < len(dnalist[0]):
        # list of nucleotides in current column for all sequences
        column_list = []
        for k in range(len(dnalist)):
            current = dnalist[k]
            column_list.append(current[i])
        i = i + 1
        # if the column has the same nucleotide, remove column from all sequences
        if column_list.count('A') == len(column_list) or column_list.count('T') == len(column_list) or column_list.count('C') == len(column_list) or column_list.count('G') == len(column_list):
            # copy current list
            sublist = newlist[:]
            # clear current list
            del newlist[:]
            # use copy of current list to create new list by removing nucleotide in the column for all sequences
            for k in range(len(dnalist)):
                if i == 0:
                    newlist.append(sublist[k][i+1:])
                else:
                    newlist.append(sublist[k][:i-1] + sublist[k][min(i, len(sublist[k])):])
            return remove_multiple_snps(newlist, i - 1)
    return newlist

  
