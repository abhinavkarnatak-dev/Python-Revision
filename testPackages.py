import requests

response = requests.get("https://api.github.com")
print(response.status_code) # prints 200 when GitHub is reachable