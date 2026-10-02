import requests
import json
import pandas as pd

data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all", timeout=30)
results = json.loads(data.text)
results_df = pd.DataFrame(results)
normailized_results_df = pd.json_normalize(results)

print(normailized_results_df)