from flask import Flask, jsonify, request
from data import data

app= Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data":data,
        "Message":"Successful"
    }), 200

@app.route("/planet") 
def planet():
    name=request.args.get("name")
    planet_data=next(item for item in data if item["name"] == name)
    return jsonify({
        "data":planet_data,
        "Message":"Successful"
    })   

    
if(__name__=="__main__"):
    app.run(debug=True)

#http://127.0.0.1:5000/planet?name=51%20Pegasi%20b