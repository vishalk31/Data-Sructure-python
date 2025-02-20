def binary_search(my_list,value):
    low = 0
    high = len(my_list)-1
    while low <= high:
        mid = (low+high)//2
        guess = my_list[mid]
        if guess == value:
            return(mid)
            break
        elif guess> value:
            high = mid-1
        else:
            low = mid+1
    return(None)
        
my_list = [1, 3, 5, 7, 9]
print (binary_search(my_list, 10))       
        
        
