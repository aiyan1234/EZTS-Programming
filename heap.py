import heapq
arr=[12,34,1,2,56]
'''heapq.heapify(arr)
print(arr)
heapq._heapify_max(arr)
print(arr)'''

#heapsort
res=[]
heapq.heapify(arr)
while arr:
    res.append(heapq.heappop(arr))
print(res)
