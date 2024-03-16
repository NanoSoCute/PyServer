import requests
import subprocess
import datetime
import os
import webbrowser
import time
import tqdm

os.system('cls')

def read_credentials_from_github(repo_url):
    response = requests.get(repo_url)
    if response.status_code == 200:
        credentials = {}
        for line in response.text.split('\n'):
            if line.strip():  # Check if line is not empty
                username, password = line.strip().split(',')
                credentials[username] = password
        return credentials
    else:
        raise Exception("Failed to fetch file from GitHub")

def open_program(program_number):
    if program_number == "1":
        program_path = "C:/Program Files/Mozilla Firefox/firefox.exe"  # Replace with the actual path
        subprocess.Popen(program_path)
    elif program_number == "2":
        program_path2 = "D:/Minecraft/Tl.exe"
        subprocess.Popen(program_path2)
    else:
        print("Invalid input. Please enter 1 or 2.")

def login():
    repo_url = 'https://raw.githubusercontent.com/NanoSoCute/PyServer/main/assets/credentials/logincredentials.txt'
    credentials = read_credentials_from_github(repo_url)

    print(' ')
    print('Operation Done - Fetched Execute Code From Github Repo')
    time.sleep(2)
    os.system('cls')
    while True:
        username = input("User : ")
        password = input("Password : ")
        
        if username in credentials and credentials[username] == password:
            print("Login successful! - Welcome, " + username +'!')
            while True:
                os.system('cls')  # Clear the console screen
                # Get the current time
                current_time = datetime.datetime.now()

                # Convert the current time to a string in a desired format
                time_string = current_time.strftime("%H:%M:%S")  # Format: HH:MM:SS
                
                print('Time is : ' + time_string, flush=True)
                print('User : ' + username)
                print(' logout : Logout From This User ')
                print(' special_opensource : Open Github This "Open Source" Repository. ')
                print(' 1 : Open FireFox ')
                print(' 2 : Open Minecraft Launcher ')
                user_input = input("Please Enter The Choices From Above : ")
                if user_input == 'logout':
                    os.system('cls')
                    print('Logging Out From : ' + username)
                    print(' ')
                    time.sleep(2)
                    print(' ')
                    print('Operation Done - Logged Out Success')
                    print(' ')
                    time.sleep(2)
                    os.system('cls')
                    break
                elif user_input == 'special_opensource':
                    webbrowser.open('https://github.com/NanoSoCute/PyServer')
                elif user_input == '1':
                    open_program(user_input)
                elif user_input == '2':
                    open_program(user_input)
                else:
                    print("Invalid input. Please enter 1, 2, or 'logout'.")
        else:
            print("Invalid username or password. Please try again.")
            time.sleep(2)
            os.system('cls')

if __name__ == "__main__":
    login()
