#To find out the Return array in reverse order
#Assign the empty Reversed_array =[]
#Input array=[2,3,5,7,8]
#Output = [8,7,5,3,2]

import return_fun_count

def count(array):
    count = 0
    while(array[count:]):
        count+=1
    return count

def Return_array_in_reverse_order(array):
    Reversed_array=[]
    iterated = 1
    length_of_array = return_fun_count.count(array)
    while(iterated!=length_of_array):
        Reversed_array.append(array[-iterated])
        iterated+=1
    Reversed_array.append(array[0])
    return Reversed_array

array=[2,3,5,7,8]
print(Return_array_in_reverse_order(array))
