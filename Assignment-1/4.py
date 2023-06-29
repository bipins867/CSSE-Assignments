def check(s):
    print('"{}" is '.format(s),end=' ')
    if s==s[::-1]:
        print("Panidrome")
    else:
        print("Not Panidrome")

if __name__=='__main__':

    s=input("Enter the String :")
    check(s)
