from flask import Flask

# 1. Define the app variable (Global Scope)
app = Flask(__name__)

# 2. Define a simple route
@app.route('/')
def home():
    return "<h1>It Works! The server is running.</h1>"

# 3. The Critical "Main" Block
# Gunicorn ignores this. Local python runs this.
if __name__ == "__main__":
    app.run(debug=True)
