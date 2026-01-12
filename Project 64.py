def printPowerset(s, stringsize):
    str_size = 2 ** stringsize
    for outer in range(str_size):
        string = []
        for inner in range(stringsize):
            if outer & (1 << inner) > 0:
                string.append(s[inner])
                print(string)
string = []
s = "Done"
stringsize = len(s)
printPowerset(s , stringsize)