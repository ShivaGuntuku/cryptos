from flask import Flask
# from flask import jsonify
# from flask import request
# import json
from flask import render_template
from flask_pymongo import PyMongo
from utils import get_coins


app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'historical_data'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/historical_data'
mongo = PyMongo(app)


# @app.route('/star', methods=['GET'])
# def get_all_stars():
#     stars = mongo.db.bitcoin.find()
#     output = []
#     i = 1
#     for star in stars:
#         output.append({'Date': i,
#                        # 'High': star['High'],
#                        # 'Low': star['Low'],
#                        # 'Open': star['Open'],
#                        'Close': float(star['Close'])
#                        })
#         i += 1
#     data = json.dumps(output)
#     return render_template('index.html',
#                            results=data)


@app.route('/')
def test():
    url = 'https://api.coinmarketcap.com/v1/ticker/?limit=10'
    results = get_coins(url)
    return render_template('index.html', results=results)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
