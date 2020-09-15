# best first search
import copy
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
def heurestic(arr,final):
    count=0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != final[i][j] and arr[i] != 0:
                count+=1
    return count
arr = [[2,0,3],
       [1,8,4],
       [7,6,5]
      ]
final_state = [[1,2,3],
               [8,0,4],
               [7,6,5]
               ]

i,j=find_zero(arr)
cost=heurestic(arr,final_state)
n=len(arr)
queue = []
visited = []
queue.append((arr,cost))
count=0
while len(queue)!=0:
    arr=queue.pop(0)
    arr=arr[0]
    count+=1
    if compare(arr,final_state):
        visited.append(copy.deepcopy(arr))
        print(f"Matched in {count} no. of steps")
        for x in visited:
            for y in x:
                print(y)
            print("\n")
        break
    else:
        visited.append(copy.deepcopy(arr))
        i,j=find_zero(arr)
        if i-1>=0:
            arr[i][j],arr[i-1][j] = swap(arr[i][j],arr[i-1][j])
            if arr not in visited:
                cost=heurestic(arr,final_state)
                queue.append((copy.deepcopy(arr),cost))
            arr[i][j],arr[i-1][j] = swap(arr[i][j],arr[i-1][j])
                
        if j-1>=0:
            arr[i][j],arr[i][j-1] = swap(arr[i][j],arr[i][j-1])
            if arr not in visited:
                cost=heurestic(arr,final_state)
                queue.append((copy.deepcopy(arr),cost))
            arr[i][j],arr[i][j-1] = swap(arr[i][j],arr[i][j-1])
            
        if i+1<n:
            arr[i][j],arr[i+1][j] = swap(arr[i][j],arr[i+1][j])
            if arr not in visited:
                cost=heurestic(arr,final_state)
                queue.append((copy.deepcopy(arr),cost))
            arr[i][j],arr[i+1][j] = swap(arr[i][j],arr[i+1][j])
            
        if j+1<n:
            arr[i][j],arr[i][j+1] = swap(arr[i][j],arr[i][j+1])
            if arr not in visited:
                cost=heurestic(arr,final_state)
                queue.append((copy.deepcopy(arr),cost))
            arr[i][j],arr[i][j+1] = swap(arr[i][j],arr[i][j+1])
        queue.sort(key = lambda x: x[1])
        
