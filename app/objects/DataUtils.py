"""
Data Transform for thingspeaks sources
"""
import pandas as pd

class operators():
    def __init__(self, col, json_data):
        self.col = col
        self.json_data = json_data

    def gen_dataframe(self):
        df = pd.DataFrame(data= self.json_data, columns = self.col)
        df[self.col[-1]] = df[self.col[-1]].apply(lambda strg : strg.replace('}',''))

        return df

    def clean_data(self, df: pd.DataFrame, new_col):
        dict_names = dict(zip(self.col, new_col))
        df = df.rename(columns=dict_names, inplace=False)

        df['datetime'] = df['datetime'].apply(lambda x : x.replace('Z','').split('T'))
        df['date_mpu'] = df['datetime'].apply(lambda x : x[0])
        df['time_mpu'] = df['datetime'].apply(lambda x : x[1])
        df['float_time_list'] = df['time_mpu'].apply(lambda x : x.split(':'))
        df['time_float'] = df['float_time_list'].apply(lambda x : float(x[0]) + float(x[1])/60 + float(x[2])/3600)

        df = df.drop(columns=['datetime', 'float_time_list'])
        return df


    
