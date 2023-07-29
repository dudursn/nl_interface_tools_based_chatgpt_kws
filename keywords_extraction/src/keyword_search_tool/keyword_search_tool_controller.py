
from .keyword_search_tool_service import KeywordSearchToolService
from flask import jsonify

class KeywordSearchToolController():
    def __init__(self):
        self.__kws_service = KeywordSearchToolService()

    def run(self, message, opt_prompt = 1):
        return self.__kws_service.execute(message, opt_prompt)
