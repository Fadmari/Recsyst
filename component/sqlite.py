import pandas as pd
import sqlite3
import os

class SQLite:
    
        
    def __init__(self, db_name):
        self.db_name = db_name
        self.fileways = os.path.dirname(__file__)
    
    
    
    def __create_connection(self):
        self.connection = sqlite3.connect("{}/../data/users_data/{}".format(self.fileways,self.db_name))
        
        
        
    def __close_connection(self):
        self.connection.close()

        
        
    def get_data_from_sql(self,query):

        self.__create_connection()
        cursor = self.connection.cursor()
        res = cursor.execute(query)
        datafrombd =  res.fetchall()
        self.__close_connection()
        
        return datafrombd
    
    
    
    def update_data_to_sql(self,query):
        pass
    
    
    
    def insert_data_to_sql(self,query):
        pass