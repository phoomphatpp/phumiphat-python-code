"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""
print("=== PERSONAL INFORMATION VALIDATOR ===")
user_name = input("Enter your name: ")
user_age  = input("Enter your age: ")
user_phone_number = input("Enter your phone number: ")
nameFlag = ageFlag = phone_number_flag = True
# user_phone_number = "348934834"
for char in user_name:
    if char.isalpha() or char == " " or char.isdigit():
        nameFlag = True
    else:
        nameFlag = False
        break
        
# print("user_name",nameFlag)
if 18 <= int(user_age) <= 65:
    ageFlag = True
else:
    ageFlag = False
# print("user_age",ageFlag)
if len(user_phone_number) != 10:
    phone_number_flag = False
else:
    for phone_char in user_phone_number:
        # if phone_char.isdigit():
        #     phone_number_flag = True
        #     # break
        if phone_char.isdigit() == False:
            phone_number_flag = False
            break
print()
print("Validation Results:")
if nameFlag:
    print("Name: Valid (contains only letters and spaces)")
else:
    print("Name: Invalid (not contains only letters and spaces)")
if ageFlag:
    print(f"Age: Valid ({user_age} years old)")
else:
    print("Age: Invalid")
if phone_number_flag:
    print("Phone: Valid (10-digit number)")
else:
    print("Phone: Invalid (not 10-digit number)")
print()
print("Formatted Information:")
print(f"Name: {user_name.upper()}")
if 18 <= int(user_age) <= 30:
    print("Age Group: Young Adult (18-30)")
else:
    print("you are younger or older")
print(f"Phone: +66-{user_phone_number}")
