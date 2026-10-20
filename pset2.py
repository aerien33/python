# --- PROBLEM SET 2 ---
# clone repo
# run: python3 pset2.py

def test(fun, *args, expected):
    assert fun(*args) == expected

def count_words(text):
    return len(text.split())

def split_word(word):
    return '_'.join(list(word))

def first_char(word):
    return word[0]

def last_char(word):
    return word[-1]

def combine_chars(text, fun):
    return ''.join([fun(word) for word in text.split()])

def total_word_len(text):
    return len(text.replace(" ", '').replace("\t", '').replace("\n", '').strip())

def longest_word(text):
    return max(text.split(), key=len)

def longest_word_len(text):
    return max(map(lambda word: len(word), text.split()))

if __name__ == '__main__':
    line1 = '"Króliczek"\n\tRóżowy nosek,\n\tdługie uszka cicho drżą,\n\ti kic w miękki mech.\n'
    line2 = """"Piesek"
        Klapnięte uszko,
        ciepły brzuszek do miziania,
        śpi na poduszce.
    """

    print("--- Testing 2.10: count words---")
    test(count_words, line1, expected=12)
    test(count_words, line2, expected=10)

    print("--- Testing 2.11: split word---")
    test(split_word, "Bork", expected="B_o_r_k")
    test(split_word, "Woof woof", expected="W_o_o_f_ _w_o_o_f")

    print("--- Testing 2.12: combine first/last chars---")
    test(combine_chars, line1, first_char, expected='"Rnducdikwmm')
    test(combine_chars, line2, first_char, expected='"Kucbdmśnp')
    test(combine_chars, line1, last_char, expected='"y,eao,icwi.')
    test(combine_chars, line2, last_char, expected='"e,yko,ia.')

    print("--- Testing 2.13: total word length---")
    test(total_word_len, line1, expected=60)
    test(total_word_len, line2, expected=62)

    print("--- Testing 2.14: longest word and its length---")
    test(longest_word, line1, expected='"Króliczek"')
    test(longest_word, line2, expected="Klapnięte")
    test(longest_word_len, line1, expected=len(longest_word(line1)))
    test(longest_word_len, line2, expected=len(longest_word(line2)))