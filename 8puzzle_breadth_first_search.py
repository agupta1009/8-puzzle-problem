# HERE WE HAVE UDES THE BFS APPROACH(BREADTH FIRST SEARCH)
import copy
# COMPARE FUNCTION I =S THERE TO COMPARE THE CURRENT STATE AND FINAL STATE
def compare(arr1,arr2):
    if arr1==arr2:
        return 1
    else:
        return 0
# SWAP FUNCTION IS CREATED TO SWAP THE EMPTY BOX OR "0"
def swap(a,b):
    return b,a

# FIND ZERO GIVES YOU THE INDICES OF THE EMPTY BOX OR "0"
def find_zero(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]==0:
                return i,j
# INITIAL STATE 
arr = [[1,2,3],
       [8,0,4],
       [7,6,5]
      ]
final_state = [[2,8,1],
               [0,4,3],
               [7,6,5]
               ]

i,j=find_zero(arr)
n=len(arr)
queue = []
visited = []
queue.append(arr)
count=0
# BFS IMPLEMENTATION
while len(queue)!=0:
    visited.append(copy.deepcopy(queue[0]))
    count+=1
    if compare(queue[0],final_state):
        print(f"Matched in {count} no. of steps")
        print("path:")
        for i in visited:
            print(i)
        break
    else:
        # SUCCESSORS ARE GENERATED 
        arr=queue.pop(0)
        i,j=find_zero(arr)
        if i-1>=0:
            arr[i][j],arr[i-1][j] = swap(arr[i][j],arr[i-1][j])
            if arr not in visited:
                # deepcopy is used because list provide refrence to the element not the value
                queue.append(copy.deepcopy(arr))
                # to go back to the original state
            arr[i][j],arr[i-1][j] = swap(arr[i][j],arr[i-1][j])
                
        if j-1>=0:
            arr[i][j],arr[i][j-1] = swap(arr[i][j],arr[i][j-1])
            # check if the successor is not visited 
            if arr not in visited:
                queue.append(copy.deepcopy(arr))
            arr[i][j],arr[i][j-1] = swap(arr[i][j],arr[i][j-1])
            
        if i+1<n:
            arr[i][j],arr[i+1][j] = swap(arr[i][j],arr[i+1][j])
            if arr not in visited:
                queue.append(copy.deepcopy(arr))
            arr[i][j],arr[i+1][j] = swap(arr[i][j],arr[i+1][j])
            
        if j+1<n:
            arr[i][j],arr[i][j+1] = swap(arr[i][j],arr[i][j+1])
            if arr not in visited:
                queue.append(copy.deepcopy(arr))
            arr[i][j],arr[i][j+1] = swap(arr[i][j],arr[i][j+1])
