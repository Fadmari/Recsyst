import os
import sys
import pickle 
import pandas as pd
fileways = os.path.dirname(__file__)
sys.path.append("{}/../".format(fileways))

from models import svdrecsys
from component import sqlite
from helper import helper as h


class train:

    def __init__(self):
        self.n_news = 150
        self.fileways = os.path.dirname(__file__)

        
        
    def __get_data(self):
        
        db = sqlite.SQLite('movie_data.db') # вставить название бд

        query = "SELECT userId, movieId, rating FROM ratings"
        result = db.get_data_from_sql(query)
        df_data = pd.DataFrame(result)
        df_data = df_data.rename({0:'user_id', 1:'item_id', 2:'score'}, axis='columns') # костыль
        self.df_data = df_data
    


    def __fit(self):
    
        X, y = h.create_train_data(self.df_data, self.n_news)

        self.mdl = svdrecsys.RecSysSVD()
        self.mdl.fit(X,y)

        
        
    def __save_mdl(self):
        
        with open("{}/../data/models/svd.pkl".format(self.fileways), "wb") as f:
            pickle.dump(self.mdl, f)

    
    def run(self):
        
        self.__get_data()
        self.__fit()
        self.__save_mdl()
        
        

