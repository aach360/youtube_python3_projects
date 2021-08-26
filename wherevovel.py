# give the indexes of all vovels in a string
def vowel_indices(word):
    fin = []
    out = 1
    v = "AEIOUYaeiouy"
    for x in word:
        if x in v:
            fin.append(out)
        out += 1
    return fin