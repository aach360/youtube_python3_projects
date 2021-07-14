def get_count(input_str):
    num_vowels = 0
    for x in input_str:
        if x == "a":
            num_vowels += 1
        elif x == "e":
            num_vowels += 1
        elif x == "i":
            num_vowels += 1
        elif x == "o":
            num_vowels += 1
        elif x == "u":
            num_vowels += 1
    
    return num_vowels