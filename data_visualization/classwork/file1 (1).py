num1=int(input("enter the number 1: "))
num2=int(input("enter the number 2: "))

if(num2==0):
    print("HCF" ,num1)
else:
    while(num2!=0):
        rem=num1%num2
        num1=num2
        num2=num1 
        
    print("hcf : ",num1)    