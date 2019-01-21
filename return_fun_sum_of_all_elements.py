#Return function using mean value find out
#declare count fun
#declare sum_of_all_elements fun

def count(a):
    count = 0
    while(a[count:]):
        count+=1
    return count

def sum_of_all_elements_1(a):
    i = 0
    sum1 = 0
    length_of_the_array = count(a)
    while(i!=length_of_the_array):
        sum1= sum1+a[i]
        i+=1
    return sum1
