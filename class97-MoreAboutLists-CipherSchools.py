# generate lists with range functions
# something more about pop method 
# index method 
# pass list to a function 


#numbers = list(range(1,11))    
numbers = [1,2,3,4,5,6,7,8,9,10,1]
print(numbers)

# pop method 
# popped_item = numbers.pop()
# print(numbers)

# # index method 
# print(numbers.index(1,3))

# print(numbers.index(1,11,14))


#pass list to a function 
def negative_list(l):
    negative=[]
    for i in l :
        negative.append(-i)
    return negative

print(negative_list(numbers))        
     