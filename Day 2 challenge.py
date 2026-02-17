Student_ID=(input("Enter Student ID:"))
Email=(input("Enter Email:"))
Password=(input("Enter Password:"))
Referral_code=(input("Enter Referral Code:"))
length=len(Email)
valid=True
if len(Student_ID)!=7 or  Student_ID.find('C')!=0 or Student_ID.find('S')!=1 or Student_ID.find('E')!=2 or Student_ID.find('-')!=3 or Student_ID[4]<'0' or Student_ID[4]>'9'or Student_ID[5]<'0' or Student_ID[5]>'9' or Student_ID[6]<'0' or Student_ID[6]>'9':
    valid=False
if Email.count('@')!=1 or Email.count('.')!=1 or Email.find('@')==0 or Email.find('@')==length-1 or Email[length-4]!='.' or Email[length-3]!='e' or Email[length-2]!='d' or Email[length-1]!='u':
    valid=False
if len(Password)<8 or Password[0]<'A' or Password[0]>'Z' or not(Password.find('0')!=-1 or Password.find('1')!=-1 or Password.find('2')!=-1 or Password.find('3')!=-1 or Password.find('4')!=-1 or Password.find('5')!=-1 or Password.find('6')!=-1 or Password.find('7')!=-1 or Password.find('8')!=-1 or Password.find('9')!=-1):
    valid=False
if len(Referral_code)!=6 or Referral_code.find('R')!=0 or Referral_code.find('E')!=1 or Referral_code.find('F')!=2 or Referral_code[3]<'0' or Referral_code[3]>'9' or Referral_code[4]<'0' or Referral_code[4]>'9' or Referral_code.find('@')!=5:
    valid=False

if valid:
    print("Approved ")
else:
    print("Rejected ")