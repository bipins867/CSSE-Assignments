#Question1

def bmi(height,weight):
    b=weight/((height/100)**2)

    if b<=18.5:
        print("Underweight")
    elif  b<=24.9:
        print("Normal")
    elif  b<=29.9:
        print("Overweight")
    else:
        print("Obese")

if __name__=='__main__':
    
    height=float(input("Enter Height(cm):"))
    weight=float(input("Enter Weight(Kg):"))

    bmi(height,weight)
