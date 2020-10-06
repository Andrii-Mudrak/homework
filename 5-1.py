import pathlib
import json
import csv

with open('mlt_budget.json') as json_file:
    data = json.load(json_file)
f = csv.writer(open("mlt_budget.csv", "w", newline=''))
f.writerow(list(data[0]))                             # csv headers

for data in data:
    f.writerow([data['date'],
                data['budget_id'],
                data['budget__name'],
                data['budget__code'],
                data['fond_id'],
                data['fond__code'],
                data['fond__name'],
                data['source_id'],
                data['source__code'],
                data['source__name'],
                data['plan_s'],
                data['fact_s']]
             )
    #f.writerow(*row.values())
