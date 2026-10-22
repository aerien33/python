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


    print("--- 3.2: what is wrong in this code? ---")
    # --- a) ---
    # L = [3, 5, 4] ; L = L.sort()
    print("a) it compiles, but function 'sort' doesn\'t return anything")

    # --- b) ---
    # x, y = 1, 2, 3
    print("b) mismatch between the number of variables and assigned values")

    # --- c) ---
    # X = 1, 2, 3 ; X[1] = 4
    print("c) it is not possible to assign items to a 'tuple' object")

    # --- d) ---
    # X = [1, 2, 3] ; X[3] = 4
    print("d) list assignment index out of range")

    # --- e) ---
    # X = "abc" ; X.append("d")
    print("e) 'str' object does has no attribute 'append'")

    # --- f) ---
    # L = list(map(pow, range(8)))
    print("f) 'pow' function missing required argument 'exp'")


    print("--- done ---")
