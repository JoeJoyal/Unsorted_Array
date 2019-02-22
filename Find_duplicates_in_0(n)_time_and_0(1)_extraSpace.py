def getlength(a):
    count = 0
    while(a[count:]):
        count+=1
    return count

def isSorted(a):
    flag = True
    length = getlength(a)

    if length == 0 or length == 1:
        return True
    i=0
    while(i!=length-1):
        if a[i] > a[i+1]:
            flag = False
        i+=1
    return flag


def removeDuplicate(a):
    i=0
    j=0
    count = 0
    length = getlength(a)-1
    while(i!=length):
        if(a[i] == a[i+1]):
            a[j] = a[i]
            count+=1
            j+=1
        i+=1
    a[j] = a[-i]
    a.append(count)
    return a



def Main(a):
    if isSorted(a):
        a = removeDuplicate(a)
    else:
        a.sort()
        a = removeDuplicate(a)
    untill = (a.pop())+1
    for i in range(0,untill):
        print(a[i])
        if i !=untill-1:
            print(",")
    return a

a=[1,2,3,1,3,6,6]
print(Main(a))