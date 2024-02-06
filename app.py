from flask import Flask

app = Flask(__name__)

# Import your modules here
from app.auth import auth
from app.dashboard import dashboard
from app.league import league
from app.player import player
from app.team import team

# Register your blueprints here
app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(league)
app.register_blueprint(player)
app.register_blueprint(team)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
