#Find the sum of all the elements in a array
#a = [6,4,9,1,23,2,15]
#Input = a
#Output = 60

def count(a):
    count = 0
    while(a[count:]):
        count+=1
    return count

def sum_of_all_elements(a):
    i = 0
    sum1 = 0
    length_of_the_array = count(a)
    while(i!=length_of_the_array):
        sum1 = sum1+a[i]
        i+=1
    return sum1

a =[6,4,9,1,23,2,15]
print(sum_of_all_elements(a))