def count_even(array,l,r):
    n =len(array)
    sum=0
    for i in range(l,r+1):
        if array[i] %2==0:
            sum+=1
    return sum
array = list(map(int,input("ENTER THE ARRAY ELEMENTS: ").split()))
ranges= list(map(int,input("Enter the queries(left right): ").split()))
print(count_even(array,ranges[0],ranges[1]))
