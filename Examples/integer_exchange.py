def count_min_operations():
    from random import randint

    T=int(input(''))
    for _ in range(T):
        N=int(input(''))
        arr=input('').split()
        arr=list(map(int, arr))
        count=0
        for i in range(1,N,2):
            while True:
                
                if i==N-1:
                    x=randint(1,100001)
                    
                    if x!=arr[i-1] and arr[i]==arr[i-1]:
                        arr[i]=x
                        count+=1
                        break
                    else:
                        break
                
                elif i<N-1:
                    x=randint(1,100001)
                    
                    if x!=arr[i-1] and x!=arr[i+1]:
                        if arr[i]==arr[i-1]:
                            arr[i]=x
                            count+=1
                            break
                        
                        elif arr[i]==arr[i+1]:
                            arr[i]=x
                            count+=1
                            break
                        else:
                            break
                
        print(count)