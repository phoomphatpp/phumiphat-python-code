# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
# รับ input จาก user โดย format เป็น int ถ้่าไม่มีจะเป็น return ออกเป็น str
age = int(input("Enter your age: "))
# use 'and' because if user enter 20 that mean more than 0 result will child
if age >0 and age <=12:
    print(f"{age} is Child")
elif age >= 13 and age <=19:
    print(f"{age} is Teenager")
elif age >= 20 and age <=59:
    print(f"{age} is Adult")
else:
    print(f"{age} is Senior")
