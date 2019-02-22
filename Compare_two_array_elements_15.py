#To find the Compare two array elements
#Assign boolean function True/false
#variable index,check
#Input a1 = [2,5,6,8,0], a2 =[2,6,0,8,5]
#Output = True

import return_fun_count

def count(a):
    count = 0
    while(a[count:]):
        count+=1
    return count

def Compare_two_array_element(array1,array2):
    flag = False
    index = 0
    check = 1
    length_of_array1 = return_fun_count.count(array1)
    while(index!=length_of_array1):
        if array1[index] not in array2:
            check = 1
        index+=1

        if check ==1:
            flag = True
    return flag
    

array1=[2,5,6,8,0]
array2=[2,6,0,8,1]
print(Compare_two_array_element(array1,array2))
                
    
