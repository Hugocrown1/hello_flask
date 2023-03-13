import json
from flask import Flask
from flask import jsonify


import mysql.connector
app = Flask(__name__)


# Activar el virtual env
# \venv\Scripts\activate.bat

@app.route('/ligamx/equipos')
def get_equipos():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="ligamx"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM ligamx.equipos")

    results = mycursor.fetchall()

    mydb.close()

    return jsonify(results)


@app.route("/")
def main():
    return "HOLA PAMBOLEROS"


@app.route("/bye")
def adios():
    return jsonify(despedida="bye bye")


@app.route("/about")
def about():
    with open("liga.json", "r") as archivo:
        contenido_json = json.load(archivo)
        return json.dumps(contenido_json)


if __name__ == '__main__':
    app.run()
