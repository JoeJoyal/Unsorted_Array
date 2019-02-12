#Find the Largest Number of Ntimes count
# import return_function_count (length)
# import Find the Largest Number
# Input a=[26,25,24,23,26,26]
# Output = Largest Num = 26,count = 4 

import return_fun_count
import Find_the_largest_Num_11

def Largest_count_Ntime(a,max):
    count =0
    i=0
    length = return_fun_count.count(a)

    while(i!=length):
        if(a[i]==max):
            count+=1
        i+=1
    return count

def largest_Num_occurences(a,max):
    max = Find_the_largest_Num_11.Largest_Num(a)
    counti = Largest_count_Ntime(a,max)
    return counti

a=[26,25,24,23,26,26,26]
print(largest_Num_occurences(a,max))



