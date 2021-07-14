def filter_long_words(sentence, n):
    a = sentence.split()
    print(a)
    fin = []
    for i in a:
        long = len(i)
        if long > n:
            fin.append(i)
    print(fin)
filter_long_words("sentence addav hittlet kgg", 4)