import collections
Nucleotides = ["A", "C", "G", "T"]  # Adenine, Cytosine, Guanine, Thymine


def validate_seq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


def count_nuc_freq(seq):
    return dict(collections.Counter(seq))


def return_compliment(seq):
    pass


def return_rev_compliment(seq):
    tmp_seq = seq.reverse()
    return tmp_seq
