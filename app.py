from flask import Flask, request
app = Flask(__name__)

@app.route('/add/<first>/<second>')
def add(first, second):
    return {
        "result": int(first) + int(second)
    }

@app.route("/multiply/<first>/<second>")
def multiply(first, second):
    try:
        result = int(first) * int(second)
    except Exception as e:
        result = "Err"
    return {
        "result": result
    }

"""
    Accepts several numbers for addition
"""
@app.route("/add", methods=["POST"])
def addMany():
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