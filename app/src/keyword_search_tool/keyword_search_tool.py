import requests
import os 
from dotenv import load_dotenv

load_dotenv()

class KeywordSearchTool:
    
    api = os.getenv('KEYWORD_SEARCH_API_URL')
    
    def __init__(self):
        pass    
    
    
    def search_keywords(self, keywords):
        
        print("KeywordSearchTool API: ", keywords)
        response = self.__exporter_results_by_keywords(keywords)
        return response
    
    '''
    Requisição para o Danke
    '''
    def __exporter_results_by_keywords(self, keywords):
        json_data = {}
        params = {
            'format': 'csv',
            'count': 10,
            'q': keywords
        }
        r = requests.post(self.api+'/exporter/query/results', json=json_data, params=params)
        return r.text
    
    def __exporter_results_by_conceptual_query(self, conceptual_query):
        json_data = {"query": conceptual_query}
        params = {
            'format': 'csv',
            'count': 10
        }
        r = requests.post(self.api+'/exporter/query/results', json=json_data, params=params)
        return r.text
        
    def __get_conceptual_query(self, keywords):
        r = requests.get(self.DANKE_API+'/search/queries?q='+keywords)
        return r.json();
