import pandas as pd
import requests
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"

def download(url, filename):
    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, "wb") as file:
            file.write(response.content)

download(url, "visualize_diabetes_data/diabetes.csv")
df = pd.read_csv("visualize_diabetes_data/diabetes.csv")
print(df.describe())

labels = "Not diabetic", "Diabetic"
plt.pie(df['Outcome'].value_counts(), labels=labels, autopct='%0.02f%%')
plt.legend()
plt.show()