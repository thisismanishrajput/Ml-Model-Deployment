import re
from flask import Flask, render_template, request
import term

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == "POST":
        age = request.form['age']
        premium_predicted = term.premium_prediction(age)
        # print(premium_predicted)
    return render_template("index.html", pp='Predicted Premium should be {}'.format(premium_predicted))


if __name__ == "__main__":
    app.run(debug=True)
