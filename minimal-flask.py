from flask import Flask

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'pongers'

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
