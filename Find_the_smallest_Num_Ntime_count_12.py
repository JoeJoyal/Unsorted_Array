#Find the Smallest Number of Ntimes count
# import return_function_count (length)
# import Find the smallest Number
# Input a=[1,4,6,7,3,1,1]
# Output = smallest NUm = 1,count = 3 

import return_fun_count
import Find_the_smallest_Num_10

def Smallest_count_Ntimes(a,min):
    count =0
    i=0
    length = return_fun_count.count(a)

    while(i!=length):
        if(a[i]==min):
            count+=1
        i+=1
    return count

def smallest_Num_occurences(a,min):
    min = Find_the_smallest_Num_10.smallest_Num(a)
    counti = Smallest_count_Ntimes(a,min)
    return counti

a=[1,4,6,7,3,1,1]
print(smallest_Num_occurences(a,min))



