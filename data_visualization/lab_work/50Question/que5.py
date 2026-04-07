
def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))
result = simple_interest(principal, rate, time)
print("Simple Interest =", result)