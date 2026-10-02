import requests
import os

url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path=os.path.join(os.getcwd(), 'Example1.txt')

response = requests.get(url)
with open(path, 'wb') as file:
    file.write(response.content)
