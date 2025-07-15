"""
BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below

BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese

"""

print("==== BMI ====")

weight = float(input("Enter weight "))
height = float(input("Enter height "))

bmi_result = weight / (height **2)


if bmi_result <= 18.5:
    print("Underweight")
elif bmi_result >= 18.5 and bmi_result <=24.9:
    print("Normal Weight")
elif bmi_result >= 25.0 and bmi_result <=29.9:
    print("OverWeight")
else:
    print("Obese")

    
print("BMI :",bmi_result)