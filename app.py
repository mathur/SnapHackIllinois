from flask import Flask
from flask_bootstrap import Bootstrap
from bot import HackIllinoisBot

app = Flask(__name__)
Bootstrap(app)
app.config.from_pyfile('config.py')
app.run()

def create_bot():
  bot = HackIllinoisBot(app.config['SNAP_USERNAME'], app.config['SNAP_PASSWORD'])
  bot.listen()
  return bot

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    bot = create_bot()
    bot.listen()
