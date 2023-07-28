from keyword_search_tool.keyword_search_tool_service import KeywordSearchToolService
from benchmark_keywords.benchmark_keywords_service import BenchmarkKeywordsService
from interface.service_interface import ServiceInterface
import sys

# Obtendo os argumentos da linha de comando
args = sys.argv
user_command = args[1].lower()
opt = "1"
if len(args) > 2:
    opt = args[2].lower() 
OPENING_MESSAGE = "System: You are a helpful assistant that extract keywords from a block of text,\n" + \
    "search for it in a database and show the results. "
print(OPENING_MESSAGE)  

def main():
    service = get_service(user_command)
    if (service != None):
       service.execute(opt)
    else: 
        print('Specific a valid argument: \'kws\' or \'benchmark\' (Ex. > python main.py kws)')

def get_service(user_comand) -> ServiceInterface:
    services = {"kws": KeywordSearchToolService(), "benchmark": BenchmarkKeywordsService()}
    if user_command in services: 
        return services[user_comand]
    return None
    
    
if __name__ == "__main__":
    main()
