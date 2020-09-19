def motif_finder(motif, dna):
    position = []
    for i in range(len(dna)):
        if dna.startswith(motif, i):
            position.append(i+1)

    for i in position:
        print(i, end=' ')


dna = input('dna: \n')
motif = input('motif: \n')

motif_finder(motif=motif, dna=dna)