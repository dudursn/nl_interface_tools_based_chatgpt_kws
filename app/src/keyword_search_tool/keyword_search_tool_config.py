
from .keyword_search_tool import KeywordSearchTool

class KeywordSearchToolConfig():
    def __init__(self):
        self.__keyword_search_tool = KeywordSearchTool()

    def get_config_function(self):
        
        return {
            "object": self.__keyword_search_tool,
            "function_call" :  {"name": self.__keyword_search_tool.search_keywords.__name__},
            "functions" : [
                {
                    "name": self.__keyword_search_tool.search_keywords.__name__,
                    "description": "Send keywords to keyword search tool",
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
        
    def get_keyword_search_tool(self):
        return self.__keyword_search_tool
    