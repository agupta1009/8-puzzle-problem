import copy
import time
start_time= time.time()
def compare(arr1,arr2):
    if arr1==arr2:
        return 1
    else:
        return 0
def swap(a,b):
    return b,a
def find_zero(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]==0:
                return i,j
                
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
while len(queue)!=0:
    count+=1
    if compare(queue[0],final_state):
        print(f"Matched in {count} no. of steps")
        print(queue[0])
        break
    else:
        visited.append(copy.deepcopy(queue[0]))
        arr=queue.pop(0)
        i,j=find_zero(arr)
        if i-1>=0:
            arr[i][j],arr[i-1][j] = swap(arr[i][j],arr[i-1][j])
            if arr not in visited:
                queue.append(copy.deepcopy(arr))
            arr[i][j],arr[i-1][j] = swap(arr[i][j],arr[i-1][j])
                
        if j-1>=0:
            arr[i][j],arr[i][j-1] = swap(arr[i][j],arr[i][j-1])
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
print(count)
print(round(time.time()-start_time,6))