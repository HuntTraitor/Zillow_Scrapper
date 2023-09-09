from flask import Flask, render_template, jsonify
from src.backend.db import getZipArr

app = Flask(__name__)
app.debug = True

zipGraphs = getZipArr()

@app.route('/')
def home():
    return render_template("index.html", zipGraphs=zipGraphs)

@app.route('/Docs')
def docs():
    return render_template("docs.html")

@app.route('/About')
def about():
    return render_template("about.html")

@app.route('/<zipcode>')
def zipcode_route(zipcode):
    zips = [zipGraphs.rstrip('.png') for zipGraphs in zipGraphs]
    if zipcode not in zips:
        return "Zip-not-found"
    return render_template("zipcode.html", zipcode=zipcode)

#Utility Routes
@app.route('/get_zips')
def get_zips():
    zipGraphs = getZipArr()
    return jsonify(zipGraphs)

if __name__ == "__main__":
    app.run(debug=True)