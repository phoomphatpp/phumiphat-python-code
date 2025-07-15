"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""
# MY WAY
current = input("What is your convertion between,Thai Baht (THB) and US Dollars (USD) :")
if current == "THB":
    thb = float(input("Enter your THB "))
    converted = thb / 35.5
    print("Result :",converted)
elif current == "USD":
    usd = float(input("Enter your USD"))
    converted = usd * 35.5
    print("Result :",converted)
else:
    print("invalid input bro try again!!")


# ON THE OTHER HAND YOU CAN WRITE LIKE THIS UPLOAD MY AND BELOW IS TEACHER

# OTHER WAY
direction = input("what is your directntion (1:Thai Baht (THB)) (2:US Dollars (USD))")
amount = float(input("Amount to convertion :"))
if direction == "1":
    result = amount / 35.5
    print("Result :",result)
elif direction == "2":
    result = amount * 35.5
    print("Result :",result)
else:
    print("invalid input bro")
