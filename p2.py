from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "My Portfolio App is Working!,Project"

if __name__ == "__main__":
    app.run(debug=True)
