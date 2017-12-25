from flask import Flask
from flask import jsonify
from flask import request
import json
from flask import render_template
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'historical_data'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/historical_data'
mongo = PyMongo(app)


@app.route('/star', methods=['GET'])
def get_all_stars():
    stars = mongo.db.bitcoin.find()
    output = []
    for star in stars:
        output.append({'Date': star['Date'],
                       # 'High': star['High'],
                       # 'Low': star['Low'],
                       # 'Open': star['Open'],
                       'Close': float(star['Close'])
                       })
    data = json.dumps(output)
    print (data[10],"::::::::::::::")
    return render_template('index.html',
                           results=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
