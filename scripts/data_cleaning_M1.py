import pandas as pd
from datetime import datetime
import numpy as np

# Note deleted the query.csv file after saving as a txt file
# df = pd.read_csv('/workspaces/Group-Formative-Assignment-Data-Cleaning-and-Collaborative-Coding//data/query.csv')
# df.to_csv('/workspaces/Group-Formative-Assignment-Data-Cleaning-and-Collaborative-Coding//data/dataset_M1.txt', sep=',', index=False) #saving original dataset as a txt file

df = pd.read_csv('/workspaces/Group-Formative-Assignment-Data-Cleaning-and-Collaborative-Coding/data/dataset_M1.txt', sep=',')

# Function to remove trailing Z in time and updated columns
def removing_trailing_z(column):
    updated_column = []
    for row in column:
        if 'Z' in row:
            updated_column.append(row.replace('Z', ''))
        else: 
            updated_column.append(row)
    return pd.DataFrame(updated_column)

df['time'] = removing_trailing_z(df['time'])
df['updated'] = removing_trailing_z(df['updated'])

# Setting time/update column as a datetime object 
df['time'] = pd.to_datetime(df['time']).dt.floor("s")
df['updated'] = pd.to_datetime(df['updated']).dt.floor("s") 
print(df.head(1))

# Saving updated dataframe as a txt file called 'cleaned_data_M1.txt'
# df.to_csv('/workspaces/Group-Formative-Assignment-Data-Cleaning-and-Collaborative-Coding/output/cleaned_data_M1.txt', sep=',', index=False)
