clonalSNPs
==========
Depict clonal divergence of S.aureus strains by comparing the SNPs profile of related S.aureus strains to a reference strain

To do

A. For a cluster of related strains.

1. generate artificial sequence of SNPs represented as strings

2. generate consensus sequence base on list of SNPs sequence corresponding to different "strains" (difficulty with multiple equally common bases, may not need consensus sequence)

3a. calculate probability of observing each SNPs sequence base on consensus sequence (probability matrix) or calculate distance from each SNPs sequence to consensus sequence (number of differences between given SNPs sequence and consensus sequence)

3b. currently calculating Hamming distance between each strain using dynamic programming (memory cost)

4. for each strain, rank its relatedness (by probability or distance) to all other strains

5. hypothesize divergence pattern 

B. For database of sequences. 

1. define "rare SNPs" as SNPs appearing at or below certain frequency

2. for each strain, find the two most closesly related strains

3. compare to results using multilocus sequencing type

4. potential issues with insignificant SNPs considered as "rare SNPs", indels affect Hamming distance (may need edit distance)
