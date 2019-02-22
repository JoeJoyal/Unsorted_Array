

import return_fun_count
def count(array):
    count = 0
    while(array[count:]):
        count+=1
    return count

def Reverse_Unsorted_element(array):
    iterated = 1
    length_of_array = return_fun_count.count(array)
    while(iterated!=length_of_array):
        print(array[-iterated])
        iterated+=1
    print(array[0])

array=[2,3,5,7,8]
print(Reverse_Unsorted_element(array))