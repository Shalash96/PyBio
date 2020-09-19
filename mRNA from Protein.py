""""Calculate only the number of possibilities that the protein could have benn translated from"""""

freq = {
    'A': 4, 'C': 2, 'D': 2, 'E': 2,
    'F': 2, 'G': 4, 'H': 2, 'I': 3,
    'K': 2, 'L': 6, 'M': 1, 'N': 2,
    'P': 4, 'Q': 2, 'R': 6, 'S': 6,
    'T': 4, 'V': 4, 'W': 1, 'Y': 2,
    'STOP': 3
}


def num_of_possibilities(protein):
    number = 1
    for i in protein:
        number *= freq[i]                # we multiply with the freq value of each amino acid

    return number*3 % 1000000            # we then multiply by 3 for freq of stop codon, then we take modulus of million


