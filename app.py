import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Bonjour de nouveau!"

@app.route('/how are you')
def hello():
    return 'je suis ok et vous?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
