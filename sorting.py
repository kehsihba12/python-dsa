# array is Sorted or not 

# def sortB(arr):
#     i = 0
#     for j in range(len(arr)-1):
#         if arr[j] < arr[j+1]:
#             pass
#         else:
#             return False
#     return True
# # print(sortB([1,2,3,4])) 


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
#         for j in range(1,len(arr)):
#             if arr[j] > arr[j-1]:
#                 arr[j],arr[j-1] = arr[j-1],arr[j]
#                 sorting =  True
#         if sorting == False:
#             break
#     return arr
# print(bubble([5,8,3,65,-43,0,12]))


# # Selection sort  best / worst / average complexity ---O(n*n) taking minimum element and put into first index
# def selection_sort(arr):
#     for i in range(len(arr)):
#         mini = i
#         for j in range(i,len(arr)):
#             if arr[j] < arr[mini]:
#                 mini = j
#         temp = arr[mini]
#         arr[mini] = arr[i]
#         arr[i] = temp
#     return arr
# print(selection_sort( [-23,0,3,-33]))

# Selection sort  best / worst / average complexity ---O(n*n) taking max element and put into last index
# def selection_sort(arr):
#     for i in range(len(arr)):
#         max = len(arr)-1-i
#         for j in range(i,len(arr)):
#             if arr[j] > arr[max]:
#                 max = j
#         temp = arr[max]
#         arr[max] = arr[i]
#         arr[i] = temp
#     return arr
# print(selection_sort( [-23,0,3,-33]))

#  insertion sort  best complexity O(n) worst avg -- O(n*n)

# def insertion_sort(arr):
#     for i in range(len(arr)):
#         j = i
#         while(j > 0 and arr[j-1] > arr[j]):
#             arr[j],arr[j-1] = arr[j-1],arr[j]
#             j -= 1
#     return arr
# print(insertion_sort([-23,0,3,-33]))

# merge sort 
# def merge(l,h):
#     if l == h:
#         return 
#     if (l < h):
#         mid = (l+h)/2
#         merge(l,mid)
#         merge(mid+1,h)
#         merge(l,mid,h)
#     return 
# arr =[4,2,5,7,8]
# print(merge(0,len(arr)))


# merge sort
def merged(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        merged(left_arr)
        merged(right_arr)
        #  merge
        i = 0
        j = 0
        k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                k += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                k += 1
        while (i < len(left_arr)):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while( j < len(right_arr)):
            arr[k] = right_arr[j]
            j += 1
            k += 1

arr = [-23,0,4,2,1,-33]
merged(arr)
print(arr)

#  quick sort 
def quickSort(arr,low,high):
    if low < high :
        pdx = partition(arr,low,high)
        quickSort(arr,low,pdx-1)
        quickSort(arr,pdx+1,high)
def partition(arr,low,high):
    pivot = len(arr)-1
    i = low-1
    for j in range(low,high):
        if arr[j] < arr[pivot]:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    i += 1
    temp = arr[i]
    arr[i] = arr[high]
    arr[high]= temp
    return i

arr = [-23,0,3,-33]
low = 0
high = len(arr)-1
quickSort(arr,low,high)
print(arr)

    