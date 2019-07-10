#x=int(input("Enter the value of x:"))
#print(x&0)
def second_Smallest(data):
    s=data[0]
    sec_s=1000000000
    for i in data:
        if i<s:
            sec_s,s=s,i
        elif i<sec_s and i!=s:
            sec_s=i
    print(s)
    print(sec_s)


data=[2,2,2,10,20,3,4,5,6,90]
print(list(dict.fromkeys(data)))
data_counts={i:data.count(i) for i in data}
print(data_counts)
second_Smallest(data)

