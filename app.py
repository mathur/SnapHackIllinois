from flask import Flask
from flask_bootstrap import Bootstrap
from snap import

def create_app():
  app = Flask(__name__)
  Bootstrap(app)
  app.config.from_object('')
  return app

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    create_app().run()
