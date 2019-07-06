import pymysql.cursors
import pandas as pd
import os
import json

class db_metawear:

    def __init__(self, conn_type='update'):
        # pull credentials
        # cred = self.load_json('credentials.json')

        if conn_type == 'update':
            self.connection = pymysql.connect(
                # host = 'localhost',
                port = 3306,
                user = 'metawear_db_manage',
                password = 'metawear_SQL1!',
                db = 'metawear',
                unix_socket = '/var/run/mysqld/mysqld.sock',
                # charset = 'utf-8',
                cursorclass = pymysql.cursors.DictCursor
            )

    def run_sql(self, sql, auto_commit=True):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)

        if auto_commit:
            self.connection.commit()

    def close_connection(self):
        self.connection.close()


    def load_json(self, json_file):
        location = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        js_file = open(os.path.join(location, json_file))
        js_str = js_file.read()
        js_dict = json.loads(js_str)
        return js_dict