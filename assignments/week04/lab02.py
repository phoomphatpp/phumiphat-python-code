
"""
Number List Operations

Ask user to input 10 numbers and store them in a list
Display the original list

Create and display:

List of even numbers
List of odd numbers
List of numbers greater than the average


Show statistics: sum, average, min, max

"""

def number_operations():
    numbers = []
    print("Enter 10 numbers:")
    for i in range(10):
        value = int(input(f"Enter Number {i+1}: "))
        numbers.append(value)
       
    # Display original list
    print(f"Original numbers: {numbers}")

    # # Create filtered lists
    even_numbers =[]
    odd_numbers = []
    # # Calculate average
    average =  sum(numbers)/ len(numbers)
    
    # print("avg :",average)
    
    # # Numbers greater than average
    above_average = []
    
    for i in range(10):
        if(numbers[i] % 2 == 0):
            even_numbers.append(numbers[i])
        else:
            odd_numbers.append(numbers[i])
        if(numbers[i] > average):
            above_average.append(numbers[i])
        pass

    #WHAT IF: enter 10 number and check both even odd and more than average
    # BUT I think should have declare them above of this function
    # for i in range(10):
    #     value = int(input(f"Enter Number {i+1}: "))
    #     numbers.append(value)
    #     if(value % 2 == 0):
    #         even_numbers.append(value)
    #     else:
    #         odd_numbers.append(value)
    #     if(value > average):
    #         above_average.append(value)
    # Display results
    # Your code here

    print("Even Number List:",even_numbers)
    print("Odd Number List:",odd_numbers)
    print("Above average:",above_average)
    print("Average :",average)
    print("Sum:",sum(numbers))
    print("Min:",min(numbers))
    print("Max:",max(numbers))
    # print("Above average:",above_average)
if __name__ == "__main__":
    number_operations()