print("to replace http-server")

from flask import  request, render_template, Flask

app = Flask(__name__)

@app.route("/")
def index():
    return(render_template("index.html"))


if __name__ == "__main__":
    app.run()
