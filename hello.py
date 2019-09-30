from bottle import route, run
import os

@route("/")
def index():
    return "Hello, heroku docker"

if __name__ == "__main__":
    p = 8000
    if "PORT" in os.environ:
        p = os.environ["PORT"]
    run(host='0.0.0.0', port=p)
