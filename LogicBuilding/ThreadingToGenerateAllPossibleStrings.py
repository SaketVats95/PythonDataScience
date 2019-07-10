import threading
#import getAllPossibleString


def getListOfAllChars(startASCII, endingASCII):
    listChars = [chr(i) for i in range(startASCII, endingASCII + 1)]
    return listChars


def printAllKLength(set, k,s):
    n = len(set)
    printAllKLengthRec(set, "", n, k,s)


def printAllKLengthRec(set, prefix, n, k,s):
    if (k == 0):
        print(prefix)
        f = open("C:\\Saket Vats\\PythonDS\\allPossible"+str(s)+'.txt', 'a+')
        f.write(prefix+'\n')
        f.close()
        return


    for i in range(n):

        newPrefix = prefix + set[i]
        printAllKLengthRec(set, newPrefix, n, k - 1,s)

if __name__ == "__main__":
    startingStrLength = 8
    endingStrLength = 20
    jobs = []
    for i in range(startingStrLength, endingStrLength + 1):
        thread = threading.Thread(target=printAllKLength, args=(getListOfAllChars(33,122), i,i,))
        jobs.append(thread)

    for i in jobs:
        i.start()
    for i in jobs:
        i.join()
    print(getListOfAllChars(33, 122))
    print("All Length All Possible String Completed")


