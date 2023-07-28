
from .keyword_search_tool_config import KeywordSearchToolConfig
from openai_model.chatgpt import run_conversation
from interface.service_interface import ServiceInterface

class KeywordSearchToolService(ServiceInterface):
    def __init__(self):
        self.__kws_config = KeywordSearchToolConfig()

    def execute(self, opt="1"):
        print("Type 'exit' and press ENTER to stop...\n")
        user_input = input("USER: ")
        while user_input != "exit":
            run_conversation(user_input, self.__kws_config.get_config_function(), opt)
            user_input = input("USER: ")