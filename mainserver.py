import os
import subprocess

def open_program(program_number):
    if program_number == "1":
        print('Hello World!')
    elif program_number == "2":
        print('Hello World!')
    else:
        print("Invalid input. Please enter 1 or 2.")

if __name__ == "__main__":
    user_input = input("Enter 1 to open program 1, 2 to open program 2: ")
    open_program(user_input)
