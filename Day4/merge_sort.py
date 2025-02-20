import sys
array=[int(i) for i in sys.argv[1:]]
def merge_sort_array(array,low,high):
    if low<high:
        mid=(low+(high-low)//2)
        merge_sort_array(array,low,mid)
        merge_sort_array(array,mid+1,high)
        merge(array,low,mid,high)
def merge(numbers,low,mid,high):
    array1=array[low:mid+1]
    array2=array[mid+1:high+1]
    i,j=0,0
    k=low
    while i<len(array1) and j<len(array2):
        if array1[i]<array2[j]:
            array[k]=array1[i]
            i+=1
        else:
            array[k]=array2[j]
            j+=1
        k+=1
    array[k:high+1]=array1[i:]+array2[j:]
merge_sort_array(array,0,len(array))
print(array)