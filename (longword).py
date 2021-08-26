#extract any words larger than a specific value and return them.
def filter_long_words(sentence, n):
    a = sentence.split()
    fin = []
    for i in a:
        long = len(i)
        if long > n:
            fin.append(i)
    return fin