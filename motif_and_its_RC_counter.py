def motif_and_its_rev_comp_counter(motif, sample):
    counter_of_motif = 0
    counter_of_res_comp_motif = 0
    for i in range(len(sample)):
        if sample.startswith(motif, i):
            counter_of_motif += 1

    comp_pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    rev_comp_of_motif = ''
    for i in motif:
        rev_comp_of_motif += comp_pairs[i]
    rev_comp_of_motif = rev_comp_of_motif[::-1]

    for i in range(len(sample)):
        if sample.startswith(rev_comp_of_motif, i):
            counter_of_res_comp_motif += 1

    total_count = counter_of_motif + counter_of_res_comp_motif
    return f'The total count of the motif and its reverse complement is {total_count}\n' \
           f'{counter_of_motif} for the motif, which is {motif}\n' \
           f'{counter_of_res_comp_motif} for its reverse complement, which is {rev_comp_of_motif}'


# print(motif_and_its_rev_comp_counter('GGTGGTAGG', 'AACTCTATACCTCCTTTTTGTCGAATTTGTGTGATTTATAGAGAAAATCTTATTAACTGAAACTAAAATGGTAGGTTTGGTGGTAGGTTTTGTGTACATTTTGTAGTATCTGATTTTTAATTACATACCGTATATTGTATTAAATTGACGAACAATTGCATGGAATTGAATATATGCAAAACAAACCTACCACCAAACTCTGTATTGACCATTTTAGGACAACTTCAGGGTGGTAGGTTTCTGAAGCTCTCATCAATAGACTATTTTAGTCTTTACAAACAATATTACCGTTCAGATTCAAGATTCTACAACGCTGTTTTAATGGGCGTTGCAGAAAACTTACCACCTAAAATCCAGTATCCAAGCCGATTTCAGAGAAACCTACCACTTACCTACCACTTACCTACCACCCGGGTGGTAAGTTGCAGACATTATTAAAAACCTCATCAGAAGCTTGTTCAAAAATTTCAATACTCGAAACCTACCACCTGCGTCCCCTATTATTTACTACTACTAATAATAGCAGTATAATTGATCTGA'))

