#Find the index value from array
#a=[4,8,3,6,0,2]
#Input = a
#Output = a = 2,index = 5
#Index = 0

def count(a):
    count = 0
    while(a[count:]):
        count+=1
    return count

def Find_the_index_value(a,search_index):
    index = 0
    length_of_the_index = count(a)
    while(index!=length_of_the_index):
        if(a[index] == search_index):
            break
        index+= 1

        if(index == length_of_the_index):
            index = -1
    return index

a = [4,8,3,6,0,2]
search_index = input('Get the index value :')
print(Find_the_index_value(a,search_index))