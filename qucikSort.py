def quicksort(arr,left,right):
    if left<right:
        pi=partition(arr,left,right)
        quicksort(arr,left,pi-1)
        quicksort(arr,pi+1,right)
def partition(arr,left,right):
    pivot=arr[left]
    i=left+1
    j=right
    while True:
        while i<=j and arr[i]<=pivot:
            i=i+1
        while i<=j and arr[j]>pivot:
            j=j-1
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
    arr[left],arr[j]=arr[j],arr[left]
    return j
arr=[3,2,71,3,2,-2,0]
quicksort(arr,0,len(arr)-1)
print(arr)
        

