
from .benchmark_keywords import BenchmarkKeywords

class BenchmarkKeywordsConfig():
    def __init__(self):
        self.__benchmark = BenchmarkKeywords('data/lista_palavras_chaves.csv')

    def get_config_function(self):
        
        return {
            "object": self.__benchmark,
            "function_call" :  {"name": self.__benchmark.save_keyword.__name__},
            "functions" : [
                {
                    "name": self.__benchmark.save_keyword.__name__,
                    "description": "Send keywords to analyze",
                    "parameters": {
                        "type": "object",
                        "properties": {                        
                            "keywords": {"type": "string"},
                                    
                        },
                        "required": ["keywords"],
                    }
                }
            
            ] 
        }
        
    def get_benchmark(self):
        return self.__benchmark
        
    
    