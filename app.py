from flask import Flask, render_template, request, jsonify
from tools.webtools.header_extractor import get_http_headers

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_headers', methods=['POST'])
def get_headers():
    url = request.form['url']
    headers = get_http_headers(url)
    return jsonify(headers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

