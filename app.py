from flask import Flask, request, render_template_string
import pandas as pd
import numpy as np
import re
import os

app = Flask(__name__)

HTML_FORM = """
<h2>TOPSIS Web Service</h2>
<form method="POST" enctype="multipart/form-data">
  Input CSV: <input type="file" name="file"><br><br>
  Weights (comma-separated): <input type="text" name="weights"><br><br>
  Impacts (+ or -): <input type="text" name="impacts"><br><br>
  Email ID: <input type="text" name="email"><br><br>
  <input type="submit">
</form>
<p>{{ message }}</p>
"""

def run_topsis(df, weights, impacts):
    data = df.iloc[:, 1:].values
    weights = list(map(float, weights.split(',')))
    impacts = impacts.split(',')

    norm = np.sqrt((data ** 2).sum(axis=0))
    norm_data = data / norm
    weighted = norm_data * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted[:, i].max())
            ideal_worst.append(weighted[:, i].min())
        else:
            ideal_best.append(weighted[:, i].min())
            ideal_worst.append(weighted[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)

    df["Topsis Score"] = score
    df["Rank"] = df["Topsis Score"].rank(ascending=False).astype(int)
    return df

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        file = request.files.get("file")
        weights = request.form.get("weights")
        impacts = request.form.get("impacts")
        email = request.form.get("email")

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return render_template_string(HTML_FORM, message="Invalid email format")

        df = pd.read_csv(file)

        if len(weights.split(',')) != len(impacts.split(',')):
            return render_template_string(HTML_FORM, message="Weights and impacts count mismatch")

        result = run_topsis(df, weights, impacts)
        result.to_csv("result.csv", index=False)

        message = "TOPSIS executed successfully. Result generated."

    return render_template_string(HTML_FORM, message=message)

if __name__ == "__main__":
    app.run(debug=True)
