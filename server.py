from flask import Flask

sample = Flask(__name__)

@sample.route("/")
def main():
    return "Página de Prueba"

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5050)
