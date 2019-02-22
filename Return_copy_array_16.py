#To find the Return copy array
#Assign copy_array variable
#Input array=[2,3,5,7,8]
#Output = [2,3,5,7,8]

def procedure_copy(array):
    copy_array=[]
    for i in array:
        copy_array.append(i)
    return copy_array

array=[2,3,5,7,8]
print(procedure_copy(array))