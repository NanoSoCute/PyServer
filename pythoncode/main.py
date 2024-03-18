import requests
import subprocess
import datetime
import os
# import webbrowser
import time

os.system('cls')

def loadingbar(max_steps):
    for i in range(100):
        percent = i
        bar = "[" + "=" * i + " " * (100 - i) + "]"
        print(f"\rLoading: {bar} {percent}%" + ' Complete!')  # \r for carriage return 
        time.sleep(0.01)
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
        print('Hello World from Program 2!')
    else:
        print("Invalid input. Please enter 1 or 2.")

def login():
    repo_url = 'https://raw.githubusercontent.com/NanoSoCute/AuthSystem/main/account.txt'
    credentials = read_credentials_from_github(repo_url)

    loadingbar(100)
    time.sleep(1)
    print(' ')
    print('Operation Done - Fetched Execute Code From Github Repo')
    time.sleep(3)
    os.system('pause')
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
                
                print(' Time is : ' + time_string, flush=True)
                print(' User : ' + username)
                print('')
                print('')
                print(' [ logout ] : Logout From This User ')
                print(' [ 1 ] : Open FireFox ')
                print(' [ 2 ] : Open Minecraft Launcher ')
                print('')
                print('')
                user_input = input(" Please Enter The Choices From Above - ")
                if user_input == 'logout':
                    os.system('cls')
                    print('Logging Out From : ' + username)
                    print(' ')
                    loadingbar(1)
                    print(' ')
                    print('Operation Done - Logged Out Success')
                    print(' ')
                    time.sleep(2)
                    os.system('cls')
                    break
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
    loadingbar(20)
    login()
