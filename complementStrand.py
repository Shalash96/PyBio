def Complement(pattern):
    comp_pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    comp_strand = ''
    for i in pattern:
        comp_strand += comp_pairs[i]
    return comp_strand


