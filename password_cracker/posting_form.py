import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "http://192.168.159.153/mutillidae/?page=dns-lookup.php"
response = request(target_url)

parsed_content = BeautifulSoup(response.content,"lxml")
forms_list = parsed_content.findAll('form')
for form in forms_list:
    action = form.get('action')
    post_url = urlparse(target_url,action)
    print(post_url.geturl())
    method = form.get('method')
    print(method)
    input_list = form.findAll('input')
    data_dict = {}
    for input in input_list:
        input_name = input.get("name")
        input_type = input.get("type")
        input_value = input.get("value")
        if input_type == "text":
            input_value = "test"
        data_dict[input_name] = input_value
    result = requests.post(post_url.geturl(), data=data_dict)
    print(result.content)





