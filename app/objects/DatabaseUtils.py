import mysql.connector
import os

from pandas import DataFrame

par_db = {
    "host": "127.0.0.1",
    "database": "streamapp",
    "user": "root",
    "password": "root",
}

class database:
    def __init__(self):
        self.dir = os.getcwd()
        self.cnx_mysql = mysql.connector.connect(
            host=par_db.get("host"),
            user=par_db.get("user"),
            database=par_db.get("database"),
            password=par_db.get("password"),
        )
        self.str_query_on = "insert into giroscope_mpu_on(x, y, z, date_mpu, time_mpu, time_float) values({x}, {y}, {z}, '{date_mpu}','{time_mpu}',{time_float})"
        self.str_query_off = "insert into giroscope_mpu_off(x, y, z, date_mpu, time_mpu, time_float) values({x}, {y}, {z}, '{date_mpu}','{time_mpu}',{time_float})"
        self.str_query_live = "insert into giroscope_mpu_live(x, y, z, date_mpu, time_mpu, time_float) values({x}, {y}, {z}, '{date_mpu}','{time_mpu}',{time_float})"

    def execute_from_query(self, sql_file):
        with open(self.dir + "/" + sql_file, "r") as reads:
            sqlScript = reads.read()
            cursor_cnxn_msql = self.cnx_mysql.cursor()
            cursor_cnxn_msql.execute(sqlScript)

    def ingest(self, values:dict, type):
        if type =='on':
            insert_query = self.str_query_on.format(**values)
        elif type == 'off':
            insert_query = self.str_query_off.format(**values)
        else:
            insert_query = self.str_query_live.format(**values)

        cursor_cnxn_msql = self.cnx_mysql.cursor()
        cursor_cnxn_msql.execute(insert_query)
        self.cnx_mysql.commit()
