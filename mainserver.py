import requests
import os
import subprocess

def read_credentials_from_github(repo_url, filename):
    response = requests.get(repo_url + '/raw/main/' + filename)
    if response.status_code == 200:
        credentials = {}
        for line in response.text.split('\n'):
            if line.strip():  # Check if line is not empty
                username, password = line.strip().split(',')
                credentials[username] = password
        return credentials
    else:
        raise Exception("Failed to fetch file from GitHub")

def login():
    repo_url = 'https://raw.githubusercontent.com/NanoSoCute/PyServer/main/assets/credentials/'
    filename = 'logincredentials.txt'
    credentials = read_credentials_from_github(repo_url, filename)
    
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        if username in credentials and credentials[username] == password:
            print("Login successful!")
            user_input = input("Enter 1 to open program 1, 2 to open program 2, or 'logout' to return to the login page: ")
            if user_input == 'logout':
                break
            else:
                open_program(user_input)
        else:
            print("Invalid username or password. Please try again.")

def open_program(program_number):
    if program_number == "1":
        print('Hello World from Program 1!')
    elif program_number == "2":
        print('Hello World from Program 2!')
    else:
        print("Invalid input. Please enter 1 or 2.")

if __name__ == "__main__":
    login()
