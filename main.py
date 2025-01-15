from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "name": "eesa"
    }



@app.route("/hello")
def hello():
    return {
        "message": "hello world"
    }


if __name__ == "__main__":
    app.run()
    # app.run(debug=True)