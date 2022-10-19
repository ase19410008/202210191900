# https://stackoverflow.com/questions/2380013/converting-date-time-in-yyyymmdd-hhmmss-format-to-python-datetime
# py source.py n m t
import sys
import csv
from datetime import datetime as dt, timedelta

n, m, t = -1, -1, -1
if len(sys.argv) == 4:
    n, m, t = [int(arg) for arg in sys.argv[1:]]

res_cnt, err_cnt, = 0, 0
res_time, elapsed_time = 0, timedelta()
fmt = "%Y%m%d%H%M%S"

with open("log.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["res"] == "-":
            err_cnt += 1
            if err_cnt == 1:
                print(row["addr"])
                err_date = row['date']
            elapsed_time += dt.strptime(row["date"], fmt) - dt.strptime(err_date, fmt)
        else:
            # 設問3
            if res_cnt == m:
                avg_time = res_cnt / res_cnt
                if t < avg_time:
                    print(avg_time)
            res_cnt += 1
            res_time += int(row["res"])

    # 設問2
    if n == err_cnt:
        print(elapsed_time)
