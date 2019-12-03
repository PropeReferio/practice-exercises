import requests
 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)

 
print(r)