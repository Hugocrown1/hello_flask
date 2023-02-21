from flask import Flask
app = Flask(__name__)


#Activar el virtual env
#\venv\Scripts\activate.bat


@app.route("/")
def main():
    return "HOLA ITE"


@app.route("/bye")
def adios():
    return "bye bye"
