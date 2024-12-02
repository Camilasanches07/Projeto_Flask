from flask import Flask, render_template
import pandas as pd 

app = Flask(__name__)


@app.route("/")
def index():
    alunos_csv = pd.read_csv("./data/alunos.csv")
    alunos_data = []

    for index, row in alunos_csv.iterrows():#Para percorrer linhas
        alunos_data.append({
            "Identificação do Aluno": row["id_aluno"],
            "Nome": row["nome"],
            "Identificação da Sala": row["salas_id"]
        })
    print(alunos_data)    
    return render_template("index.html", result = alunos_data)


@app.route("/professores")
def professores():
     return render_template("professores.html")

if __name__ == "__main__":
    app.run(debug=True)
    