# array is Sorted or not 

# def sortB(arr):
#     i = 0
#     for j in range(len(arr)-1):
#         if arr[j] < arr[j+1]:
#             pass
#         else:
#             return False
#     return True
# print(sortB([1,2,3,4])) 


# Bubble sorting -- asending order o(n*n)-- worst case best case O(n)
def bubble(arr):
    for i in range(len(arr)-1):
        sorting = False
        for j in range(1,len(arr)-i):
            if arr[j] < arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
                sorting =  True
        if sorting == False:
            break
    return arr
print(bubble([5,8,3,65,-43,0,12]))

# Bubble sorting -- Dsending order o(n*n)-- worst case best case O(n)
def bubble(arr):
    for i in range(len(arr)-1):
        sorting = False
        for j in range(1,len(arr)-i):
            if arr[j] > arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
                sorting =  True
        if sorting == False:
            break
    return arr
print(bubble([5,8,3,65,-43,0,12]))


