#Find the No.of counts in the array
#temp var assign
#a= [14,8,5,8,9,3,7,3,3]
#Input = a
#Output = 8 return count two 2 times

def count(a):
    count = 0
    while(a[count:]):
        count+=1
    return count

def Count_the_No_of_times(a,search_elements):
    i = 0
    temp = count(a)
    counti = 0
    while(i!=temp):
        if(a[i] == search_elements):
            counti+=1
        i+=1
    return counti

a = [14,8,5,8,9,3,7,3,3]
search_elements = input("No.of times count occurs :")
print(Count_the_No_of_times(a,search_elements))



