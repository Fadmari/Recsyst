import numpy as np
import pandas as pd
from scipy.sparse.linalg import svds
from recommender_model import RecSysSVD
import recsys_helper as rh

import unittest

class RecSysTest(unittest.TestCase):
    
    def setUp(self):
        self.data = pd.read_csv('data\movie_data.csv')
        self.data = self.data.rename({'userId':'user_id', 'movieId':'item_id', 'rating':'score'}, axis='columns')
        self.mdl = RecSysSVD()
        self.X, self.y = rh.create_train_data(self.data, 150)
        self.mdl.fit(self.X,self.y)        
    
            
    def test_untitled_user_item(self):        
                
        true_value = 0.3
        user = 615
        item = 1
        
        test_value = self.mdl.predict_one(user, item)
        
        self.assertEqual(test_value, true_value)
        
        
    def test_type_user_id(self):
        
        test_value = str(self.data.user_id.dtypes)[:3]
        true_value = 'int'
                
        self.assertEqual(test_value, true_value)
        
    
    
        
if __name__ == '__main__':
    unittest.main()
                