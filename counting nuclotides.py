# file = open('Vibrio_cholerae.txt', 'r')
# dna = file.read()
dna = 'CATACCGTCGCCGCTTCGGAGGGACGTACTGCATAACCGTCGGCAGCCTTTCATGAGGATATAATCGTGATGGTAAACCCCGGTAACTAAGTCATAACACTTCACCCTAGGCACGAGGGTATTCGTGGGATCGTTGTTCCAGAGTTTTTTTTCAGTGGTGCCGAAGTGGTATCAGAGCGTTGGACTTCAAGTTTGCTCCCAACGCCGTTTGCGCAAACCATACGGGGGAGGGTCAATTATGCTAATTGGATTTGTAAGGTACAGATTGTAATCCTTCAGTGCGTATCCAGACTGAACGGCCGCGGGTAAGATCCCGTTTGCCACTCAGTCTTACGTGGAAATGTCGTTGATCCCGGTGTGCTTCACTTAACCATATGTGCCCTCATTTTCCTACATTTACATGGACGTCGAGTTACGCAGATGAAAGAATGAGCTCGAAAAATCCGAGCATGAGCTAGAATGCGCCTATATACGCGGTTTGCAATTCGTGCAGCCCGGGATCTGACGCACGGTACACTAACAGATTCTTAATAGGGAGGAAATAGAGCGTCACAGTTTGTACGGGCAGGATCCAGGTTCGTTTTATATGTCGGTTACTGTGGATTCGCCGCCCCTCGCTGGTAACATGGCCCGCTCTATTCATAGTAGCATCAGCCATGACGCTTACCCGTAAACGGAACCATCTTCCGCGCGAGACCGCGTGAGACATACGACCATGCTAGCGACAGCAATGGCGGGGCGGCCTACTTAGTGAGAGACGGAACTTCCGGACTACGCGGTCCGATGAGAGAACTTCACCTGCAAAGACTGCGATCCCTGCATTGAGCTGCCTCAAGCGCTCGGTAAAGACACAGTCTTAGCGCGCGACTTATTTTTAGAGAGACTTACGGCTACAATTCACGGCGCGAGAGCGTGCAACTAGAAACCTCAGGAATTCTTAGGAAACAGCCC'

# Print the original DNA string
print ("DNA length: ", len(dna))

# Print the count of each letter
print ("Count of A: ", dna.count("A"))
print ("Count of C: ", dna.count("C"))
print ("Count of G: ", dna.count("G"))
print ("Count of T: ", dna.count("T"))