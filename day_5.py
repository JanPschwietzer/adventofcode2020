from collections import Counter

file = open("list", "r")
text = file.read().split("\n")

rows = []
seats = []

def sort():
    loesung = 0

    for i in range(len(text)):
        g = 0
        upper = 127
        lower = 0
        middle = 63

        seat_u = 7
        seat_l = 0
        seat_m = 3

        for g in range(0, 10):
            if g <= 6:
                if text[i][g] == "F":
                    upper = middle
                    middle = upper + lower
                    middle = middle // 2
                elif text[i][g] == "B":
                    lower = middle + 1
                    middle = upper + lower
                    middle = middle // 2
                g += 1

            elif g >= 7 and g <= 10:
                if text[i][g] == "L":
                    seat_u = seat_m
                    seat_m = seat_u + seat_l
                    seat_m = seat_m  // 2
                elif text[i][g] == "R":
                    seat_l = seat_m + 1
                    seat_m = seat_u + seat_l
                    seat_m = seat_m  // 2
                g += 1
        rows.append(middle)
        seats.append(seat_m)
        
        ergebnis = middle * 8 + seat_m
        if ergebnis >= loesung:
            loesung = ergebnis

    return loesung

def row_checker():
    row_check = Counter(rows)
    for key in row_check.keys():
        if row_check[key] == 7:
            print("Row: {} has {} seats.".format(key, row_check[key]))
            result = key
    return result

def seat_checker(eigb):
    result = []
    for i in range(len(rows)):
        if rows[i] == eigb:
            result.append(seats[i])
    if 0 not in result:
        print(0)
        return 0
    if 1 not in result:
        print(1)
        return 1
    if 2 not in result:
        print(2)
        return 2
    if 3 not in result:
        print(3)
        return 3
    if 4 not in result:
        print(4)
        return 4
    if 5 not in result:
        print(5)
        return 5
    if 6 not in result:
        print(6)
        return 6
    if 7 not in result:
        print(7)
        return 7
    

def calc():
    return row_checker() * 8 + seat_checker(row_checker())
            


if __name__ == "__main__":
    print(sort())
    print(calc())
