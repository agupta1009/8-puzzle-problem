# simple hill climbing
import copy
# COMPARE FUNCTION IS THERE TO COMPARE THE CURRENT STATE AND FINAL STATE
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
# WE HAVE CALCULATED HEURESTIC VALUE IN REGARDS TO THE THE NO. OF TILES MISMATCHED
def heurestic(arr,final):
    count=0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != final[i][j] and arr[i] != 0:
                count+=1
    return count
# INITIAL STATE
arr = [[2,8,3],
       [1,5,4],
       [7,6,0]
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
    # HERE WE HAVE CLEAR THE QUEUE BECAUSE IN SIMPLE G=HILL CLIMBING THE SUCCESSOR HAVING THE LEAST HEURESTIC VALUE IS ONLY TAKEN INTO CONSIDERATION
    queue.clear()
    count+=1
    visited.append(copy.deepcopy(arr))
    if compare(arr,final_state):
        # GOAL STATE REACHED
        print(f"Matched in {count} no. of steps")
        for x in visited:
            for y in x:
                print(y)
        print("\n")
        break
    else:
        # GENERATING SUCCESSORS
        i,j=find_zero(arr)
        if i-1>=0:
            arr[i][j],arr[i-1][j] = swap(arr[i][j],arr[i-1][j])
            if arr not in visited:
                # CALCULATING THE COST THAT IS HEURESTIC VALUE FOR EACH SUCCESSOR
                cost=heurestic(arr,final_state)
# deepcopy is used because list provide refrence to the element not the value
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
            # SORTING THE QUEUE BASED ON HEURESTIC VALUE IN INCREASING ORDER SINCE WE HAVE TAKEN NO. OF MISMATCHED TILES
        queue.sort(key = lambda x: x[1])
        # IF THE HEURESTIC VALUE OF SUCCESSOR IS MORE THAN THE CURRENT STATE THEREFORE WE CANNOT MOVE FORWARD SO THE CURRENT STATE IS THE BEST STATE REACHED
        # THATS WHY WE HAVE USED THIS PIECE OF CODE HERE
        if queue[0][1]>heurestic(arr,final_state):
            print(f"best state reached is :{arr}")
            break
