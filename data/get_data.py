import pandas as pd
import requests
import os
from datetime import datetime

# datetime object containing current date and time
now_str = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
p_dir = "/Users/rishabhkaushal/dsa-project/data"  
os.chdir(p_dir)
path = os.path.join(p_dir, now_str)
os.mkdir(path)
print ("creating dir:", path)
os.chdir(path)

# downloading the data files
for i in range (1,201):
  print ("downloading ", i, " csv file")
  url = 'https://transparency.dsa.ec.europa.eu/statement/csv?page=' + str(i)
  r = requests.get(url, allow_redirects=True)
  filename = str(i) + '.csv'
  open(filename, 'wb').write(r.content)

# merging and de-duplicating
first_file_name = "1.csv"
data = pd.read_csv(first_file_name)
print ("merging begins ... ")
print (data.shape)

for i in range (2,201):
  filename = str(i) + ".csv" 
  tmpdata = pd.read_csv(filename)
  data = pd.concat([data,tmpdata]).drop_duplicates('uuid').reset_index(drop=True)
  print (i, data.shape)

final_file = os.path.join(path, "data.csv")
data.to_csv (final_file)
print (data['created_at'].min(), " to ", data['created_at'].max())
