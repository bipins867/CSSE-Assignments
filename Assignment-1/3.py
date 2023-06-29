def print_largest(arr,n):
    arr.sort(reverse=True)

    if n>=len(arr):
        print("Invalid Input Length")
    else:
        print("The {} largest number is :".format(n),end=' ')
        print(arr[n-1])


if __name__=='__main__':

    arr=list(map(int,input("Enter the array :").split()))
    print(arr)
    n=int(input("Enter the Number :"))

    print_largest(arr,n)
