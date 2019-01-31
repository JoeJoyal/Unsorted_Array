#To find the Largest value 
#import return fun count
#declare first_num and second_num
#Input a=[20,12,15,10,5]
#Output '20'

import return_fun_count

def Largest_Num(a):
    value_count = return_fun_count.count(a)
    first_num = a[0]
    second_num = a[1]

    if(first_num>second_num):
        max = first_num
    else:
        max = second_num

    i=2
    while(i!=value_count):
        if(a[i]>max):
            max=a[i]
        i+=1
    return max

a = [20,12,15,10,5] 
print(Largest_Num(a))   