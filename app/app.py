from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# @app.route("/ci")
# def ci_data():
#     return "I was built by jenkins and my last commit is : {} running on node: {}".format(os.getenv("GIT_COMMIT", "FAILED"), os.getenv("GIT_BRANCH", "FAILED"))

app.run("0.0.0.0", port=5000)