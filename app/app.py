from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! After triggered build"

@app.route("/ci")
def ci_data():
    return "I was built by jenkins and my last commit is : {} done by : {}".format(os.getenv("GIT_COMMIT", "FAILED"), os.getenv("GIT_AUTHOR_NAME", "FAILED"))

app.run("0.0.0.0", port=5000)