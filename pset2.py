# --- PROBLEM SET 2 ---
# clone repo
# run: python3 pset2.py

def count_words(text):
    return len(text.split())

def split_word(word):
    return '_'.join(list(word))

def test_count_words(text, expected):
    print("Dane wejściowe:\n" + text)
    print("Liczba słów: " + str(count_words(text)))
    assert count_words(text) == expected

if __name__ == '__main__':
    line1 = '"Króliczek"\n\tRóżowy nosek,\n\tdługie uszka cicho drżą,\n\ti kic w miękki mech.\n'
    line2 = """"Piesek"
        Klapnięte uszko,
        ciepły brzuszek do miziania,
        śpi na poduszce.
    """

    print("--- Test 2.10: count words---")
    test_count_words(line1, 12)
    test_count_words(line2, 10)

    print("--- Test 2.11: split word---")
    print(split_word("Bork"))
    print(split_word("Woof woof"))
