import threading
#import getAllPossibleString


def getListOfAllChars(startASCII, endingASCII):
    listChars = [chr(i) for i in range(startASCII, endingASCII + 1)]
    return listChars


def printAllKLength(set, k,s):
    n = len(set)
    printAllKLengthRec(set, "", n, k,s)


# The main recursive method
# to print all possible
# strings of length k
def printAllKLengthRec(set, prefix, n, k,s):
    if (k == 0):
        print(prefix)
        f = open("C:\\Saket Vats\\PythonDS\\allPossible"+str(s)+'.txt', 'a+')
        f.write(prefix+',')
        f.close()
        return


    for i in range(n):

        newPrefix = prefix + set[i]
        printAllKLengthRec(set, newPrefix, n, k - 1,s)

if __name__ == "__main__":
    startingStrLength = 8
    endingStrLength = 10

    jobs = []
    for i in range(startingStrLength, endingStrLength + 1):
        thread = threading.Thread(target=printAllKLength, args=(getListOfAllChars(97, 122), i,i,))
        jobs.append(thread)
        # print("All ",i," String Completed")
        # f.close()

    for i in jobs:
        i.start()
    for i in jobs:
        i.join()

    print("All Length All Possible String Completed")


