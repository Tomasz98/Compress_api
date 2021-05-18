from flask import Flask, request, json
import json
import tools
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/',methods =["POST"])
def hello_world():
    if request.method == 'POST':
        json_data = request.json
        tools.main(json_data)





if __name__ == '__main__':
    app.run()
