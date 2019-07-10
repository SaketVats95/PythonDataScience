#f=open("dataWithPolicyNumber.txt",'r')
from collections import Counter
array=[]


with open("dataWithPolicyNumber.txt", "r") as ins:
    array = []
    #a=ins.replace("\n","")
    for line in ins:
        array.append(line.replace("\n",""))


#s={i:array.count(i) for i in array}

print(Counter(array))
