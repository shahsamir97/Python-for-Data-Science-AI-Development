import pandas as pd
import requests

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx"

def download(url, filename):

    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, "wb") as file:
            file.write(response.content)

download(filename, "read_xlsx_file/file_example_XLSX_10.xlsx")

df = pd.read_excel("read_xlsx_file/file_example_XLSX_10.xlsx")
print(df)