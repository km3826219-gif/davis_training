def calculatesi(p,r,t):
    return ((p*r*t)/100)

principal=float(input("enter the principal :"))
rate=float(input("enter the rate :(in%)"))
time=int(input("enter time (in years):"))

print("simple interest : as ", calculatesi(principal,rate,time))