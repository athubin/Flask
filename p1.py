from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello from Flask!</h1><p>This is the home page.</p>"

@app.route('/about')
def about():
    return "<h2>About Page</h2><p>This is a simple Flask example.</p>"

if __name__ == "__main__":
    app.run(debug=True)
