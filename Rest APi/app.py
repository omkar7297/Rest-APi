from flask import Flask 

app=Flask(__name__)


@app.route("/")
def Welcome():
    return "This is Welcome page"

from controller import user_controller