from flask import Flask
from DAO import dbConnection

app = Flask(__name__)
databaseConnection = dbConnection

@app.route("/")
def hello():
    return "Hello"

@app.route("/test")
def mongoCollection():
    return str(databaseConnection.getCollectionNames())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4321', debug=True)