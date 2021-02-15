from DNAToolkit import *
import random

rndDNAstr = ''.join([random.choice(Nucleotides)
                     for nuc in range(20)])

print(validate_seq(rndDNAstr))
print(count_nuc_freq(validate_seq(rndDNAstr)))
