import os
import pandas
from dotenv import load_dotenv, dotenv_values
from telegram_sleuth import Sleuth

load_dotenv()
API_ID = os.getenv("TELEGRAM_API_ID")
API_HASH = os.getenv("TELEGRAM_API_HASH")

sleuth = Sleuth(
    api_id = API_ID,
    api_hash = API_HASH,
    username = 'cyber_security_feed',
    start_date = '2024-11-01',
    end_date = '2024-11-01',

)

# Generate a dict with messages, media, & metadata. Then dumps to a CSV
data = sleuth.dig()

dataframe = pandas.DataFrame(data)
dataframe.to_csv('output.csv', index=True)
