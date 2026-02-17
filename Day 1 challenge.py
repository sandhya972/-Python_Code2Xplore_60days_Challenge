full_name=(input("Enter your full name: "))
Email_ID=(input("Enter your Email ID: "))
Mobile_number=(input("Enter your mobile number: "))
Age=int(input("Enter your age: "))
length=len(full_name)
valid=True
if full_name.count(" ")<1 or full_name.find('')=="0" or full_name.find('')=="lenth-1":
    valid=False
if  Email_ID.count('@')!=1 or Email_ID.count('.')<1  or Email_ID[0]=="@":
    valid=False
if  len(Mobile_number)!=10 or Mobile_number<"0000000000" or Mobile_number>"9999999999" or  Mobile_number.find('0')==0:
    valid=False
if Age<18 and Age>60:
    valid=False

if valid:
    print("User profile is valid")
else:
    print("User profile is invalid")
