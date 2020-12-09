with open("list", "r") as file:
    text = file.read().split("\n")

global_counter = 0
global_sum = 0


# Star 1:
# This function checks if the actual line can be sumed up with 2 numbers in the range of 25 lines before the line  
#
def star1(text):
    loop = True
    counter = 25
    i = 0
    g = 0
    while loop:
        if int(text[i]) + int(text[g]) == int(text[counter]): # line can be sumed up, go to the next line
            counter += 1
            i = counter - 25
            g = counter - 25
        elif int(text[i]) + int(text[g]) != int(text[counter]) and i >= counter - 1 and g >= counter - 1: # line can not be sumed up, return line
            loop = False
            return int(text[counter]), counter

        if g == counter:
            g = counter - 25
            i += 1
        else:
            g += 1
            if g == i:
                g += 1


# Star 2:
# In this funtion we put all numbers in a list that are needed to sum up our result from star 1 
#
def star2(text):
    loop = True
    g = 0
    i = 0
    sum = 0
    list = []
    g_sum = global_sum
    g_c = global_counter

    while loop:
        sum += int(text[g])

        if sum == g_sum: # if we found the right contiguous numbers!
            loop = False
            return min(list) + max(list)

        elif sum < g_sum and g < g_c: # add the next number if our sum is smaller than the star 1 result
            list.append(int(text[g]))
            g += 1
        elif sum > g_sum and g < g_c: # reset if our sum is bigger than the star 1 result
            i += 1
            g = i
            sum = 0
            list.clear()
        else: # for the case we have an error
            loop = False




if __name__ == "__main__":
    global_sum = star1(text)[0]
    global_counter = star1(text)[1]

    print("Star 1: ", global_sum)
    print("Star 2: ", star2(text))
