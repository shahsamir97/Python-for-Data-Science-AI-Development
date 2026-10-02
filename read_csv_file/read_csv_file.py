import pandas as pd
import requests
import os

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"

def download(url, filename):
    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, "wb") as file:
            file.write(response.content)

if os.path.exists("read_csv_file/addresses.csv") is False:
    download(url, "read_csv_file/addresses.csv")
else:
    print("File already exists.")

df = pd.read_csv("read_csv_file/addresses.csv", header=None)
df.columns = ["First Name", "Last Name", "Address", "City", "State", "Zip Code"]

print(df.loc[[0,1,2], "First Name"])
print(df.iloc[[0,1,2], 0:3])