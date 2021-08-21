# import libraries
from flask import Flask, request

# starts our main server
def create_app():
    app = Flask(__name__)

    # simple route that combines two values
    @app.route('/add/<first>/<second>')
    def add(first, second):
        return {
            "result": int(first) + int(second)
        }

    # simple route multiplying two values
    @app.route("/multiply/<first>/<second>")
    def multiply(first, second):
        try:
            result = int(first) * int(second)
        except Exception as e:
            result = "Err"
        return {
            "result": result
        }

    # can add an array of values
    @app.route("/add", methods=["POST"])
    def add_many():
        values = request.get_json()
        result = 0
        try:
            for value in values["values"]:
                result += value
        except Exception as e:
            result = "Err"
        return {
            "result": result
        }

    # multiplies an array of values
    @app.route("/multiply", methods=["POST"])
    def multiply_many():
        values = request.get_json()
        result = 1
        try:
            for value in values["values"]:
                result *= value
        except Exception as e:
            result = "Err"
        return {
            "result": result
        }
    
    return app;