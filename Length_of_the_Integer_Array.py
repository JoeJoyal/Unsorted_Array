#Find the length of the Integer Array
def length_of_Integer(N):
    count = 0
    while(N[count:]):
        count+=1
    return count
Array = [2,4,6,8,10]
print(length_of_Integer(Array))