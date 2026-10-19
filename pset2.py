# --- PROBLEM SET 2 ---
# clone repo
# run: python3 pset2.py

def count_words(text):
    return len(text.split())

def split_word(word):
    return '_'.join(list(word))

def test(fun, text, expected):
    assert fun(text) == expected

if __name__ == '__main__':
    line1 = '"Króliczek"\n\tRóżowy nosek,\n\tdługie uszka cicho drżą,\n\ti kic w miękki mech.\n'
    line2 = """"Piesek"
        Klapnięte uszko,
        ciepły brzuszek do miziania,
        śpi na poduszce.
    """

    print("--- Testing 2.10: count words---")
    test(count_words, line1, 12)
    test(count_words, line2, 10)

    print("--- Testing 2.11: split word---")
    test(split_word, "Bork", "B_o_r_k")
    test(split_word, "Woof woof", "W_o_o_f_ _w_o_o_f")
