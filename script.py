import csv
from datetime import datetime


with open(r"/data/results.csv", "a") as f:
    w = csv.writer(f)
    date = datetime.now()
    w.writerow([date])
