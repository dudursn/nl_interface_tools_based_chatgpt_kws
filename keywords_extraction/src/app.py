from flask import Flask, request, url_for, redirect, render_template
from keyword_search_tool.keyword_search_tool_controller import KeywordSearchToolController
# from benchmark_keywords.benchmark_keywords_contrroller import BenchmarkKeywordsController
from logs.log_manager import LogManager

import flask

app = Flask('chatgpt_kws')

@app.route("/", methods = ['GET','POST'])
def index():
    response = None
    if request.method == 'POST':
        response = {}
        user_input = request.form.get("userInput") 
        if(user_input == None or user_input.strip() == ""):
            response["final_message"] = "Enter the input"
        else:
            opt_prompt = "0"
            prompt = False
            if request.form.get("optPrompt"):
                opt_prompt = "1"
                prompt = True

            controller = KeywordSearchToolController()
            response = controller.run(user_input, opt_prompt)
            LogManager.show(response, False)
            
            response["prompt"] = "NO"
            if prompt:
                response["prompt"] = "YES"
            response["success"] = True
            response["final_message"] = "Result"
            response["user_input"] = user_input


    return render_template("index.html", result=response)


@app.route("/benchmark")
def benchmark(message=""):
    #controller = BenchmarkKeywordsController()
    result = f'Resource not implemented'
    return render_template("index.html", result=result)

