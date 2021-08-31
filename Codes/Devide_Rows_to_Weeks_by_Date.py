import csv
import pandas as pd
newRow=[]
with open('/Users/mertyenilmez/Thesis/covid_ireland.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
    for j in range(30):
        for i in range(7):
            if row[0][0:10]== str(pd.to_datetime("2020-03-16")+ pd.DateOffset(days=i)+pd.DateOffset(weeks=j))[0:10]:
                newRow.append([j+1,row[1]])

with open('/Users/mertyenilmez/Thesis/covid_ireland.csv', 'wt') as f:
    csv_writer = csv.writer(f)

    csv_writer.writerows(newRow)
