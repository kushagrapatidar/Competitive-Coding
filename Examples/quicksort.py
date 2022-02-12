import random

def quick_sort(array, Lb, Ub):

    if Lb<=Ub:
        pivot = partition(array, Lb, Ub)
        print(pivot)
        quick_sort(array, Lb, pivot-1)
        quick_sort(array, pivot+1, Ub)

def partition(array, Lb, Ub):
    pivot = random.randint(Lb, Ub)
    pivot_element = array[pivot]
    # print('pivot', pivot, 'Ub', Ub, 'Lb', Lb)
    i=Lb
    j=Ub

    while i<j:
        print(i, pivot, 'i pivot')
        while array[i]<=pivot_element and i<Ub:
            i += 1

        # print(j, pivot, 'j pivot')
        while array[j]>=pivot_element and j>Lb:
            j -= 1
        
        if(i<j):
            array[i], array[j] = array[j], array[i]

    array[pivot], array[j] = array[j], array[pivot]

    return j    

array = [8, 7, 2, 1, 0, 9, 6]

quick_sort(array, 0, len(array)-1)

print(array)