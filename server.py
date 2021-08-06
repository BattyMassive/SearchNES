from flask import Flask
from flask import render_template, request
import game_db
def sort_games(game):
    return game["title"]["value"]
app = Flask(__name__)
@app.route("/")
def index():
    games = game_db.system_games()
    games.sort(key = sort_games)
    return render_template('index.html',games = games)

@app.route("/game")
@app.template_filter("urlencode")
def game():
    uri = request.args.get("uri")
    game = game_db.game_info(uri)
    return render_template('game.html',game = game)