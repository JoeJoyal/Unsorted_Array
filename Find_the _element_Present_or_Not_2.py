#Find the element weather, present or Not
#Using flag True/False
#Search_element declare
#a = [4,9,6,2,0]
#Input = array
#Output = 4 True 

def Find_the_element(a,Search_element):
    for i in a:
        flag = False
        if(i==Search_element):
            flag = True
            break
    return flag

a = [4,9,6,2,0]
Search_element = input('Enter the search element :')
print(Find_the_element(a,Search_element))