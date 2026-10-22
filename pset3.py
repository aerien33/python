# --- PROBLEM SET 3 ---
# clone repo
# run: python3 pset3.py

if __name__ == '__main__':
    print("--- 3.1: is this syntax correct? ---")
    # --- a) ---
    # x = 2;
    # y = 3;
    # if (x > y):
    #     result = x;
    # else:
    #     result = y;
    print("a) yes, although semicolons and parentheses are redundant")

    # --- b) ---
    # for i in "axby": if ord(i) < 100: print (i)'
    print("b) no, the body of the 'for' loop contains more than one command")
    print("\tenters and indents are needed after the colons")

    # --- c) ---
    # 'for i in "axby": print (ord(i) if ord(i) < 100 else i)')
    print("c) yes, in the 'for' loop there is just one complex command")

    print("--- done ---")

    # słownik tworzyć na 3 sposoby