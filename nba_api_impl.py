from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd

nba_teams = teams.get_teams()

df_teams = pd.DataFrame(nba_teams)

print(df_teams.head())