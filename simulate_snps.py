#! /usr/bin/env python
"""

"""
import sys
from clonal_snps import simulation

length = int(sys.argv[1])
n = int(sys.argv[2])
p = float(sys.argv[3])

ancestor_dna = simulation.random_dna(length)
mutated_seqs = simulation.mutate_dna_list(ancestor_dna, p, n)
print mutated_seqs
identical_pos = simulation.find_identical_snps(mutated_seqs)
uncommon_snps = simulation.remove_identical_snps(mutated_seqs, identical_pos)
print uncommon_snps
for i in uncommon_snps:
    print ''.join(i)
