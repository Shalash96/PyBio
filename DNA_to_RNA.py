def dna_to_rna(DNA_strand):
    rna_strand = ''
    for i in DNA_strand:
        if i == 'T':
            rna_strand += 'U'
        else:
            rna_strand += i

    return rna_strand


