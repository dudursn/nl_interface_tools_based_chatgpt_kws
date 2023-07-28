import openai
import json
import os
from dotenv import load_dotenv
from prompt_messages.messages import get_messages

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

'''
Requisição para o ChatGPT

'''
def run_conversation(prompt_input, functions_to_chatgpt, opt=1, show_result = True):


    function_call = functions_to_chatgpt["function_call"]
    functions = functions_to_chatgpt["functions"]
    object = functions_to_chatgpt["object"]
        
    
    prompt_messages = get_messages(opt)   
    prompt_messages.append({"role": "user", "content": prompt_input})  
              
    '''
    Extract keywords from a block of text. At a lower temperature it picks keywords from the text.
    At a higher temperature it will generate related keywords which can be helpful for creating search indexes.
    '''
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages= prompt_messages,
        temperature=0.5,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.8,
        presence_penalty=0.0,
        functions= functions,
        #function_call="auto",
        function_call= function_call
    )

    message = response["choices"][0]["message"]

    # Step 2, check if the model wants to call a function
    if message.get("function_call"):

        function_name = message["function_call"]["name"]
        function_args = json.loads(message["function_call"]["arguments"])
        print("CHATGPT ASKED TO RUN FUNCTION: " + function_name + "(" + function_args.get("keywords") + ")\n")

        # Step 3, call the function
        function_to_run = getattr(object, function_name)
        
        function_response = function_to_run(
            keywords = function_args.get("keywords")       
        )
        
        if(show_result):
            prompt2 = "USER: Show me the results from query."

            # Step 4, send model the info on the function call and function response
            second_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0613",
                messages=[
                    {"role": "user", "content": prompt2},
                    message,
                    {
                        "role": "function",
                        "name": function_name,
                        "content": function_response,
                    },
                ],
            )
            print("CHATGPT: " + second_response["choices"][0]["message"]["content"].strip())
    else:
        print("CHATGPT: " + response["choices"][0]["message"]["content"].strip())
        
