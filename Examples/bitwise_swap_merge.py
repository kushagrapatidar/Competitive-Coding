def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        
        L=arr[:mid]
        R=arr[mid:]
        
        mergesort(L)
        
        mergesort(R)
        print(R)
        
        i=j=k=0
        while i<len(L) and j<len(R):

            if L[i]<R[j]:# and i!=j and arr[i]&L[j]!=0:
                arr[i]=L[i]
                i+=1
            else:
                #if i!=j and arr[i]&R[j]!=0:
                arr[k]=R[j]
                j+=1
            k+=1
        
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1

        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1

arr=[9,34,4,24,1,6]
print("Given array is\n",arr)
mergesort(arr)
print("Sorted array is:\n",arr)