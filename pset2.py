# --- PROBLEM SET 2 ---
# clone repo
# run: python3 pset2.py

def count_words(text):
    return len(text.split())

def test_count_words(text, expected):
    print("Dane wejściowe: \n" + text)
    print("Liczba słów: " + str(count_words(text)))
    assert count_words(text) == expected

if __name__ == '__main__':
    line = '"Króliczek"\n\tRóżowy nosek,\n\tdługie uszka cicho drżą,\n\ti kic w miękki mech.\n'

    print("--- Test 2.10: count words---")
    test_count_words(line, 12)
