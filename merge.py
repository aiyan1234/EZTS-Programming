def mergesort(arr,low,high):
    if low<high:
        mid=(low+high)//2
        mergesort(arr,low,mid)
        mergesort(arr,mid+1,high)
        merge(arr,low,mid,high)
def merge(arr,low,mid,high):
    i=low
    j=mid+1
    k=low
    b=[0]*(high+1)
    while i<=mid and j<=high:
        if arr[i]>arr[j]:
            b[k]=arr[j]
            j=j+1
        else:
            b[k]=arr[i]
            i=i+1
        k=k+1
    while i<=mid:
        b[k]=arr[i]
        i=i+1
        k=k+1
    while j<=high:
        b[k]=arr[j]
        j=j+1
        k=k+1
    for m in range(low,high+1):
        arr[m]=b[m]
arr=[1,4,6,2,9,0,98]
mergesort(arr,0,len(arr)-1)
print(arr)

