n=int(input("Enter the number of students:"))
marks=[]
count_valid=0
count_failed=0
name="sandhya"
for i in range(n):
    m=int(input("Enter marks:"))
    marks.append(m)
for m in marks:
    if m>=90 and m<=100 :
        print(m ,"->Excellent")
        count_valid = count_valid + 1
    elif m>=75 and m<=89 and name=="sandhya":
        print(m,"->Very Good(personalized)")
        count_valid = count_valid + 1
    elif m>=60 and m<=74:
        print(m,"->Good")
        count_valid = count_valid + 1
    elif m>=40 and m<=59:
        print(m,"->Average")
        count_valid = count_valid + 1
    elif m>=0 and m<=39:
        print(m,"->Fail")
        count_valid = count_valid + 1
        count_failed = count_failed + 1
    else:
        print(m,"->Invalid")
print("Total valid Students:",count_valid)
print("Total failed Students:",count_failed)