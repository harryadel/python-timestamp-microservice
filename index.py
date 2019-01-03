from flask import Flask
import time
import numbers
import json
app = Flask(__name__)


@app.route('/api/timestamp/<unix>')
def timestamp(unix):
    try:
        return json.dumps({'utc': time.ctime(int(unix)), 'unix': unix})
    except ValueError:
        return json.dumps({'error': 'Invalid Date'})


if __name__ == "__main__":
    app.run()
