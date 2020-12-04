file = open("list", "r")
text = file.read().split("\n")
file.close()

dict = {}


def clearing_up(text):
    file = open("list", "w")
    for i in range(len(text)):
        if text[i] == "":
            file.write("\n")
        else:
            file.write(text[i])
            file.write(" ")
    file.close()
    file = open("list", "r")
    return file.read().split("\n")

def check_text(list):
    counter = 0
    for i in range(len(list)):
        if list[i].__contains__("byr"):
            if list[i].__contains__("iyr"):
                if list[i].__contains__("eyr"):
                    if list[i].__contains__("hgt"):
                        if list[i].__contains__("hcl"):
                            if list[i].__contains__("ecl"):
                                if list[i].__contains__("pid"):
                                    counter +=1
    return counter

if __name__ == "__main__":
    sorted_text = clearing_up(text)
    print(sorted_text[0])
    print(check_text(sorted_text))
