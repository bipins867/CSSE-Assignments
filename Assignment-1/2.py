# Quest2
def check_prime(n):

    cond=True
    if n==0 or n==1:
        return False

    for i in range(2,n//2+1):
        if n%i==0:
            cond=False
            break
    return cond

if __name__=='__main__':
    for i in range(1000):
        if check_prime(i):
            print(i,end=' ')
