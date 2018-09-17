def count_vowels(txt):
    if not isinstance(txt, str):
        raise TypeError('invalid input')

    vowels = 'aeiou'
    newtxt = txt.lower()
    noduplicates = set(newtxt)
    duplicates = len(newtxt)-len(noduplicates)
    vowel_string = ""

    for i in vowels:
        if i in noduplicates:
            vowel_string += str(i)

    return (vowel_string, duplicates)


if __name__ == "__main__":

    print(count_vowels('acirebai'))