clonalSNPs
==========
Depict clonal divergence of S.aureus strains by comparing the SNPs profile of related S.aureus strains to a reference strain

To do

A. For a cluster of related strains.

1. generate artificial sequence of SNPs represented as strings

2. generate consensus sequence base on list of SNPs sequence corresponding to different "strains"

3. calculate probability of observing each SNPs sequence base on consensus sequence (probability matrix) or calculate distance from each SNPs sequence to consensus sequence (number of differences between given SNPs sequence and consensus sequence)

4. for each strain, rank its relatedness (by probability or distance) to all other strains

5. hypothesize divergence pattern (note: distance matrix may miss nodes, Neighbour joining)
