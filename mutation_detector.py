def counting_mutations(s, t):
    num = 0
    for x, y in zip(s, t):
        if x != y:
            num += 1
    return num

