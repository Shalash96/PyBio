def ReverseComplement(pattern):
    comp_pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    comp_strand = ''
    for i in pattern:
        comp_strand += comp_pairs[i]
    rev_comp_strand = comp_strand[::-1]
    return rev_comp_strand


print(ReverseComplement('AAAGGACATCTACGAATCCATAGGCTAAAGGTTATAGACACCTATTTTTTTTGAAAGCTTCGGGATGCTGATTAACCTGTTATCTTGTAACATTTGGGGGAAGCAACCGACCCACTTCCATCGGAGTATCTCACGAGCGTCATGTGGGTGTACCTAGGCGTCCTGTATTGCAATTAAGGATCTTGAATCGTAGACACCGTTATACCCAGAGGTTATTTTGATAAGGCAGTGTTACTTCGATCTGTTTGTGTAGATGTCCTCGAAATGAAATGTGTTCACACGTAACGAATGTAAAAGAGAGTAATGGAGTCAGAATGAAGTGACGTGAGCAAAGGACTCACGCGACGCACCTTCTTCAAGGGATCTGTCCTGTAACAAGCCCCCCGTTGCTATCGCGTTGCCTGAGTTTCATCGCCAATCACCCGCGGACTACACCGCGATGTGTAAGCCCTGATAGGTGGGTTGTTAACGGGTGCTCAGCTGGACAGCCAGTTGAGTCATACCGCCAGCAGTTGCTGCGACAGATTTGCTCGTTGATGGGCAATTTGCGTGAGCTCGAGCCCTTTAGGGACGACATGCCATGAAAGATAAAACCGACTCCCCTCAAGAACAGCTGTAGTCTTCATTATTACGAGCCAAATTACTCGGCCCTCTACCAAATGAGCGATTTTGCAACACAAGTGCCGTTGCAAATCGGCGGAACTAACGACTCCTTTTAAACCGAGGTGACTGGGACATAAGTATACTCAAGTTCGGTCTCAGATGTTCGGTCCGCGATTCACTATGATTGTCCAGATCGAATTGGTTAAGCTCGTCCTCGACTTCCCGGAATCCCGCATACTTGAAAGCCTCCCTTGTTGAAGTGCGCGTGAG'))
