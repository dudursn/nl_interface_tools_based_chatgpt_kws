# Combining OpenAI ChatGPT and Database Keyword Search 

This application proposes two alternatives to use ChatGPT to extract keywords from NL
sentences, expressing database queries, which are then passed to the database keyword search tool (KwS
tool). It describes experiments based on KwS tools that work on top of relational databases
and RDF datasets with or without an RDF schema and translate NL queries  from ChatGPT and compares both. 

The experiments from ChatGPT consists in translate NL queries into SQL and extract keywords
from a text block.

To translate in SQL queries, we have three approaches:
- we create a simple input, without practically any context passed, using the knowledge of the model;
- we provide manually context information about schema, joins, tables and columns to model;
- we use LangChain to provide context information for model, automatically way.

The SQL queries translation experiments are in notebooks at [studies_translate_SQL_query_Langchain](/studies_translate_SQL_query_Langchain).

To extracted keywords from ChatGPT and send for KwS, we have two approaches:
- we create a simple input, without practically any context passed, using the knowledge of the model;
- we provide manually context information about KwS, database, queries examples in natural language and the desired responses to model;

The extracted keywords experiments are in an application at [app](app/src).

## Installing / Getting started
    > git clone https://github.com/dudursn/chatgpt_kws.git
    > cd /chatgpt_kws
    Run the batch file:
    > .\install.bat
    Then, run:
    > .\run.bat
  
## Developing

### Built With
- Flask v2.2
- openai v0.27.8
- openpyxl v3.0.9
- pandas v1.3.4
- Flask-cors v3.0.10
- requests v2.31.0
- python-dotenv v1.0.0
  
### Prerequisites
- Python 3.10.7
- OPENAI_KEY: [OpenAI key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)

Authors: Eduardo Nascimento, Grettel Monteagudo García, Wendy Zuloaga Victorio,
Melissa Lemos, Yenier Torres Izquierdo, Luiz André Portes Paes Leme and
Marco A. Casanova
