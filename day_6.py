from collections import Counter
import time

file = open("list", "r+")
text = file.read().split("\n")

#
# Format the list file to my needs. (Every group in 1 line, people splitted with "---")
#
def clearing_up(text):
    file = open("list", "w")
    for i in range(len(text)):
        if text[i] == "":
            file.write("\n")
        else:
            file.write(text[i])
            file.write("---")
    file.close()
    file = open("list", "r")
    return file.read().split("\n")


#
# count every letter in the alphabet and set it to one if 2 people answered it with yes(1)
#
def count():
    n_text = 0

    file = open("list", "r")
    text = file.read().split("\n")

    for i in range(len(text)):
        for letter in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'):
            if text[i].count(letter) >= 1:
                n_text +=1
    file.close()
    return n_text


#
# count the answers everyone in the group answered with yes (spaces = number of people in the group)
#
def count_all():
    n_text = 0
    file = open("list", "r")
    text = file.read().split("\n")

    for i in range(len(text)):
        spaces = text[i].count("---")

        for letter in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'):
            if text[i].count(letter) == spaces:
                n_text +=1
    file.close()
    return n_text


#
# main function
#
if __name__ == "__main__":
    caution = input("Do you want to analyse the file? Please only do this the first time! (yes/no): ")
    if caution.upper() == "YES":
        text = clearing_up(text)
    else:
        print("File did not get formatted.")
    print("Star 1: ", count())
    print("Star 2: ", count_all())
