#To find out smallest value
#import the return fun count
#declare first_num and second_num
#input a =[5,12,7,3]
#Output '5'

import return_fun_count

def smallest_Num(a):
  value_count =return_fun_count.count(a)    
  first_num = a[0]        
  Second_num = a[1]

  if(first_num<Second_num):
      min = first_num
  else:
      min = Second_num

  i=2
  while(i!=value_count):
      if(a[i]<min):
          min=a[i]
      i+=1
  return min

a=[5,12,7,13,9]
print(smallest_Num(a))