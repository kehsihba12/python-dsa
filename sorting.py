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
# def bubble(arr):
#     for i in range(len(arr)-1):
#         sorting = False
#         for j in range(1,len(arr)-i):
#             if arr[j] < arr[j-1]:
#                 arr[j],arr[j-1] = arr[j-1],arr[j]
#                 sorting =  True
#         if sorting == False:
#             break
#     return arr
# print(bubble([5,8,3,65,-43,0,12]))

# # Bubble sorting -- Dsending order o(n*n)-- worst case best case O(n)
# def bubble(arr):
#     for i in range(len(arr)-1):
#         sorting = False
#         for j in range(1,len(arr)-i):
#             if arr[j] > arr[j-1]:
#                 arr[j],arr[j-1] = arr[j-1],arr[j]
#                 sorting =  True
#         if sorting == False:
#             break
#     return arr
# print(bubble([5,8,3,65,-43,0,12]))


# Selection sort  best / worst / average complexity ---O(n*n) taking minimum element and put into first index
def selection_sort(arr):
    for i in range(len(arr)):
        mini = i
        for j in range(i,len(arr)):
            if arr[j] < arr[mini]:
                mini = j
        temp = arr[mini]
        arr[mini] = arr[i]
        arr[i] = temp
    return arr
print(selection_sort( [-23,0,3,-33]))

# Selection sort  best / worst / average complexity ---O(n*n) taking max element and put into last index
def selection_sort(arr):
    for i in range(len(arr)):
        max = len(arr)-1-i
        for j in range(i,len(arr)):
            if arr[j] > arr[max]:
                max = j
        temp = arr[max]
        arr[max] = arr[i]
        arr[i] = temp
    return arr
print(selection_sort( [-23,0,3,-33]))

