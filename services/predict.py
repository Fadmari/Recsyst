import os
import sys
import pickle 
import pandas as pd

from component import sqlite

fileways = os.path.dirname(__file__)
sys.path.append("{}/../".format(fileways))

class predict:
    def __init__(self, user):
        self.user = user
        self.fileways = os.path.dirname(__file__)
        self.db = sqlite.SQLite('movie_data.db') # вставить название бд
        
    def __load_mdl(self):
        with open("{}/../data/models/svd.pkl".format(self.fileways), 'rb') as f:
            self.mdl = pickle.load(f)
            
    def __create_data_for(self):
        
        self.df_useritem = pd.DataFrame()
        self.df_useritem['user_id'] = [self.user for i in self.all_items_id]
        self.df_useritem['item_id'] = self.all_items_id
        
        
    def __get_items_id(self):
        
        query = "SELECT movieId FROM movies"
        result = self.db.get_data_from_sql(query)
        temp = pd.DataFrame(result)
        self.all_items_id = temp[0].values
        
        
    def __reccomend(self):
        temp = self.df_useritem.copy()
        temp['pred_score'] = self.mdl.predict(self.df_useritem)
        temp = temp.sort_values(by = ['pred_score'], ascending = False)
        
        self.rec_items_id = temp.head(10)['item_id'].values
        
    
    def __get_items_name(self):
        
        query = "SELECT title FROM movies WHERE movieId in {}".format(tuple(self.rec_items_id))
        result = self.db.get_data_from_sql(query)
        for i in result:
            print(i)
            
  #  def __get_actual_item(self):
        
   #     self.mdl.df_data
        
        
    def run(self):
        self.__load_mdl()
        self.__get_items_id()
        self.__create_data_for()
        self.__reccomend()
        self.__get_items_name()
        
        
    
    
        


    