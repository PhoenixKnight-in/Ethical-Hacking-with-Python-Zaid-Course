import requests

def request(url):
    try:
        return requests.get("http://"+url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "192.168.159.153/mutillidae/"
with open("subdomains-wodlist.txt","r") as f:
    content = f.readlines()
    for line in content:
        word = line.strip()
        test_url = word + "." +target_url
        response = request(test_url)
        if response:
            print("[+] Discovered Directory --> "+test_url)
