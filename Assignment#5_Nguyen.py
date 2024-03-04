#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:27:28 2024

@author: tnguyen287
"""

#Create a class named BasicMathOperations.
class BasicMathOperations:
    
    #Inside the class, define methods for each of the tasks listed below.
    def __init__(self,  first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        
    #Greet User: A method that takes a first name and last name, then greets the user with their full name.
    def GreetUser(self):
        print(f" Hi {self._first_name} {self._last_name}!")
        
    #Add Numbers: A method that prompts the user for two numbers, adds them, and returns the sum.
    def AddNumber(self, x, y):
        return x + y
    
    def PerformOperation(self, num1, num2, operation):
        '''
        Perform Operation: A method that takes three arguments: num1, num2, and an operator. It
        performs the operation (addition, subtraction, multiplication, or division) on the numbers and
        returns the result.
        '''
   
        if operation == 'add':
            return num1 + num2
        elif operation == 'subtraction':
            return num1 - num2
        elif operation == 'multiplication':
            return num1 * num2
        elif operation == 'division':
            result = num1 / num2
            rounded = round(result, 3)  
            return rounded
        
    def SquareNumber(self, number):
        '''
        Square Number: A method that takes a number as an argument and returns its square.
        '''
        self._number = number
        return self._number ** 2
    
    #Factorial: A method that computes the factorial of a number.
    def Factorial(self):
        result = 1
        if self._number == 0:
            return 1 
        for i in range(1, self._number + 1):
           result *= i
        return result
    
    #Counting: A method that takes a start and an end number as inputs and displays counting from start to end.
    def Counting(self, num1, num2):
        lst = []
        for i in range(num1 , num2 + 1):
            lst.append(i)
        return lst
    
    #Compute Hypotenuse
    def calculate_hypotenuse(self, a, b):
        square_a = self.SquareNumber(a)
        square_b = self.SquareNumber(b)
        result = (square_a + square_b) ** 0.5
        round_result = round(result, 3)
        return round_result
    
        
        #Area of Rectangle: A method that calculates the area of a rectangle given its width and height.
        def area(self, a, b):
            return a * b
    
    #Power of Number: A method that computes the power of a number (e.g., base^exponent).
    def PowerofNumber(self, number, exponent):
        return number ** exponent
    
    #Type of Argument: A method that accepts an argument and returns its type.
    def TypeofArgument(self, anything):
        return type(anything)
    
    
def main():
    # Create an instance of BasicMathOperations with placeholder values
    first_name = input('Please input your first name: ')
    last_name = input('Please input your last name: ')
    
    
    operations = BasicMathOperations(first_name, last_name)

    # Task dictionary to map user choices to class methods
    tasks = {
        "1": ("Greet User", operations.GreetUser),
        "2": ("Add Numbers", operations.AddNumber),
        "3": ("Perform Operation", operations.PerformOperation),
        "4": ("Square Number", operations.SquareNumber),
        "5": ("Compute Factorial", operations.Factorial),
        "6": ("Counting", operations.Counting),
        "7": ("Compute Hypotenuse", operations.calculate_hypotenuse),
        "8": ("Compute Power of Number", operations.PowerofNumber),
        "9": ("Determine Type of Argument", operations.TypeofArgument)
    }

    while True:
        print("\nAvailable Tasks:")
        for key in tasks:
            print(f"{key}: {tasks[key][0]}")

        choice = input("Please select a task by number (or type 'exit' to quit): ")

        if choice.lower() == 'exit':
            print("Goodbye!")
            break

        if choice in tasks:
            # Some tasks require additional inputs, handle them individually
            if choice == '1':
                operations.GreetUser()
            elif choice == '2':
                num1 = int(input('Input your 1st number: '))
                num2 = int(input('Input your 2nd number: '))
                print("Sum:", operations.AddNumber(num1, num2))
            elif choice == '3':
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                operation = input("Enter the operation (add, subtraction, multiplication, division): ")
                print("Result:", operations.PerformOperation(num1, num2, operation))
            elif choice == '4':
                number = float(input("Enter a number to square: "))
                print("Square:", operations.SquareNumber(number))
            elif choice == '5':
                number = int(input("Enter a number to compute the factorial: "))
                operations._number = number  # Update the number attribute
                print("Factorial:", operations.Factorial())
            elif choice == '6':
                start = int(input("Enter the start number: "))
                end = int(input("Enter the end number: "))
                print("Counting:", operations.Counting(start, end))
            elif choice == '7':
                a = float(input("Enter side a: "))
                b = float(input("Enter side b: "))
                print("Hypotenuse:", operations.calculate_hypotenuse(a, b))
            elif choice == '8':
                number = float(input("Enter the base number: "))
                exponent = float(input("Enter the exponent: "))
                print("Power:", operations.PowerofNumber(number, exponent))
            elif choice == '9':
                anything = input("Enter an argument to check its type: ")
                print("Type:", operations.TypeofArgument(anything))
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid selection, please try again.")

if __name__ == "__main__":
    main()

            
            
    
    
    
    
    
    
    
    
    
            
        