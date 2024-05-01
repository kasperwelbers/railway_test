import csv, logging
from datetime import datetime

date = datetime.now()

logger = logging.getLogger(__name__)
logger.info(date)

with open(r"data/results.csv", "a") as f:
    w = csv.writer(f)
    w.writerow([date])
