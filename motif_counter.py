def motif_counter(motif, sample):
    counter = 0
    for i in range(len(sample)):
        if sample.startswith(motif, i):
            counter += 1
    return counter


text = input('Enter DNA: \n')
pattern = input('motif: \n')

print(motif_counter(pattern, text))


