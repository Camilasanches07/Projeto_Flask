from flask import Flask, render_template
import pandas as pd 

app = Flask(__name__)


@app.route("/")
def index():
    alunos_csv = pd.read_csv("./data/alunos.csv")
    print(alunos_csv)
    return render_template("index.html", result = alunos_csv)

if __name__ == "__main__":
    app.run(debug=True)
    