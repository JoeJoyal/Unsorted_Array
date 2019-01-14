#Found the more than onces values occurs
#declare temp var assign
#Using flag True/False
#a = [14,5,5,9,21,21,13]
#Input = a
#Output = 5,21 = True

def count(a):
    count = 0
    while(a[count:]):
        count+=1
    return count

def found_more_than_onces(a,search_element):
    flag = False
    i = 0
    temp = count(a)
    counti = 0
    while(i!=temp):
        if(a[i] == search_element):
            counti+=1
        i+=1

        if(counti == 2):
            flag = True
    return flag

a = [14,5,5,9,21,21,13]
search_element = input("More than one values occurs :")
print(found_more_than_onces(a,search_element))
