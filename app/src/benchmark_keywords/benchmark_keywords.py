import pandas as pd

from datetime import datetime

class BenchmarkKeywords:
    
    def __init__(self, file_csv):
        self.keywords_list = pd.read_csv(file_csv)
        self.__total = len(self.keywords_list)
        self.keywords_generated = []
         
        
    def get_question(self, pos):
        if(pos < len(self.keywords_list)):
            return self.keywords_list.iloc[pos]['questions']
        return None
    
    def get_keyword(self, pos):
        return self.keywords_list.iloc[pos]['keywords']
        
    def save_keyword(self, keywords):
        keywords = keywords.replace(",", " ")
        print(keywords)
        self.keywords_generated.append(keywords)
        return keywords
    
    def save_result(self):
        
        self.keywords_list["keywords_result"] = self.keywords_generated
        #self.__compare_results()
        
        now = datetime.now()
        self.keywords_list.to_csv("data/out_"+ str(now.timestamp()) +".csv", index=False)
        
    def __compare_results(self):
        self.keywords_list['result'] = self.keywords_list.apply(lambda row: row['keywords'] in row['keywords_result'], axis=1)
            
    def get_total(self):
        return self.__total