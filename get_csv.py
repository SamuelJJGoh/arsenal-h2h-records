import requests
import pandas as pd
from io import StringIO

headers = {
    "Accept-Language": "en-GB,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
}

h2h_history_url = "https://fbref.com/en/squads/18bb7c10/history/vs_opp/Arsenal-Records-vs-Opponents"
data = requests.get(h2h_history_url, headers=headers)

h2h = pd.read_html(StringIO(data.text), match="Records vs. Opponents", flavor="lxml")[0]
h2h.to_csv('arsenal_h2h_records.csv', index=False)