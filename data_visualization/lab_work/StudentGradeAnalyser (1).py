def calculate_marks(marks):
    if(marks>=90):
        print("Grade of student is A")
    elif(marks>=75 and  marks<=89):
        print("Grade of student is B")
    elif(marks>=50 and marks<75):
        print("Grade if student is B")
    else:
        print("Fail")
        
marks=int (input("enter the marks of student :"))
calculate_marks(marks)                    