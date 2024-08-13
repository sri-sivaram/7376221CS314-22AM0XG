from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/get_details')
def get_details():
    return 'SRI SIVARAM A - 7376221CS314'

if __name__ == '__main__':
    app.run(debug=True)
