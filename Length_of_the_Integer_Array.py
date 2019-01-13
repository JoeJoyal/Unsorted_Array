#Find the length of the Integer Array
#cCount variable assign
#a =[2,4,6,8,10]
#Input = a
#Output = 5

def length_of_Integer(a):
    count = 0
    while(a[count:]):
        count+=1
    return count
a = [2,4,6,8,10]
print(length_of_Integer(a))