'''#bubble sort
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j+1]<arr[j]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr
arr=[2,4,5,7,8,1]
print(bubble_sort(arr))'''

'''#selection sort
def selec_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if arr[min]>arr[j]:
                min=j
        temp=arr[min]
        arr[min]=arr[i]
        arr[i]=temp
    return arr
arr=[2,4,-1,-4,6,3,89]
print(selec_sort(arr))'''

'''
#inser sort
def inser_sort(arr):
    n=len(arr)
    for i in range(1,n):
        curr=arr[i]
        j=i-1
        while j>=0 and arr[j]>curr:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=curr
    return arr 
arr=[2,9,-1,0,7,5]
print(inser_sort(arr))'''


'''
#merge sort
def mergesort(A,left,right):
    if left<right:
        mid=(left+right)//2
        mergesort(A,left,mid)
        mergesort(A,mid+1,right)
        merge(A,left,mid,right)
def merge(A,left,mid,right):
    i=left
    j=mid+1
    k=left
    l=[0]*(right+1)
    while i<=mid and j<=right:
        if A[i]<A[j]:
            l[k]=A[i]
            i=i+1
        else:
            l[k]=A[j]
            j=j+1
        k=k+1
    while i<=mid:
        l[k]=A[i]
        i=i+1
        k=k+1
    while j<=right:
        l[k]=A[j]
        j=j+1
        k=k+1
    for m in range(left,right+1):
        A[m]=l[m]
A=[3,7,2,1,9,0,0,2,1,5,3]
print("array without sorting",A)
mergesort(A,0,len(A)-1)
print("array after sorting",A)'''
'''
#merge sort in constant space
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergesort(nums,0,len(nums)-1)
        return nums

    def mergesort(self,nums,low,high):
        if low<high:
            mid=(low+high)//2
            self.mergesort(nums,low,mid)
            self.mergesort(nums,mid+1,high)
            self.merge(nums,low,mid,high)
    def merge(self,nums,low,mid,high):
        left = nums[low:mid + 1]
        right = nums[mid + 1:high + 1]
        i, j, k = 0, 0, low
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                nums[k]=left[i]
                i=i+1
            else:
                nums[k]=right[j]
                j=j+1
            k=k+1
        while i<len(left):
            nums[k]=left[i]
            i=i+1
            k=k+1
        while j<len(right):
            nums[k]=right[j]
            j=j+1
            k=k+1
        return nums
            
'''

'''
#Quick sort
def quicksort(A,low,high):
    if low<high:
        pi=partition(A,low,high)
        quicksort(A,low,pi-1)
        quicksort(A,pi+1,high)

def partition(A,low,high):
    pivot=A[low]
    i=low+1
    j=high
    while True:
        while i<=j and A[i]<= pivot:
            i=i+1
        while i<=j and A[j]>pivot:
            j=j-1
        if i<=j:
            A[i],A[j]=A[j],A[i]
        else:
            break
    A[low],A[j]=A[j],A[low]
    return j

A=[45,65,2,1,0,-345,56,78]
print("array without sorting",A)
quicksort(A,0,len(A)-1)
print("array after sorting",A)
'''

        
