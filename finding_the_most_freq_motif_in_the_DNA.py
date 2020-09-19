

def frequency_map(DNA_starnd, k):

    motifs = {}
    for i in range(0,len(DNA_starnd)):
        motif_frq = DNA_starnd[i: i+k]
        if len(motif_frq) == k:
            if motif_frq in motifs:
                motifs[motif_frq] += 1

            else:
                motifs[motif_frq] = 1

    most_repeated_motifs = []
    there_is_a_motif_that_occur_more_than_one = False
    for key, val in motifs.items():
        if max(motifs.values()) != 1:
            if val == max(motifs.values()):
                most_repeated_motifs.append(key)
                there_is_a_motif_that_occur_more_than_one = True
    if there_is_a_motif_that_occur_more_than_one:
        # return most_repeated_motifs
        print(f'The most repeated {k}-mer motif is\\are', most_repeated_motifs, 'by occurrence equal to', max(motifs.values()))
    else:
        print(f'THERE IS NO MOTIF OF THAT OCCURS MORE THAN ONE TIME ALL MOTIFS OF LENGTH {k}-mer ARE UNIQUE')


# file = open('Vibrio_cholerae.txt', 'r')
# dna = file.read()

frequency_map('ACAACTATGCATACTATCGGGAACTATCCT', 5)
