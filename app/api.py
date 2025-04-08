from flask import Flask, jsonify, render_template
from app.database import fetch_data, create_table
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


@app.route('/api/reads')
def get_data():
    db_date = fetch_data(20)
    data = [
        {
            "id": id,
            "temperature": temp,
            "humidity": humid,
            "timestamp": ts,
        }
        for id, temp, humid, ts in db_date
    ]
    return jsonify(data)


@app.route('/')
def index():
    rows = fetch_data(limit=50)
    result = [{
        "id": row[0],
        "temperature": row[1],
        "humidity": row[2],
        "timestamp": row[3]
    } for row in rows]
    return render_template('index.html', data=result)


if __name__ == "__main__":
    create_table()
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    port = int(os.getenv('FLASK_RUN_PORT', 5000))
    app.run(host="0.0.0.0", port=port, debug=debug)
