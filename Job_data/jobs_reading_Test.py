import csv
import pandas as pd

"""
csv_file = open("/nethome/ynakajo6/Research/GT_router/Job_data/Jobs_list.csv", "r")
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"')

header = next(f)
print(header)
Jobslist=[]
for row in f:
	Jobslist.append(row)

print(Jobslist)
"""

df=pd.read_csv("/nethome/ynakajo6/Research/GT_router/Job_data/Jobs_list.csv", header=None)

df=df.T.values.tolist()
Jobs_list=df[0]
print(Jobs_list)
print(type(Jobs_list))
