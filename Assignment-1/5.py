from collections import Counter

def print_max(st):
    cx=Counter(st)
    mx=-1
    vl=-1

    for i in cx:
        val=cx[i]
        if val>mx:
            mx=val
            vl=i
    print("Maximum frequency character is '{}' - {} times".format(vl,mx))


if __name__=='__main__':
    s=input("Enter the String :")
    print_max(s)
