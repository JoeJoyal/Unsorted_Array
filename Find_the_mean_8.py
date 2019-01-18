#Find the mean value
#a = [12,4,6,8,14]
#Input = a
#Output = 44/5 = 8

import return_fun_sum_of_all_elements

def mean(a):
    sum1 = return_fun_sum_of_all_elements.sum_of_all_elements_1(a)
    divide = return_fun_sum_of_all_elements.count(a)
    mean = sum1/divide
    return mean

a = [12,4,6,8,14]
print(mean(a))
