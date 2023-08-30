from flask import Flask, render_template
from src.backend.db import getZipArr

app = Flask(__name__)

@app.route('/')
def home():
    zipGraphs = getZipArr()
    return render_template("index.html", zipGraphs=zipGraphs)

if __name__ == "__main__":
    app.run(debug=True)