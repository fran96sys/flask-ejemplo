from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("inicio.html")


@app.route("/estudiantes")
def estudiantes():
    lista_estudiantes = [
        {"nombre": "Ana García", "carrera": "Ingeniería de Sistemas", "semestre": 5},
        {"nombre": "Luis Flores", "carrera": "Administración de Empresas", "semestre": 3},
        {"nombre": "María Pérez", "carrera": "Diseño Gráfico", "semestre": 7},
    ]
    return render_template("estudiantes.html", estudiantes=lista_estudiantes)


@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


if __name__ == "__main__":
    app.run(debug=True)
