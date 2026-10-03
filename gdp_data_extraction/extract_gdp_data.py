import pandas as pd
import numpy as np

url="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
headers = {
    'User-Agent': 'MyLearningProject/1.0 (contact: mdshahsamir1997@gmail.com)'
}

tables = pd.read_html(url)
df = tables[3]
df.columns = range(df.shape[1])
df = df[[0,2]]
df.columns = ['Country','GDP (Million USD)']
#df = df.iloc[1:11, :]
df = df.loc[1:10,:]
df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int)
df['GDP (Million USD)'] = df['GDP (Million USD)'] / 1000
df[['GDP (Million USD)']] = np.round(df[['GDP (Million USD)']], 2)
df.rename(columns={'GDP (Million USD)':'GDP (Billion USD)'})

with open("gdp_data_extraction/gdp_data.csv", "w+") as file:
    df.to_csv(file, index=False)
    file.seek(0)
    df2 = pd.read_csv("gdp_data_extraction/gdp_data.csv")
    print(df2)

