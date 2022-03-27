"""
    ----Main code to get the data and 
    ----ingest into an database engine.
    ----Needs to have a thingspeaks API key

    @autor: Eng. Francis Zavaleta
    """
    from dataclasses import fields
    import os
    import requests
    import objects.DataUtils as du
    import objects.DatabaseUtils as db

    #Parameters
    dir = os.getcwd()
    fields_giroscope = ['datetime', 'id', 'x', 'y', 'z']
    fields_tks = ['created_at', 'entry_id', 'field1', 'field2', 'field3']

    # First we need to build the valid url
    READ_KEY = list(map(lambda x: x.strip(), open(dir + "/" + "keys", "r").readlines()))
    URL = "https://api.thingspeak.com/channels/{id_channel}/feeds.json?api_key={api_read_key}&results=700".format(
        id_channel=READ_KEY[-1], api_read_key=READ_KEY[0]
    )

    # get data response and feed
    data_all_channel = requests.get(URL).json()
    data_feed = data_all_channel['feeds']

    #transform data into dataframe structure
    giroscope = du.operators(col = fields_tks, json_data = data_feed)
    giroscope_df = giroscope.gen_dataframe()
    giroscope_df_clean = giroscope.clean_data(giroscope_df, new_col=fields_giroscope)

    #Create Mysql tables
    data_engine = db.database()
    try:
        data_engine.execute_from_query(sql_file='database.sql')
    except:
        print("Database tables already exist!!!")

    #Load data into table
    len_data = giroscope_df_clean.shape[0]
    for i in range(0, len_data):
        values = giroscope_df_clean.iloc[i].to_dict()
        data_engine.ingest(values=values, type='live')