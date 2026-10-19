# ZADANIE 2.10
# Mamy dany string wielowierszowy line.
# Podać sposób obliczenia liczby wyrazów w stringu.
# Przez wyraz rozumiemy ciąg "czarnych" znaków,
# oddzielony od innych wyrazów białymi znakami (spacja, tabulacja, newline).

line = '"Króliczek"\n\tRóżowy nosek,\n\tdługie uszka cicho drżą,\n\ti kic w miękki mech.\n'
print(line)

n_words = len(line.split())
print("Liczba słów: " + str(n_words))
assert n_words == 12
