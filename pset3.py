# --- PROBLEM SET 3 ---
# clone repo
# run: python3 pset3.py

from functools import reduce
from itertools import count, islice, repeat, chain

def test(fun, *args, expected):
    assert fun(*args) == expected

def for_loop(data):
    result = []
    for i in range(data["start"], data["end"]):
        if data["condition"](i):
            result.append(i)
    return result

def while_loop(data):
    result = []
    i = data["start"]
    while i < data["end"]:
        if data["condition"](i):
            result.append(i)
        i = i + 1
    return result

def cube_float():
    while True:
        i = input("Insert number (type 'stop' to exit):\n")
        if i == 'stop': break
        else:
            try:
                print(f"Result: ({float(i):,g})^3 = {float(i)**3:,g}".replace(","," "))
            except ValueError:
                print("Please insert a valid number")

def draw_ruler(size):
    ruler = "|" + "".join(islice(repeat("....|"), size))
    numbers = "0" + "".join(map(lambda x: f"{x:5d}", islice(count(1), size)))
    return ruler + "\n" + numbers

def draw_grid(rows, cols):
    horizontal = "+" + "".join(repeat("---+", rows))
    vertical = "\n" + "|" + "".join(repeat("   |", rows)) + "\n"
    return horizontal + "".join(repeat(vertical + horizontal, cols))

def intersection(data1, data2):
    return sorted(set(data1).intersection(set(data2)))

def union(data1, data2):
    return sorted(set(chain(data1, data2)))

def calculate_sum(data):
    return list(map(lambda item: reduce(lambda total, x: total + x, item, 0), data))

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


    print("--- 3.3: testing 'for' vs 'while' loop ---")
    loop_data = {
        "start": 0,
        "end": 31,
        "condition": lambda x: not x % 3 == 0,
        "expected": [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29]
    }

    test(for_loop, loop_data, expected=loop_data["expected"])
    test(while_loop, loop_data, expected=loop_data["expected"])

    print("--- 3.4: test cube float (from user input) ---")
    test(cube_float, expected=None)

    print("--- 3.5: test ruler generator ---")
    ruler_data = {
        "len": 12,
        "expected": "|....|....|....|....|....|....|....|....|....|....|....|....|\n0    1    2    3    4    5    6    7    8    9   10   11   12"
    }

    print(draw_ruler(ruler_data["len"]))
    test(draw_ruler, ruler_data["len"], expected=ruler_data["expected"])

    print("--- 3.6: test grid generator ---")
    grid_data = {
        "rows": 4,
        "cols": 2,
        "expected": "+---+---+---+---+\n|   |   |   |   |\n+---+---+---+---+\n|   |   |   |   |\n+---+---+---+---+"
    }

    print(draw_grid(grid_data["rows"], grid_data["cols"]))
    test(draw_grid, grid_data["rows"], grid_data["cols"], expected=grid_data["expected"])

    print("--- 3.8: test intersection and union set ---")
    lists_data = [
        {
            "list1": [1, 2, 4, 3],
            "list2": [2, 3, 4, 6, 5],
            "exp_intersection": [2, 3, 4],
            "exp_union": [1, 2, 3, 4, 5, 6]
        },
        {
            "list1": ["b", "a", "c", "d"],
            "list2": ["b", "c", "e", "d", "f"],
            "exp_intersection": ["b", "c", "d"],
            "exp_union": ["a", "b", "c", "d", "e", "f"]
        }
    ]

    for data in lists_data:
        test(intersection, data["list1"], data["list2"], expected=data["exp_intersection"])
        test(union, data["list1"], data["list2"], expected=data["exp_union"])

    print("--- 3.9: test sum of numbers from lists or tuples ---")
    series_data = {
        "data": [[],[4],(1,2),[3,4],(5,6,7)],
        "expected": [0, 4, 3, 7, 18]
    }

    test(calculate_sum, series_data["data"], expected=series_data["expected"])

    print("--- done ---")
