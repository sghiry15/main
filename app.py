from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello depuis Azure App Service avec Python sans installation locale !"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
