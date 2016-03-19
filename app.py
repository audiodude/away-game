import json

import flask
app = flask.Flask(__name__)

TEAM_ABBR = [
  "ari", "atl", "bal", "bos", "chc", "cin", "cle", "col", "cws", "det", "hou",
  "kc", "laa", "lad", "mia", "mil", "min", "nym", "nyy", "oak", "phi", "pit",
  "sd", "sea", "sf", "stl", "tb", "tex", "tor", "was",
]

TEAMS = {
  'teams': [{
    'team': t,
    'logo': 'logo_%s_79x76.jpg' % t,
  } for t in TEAM_ABBR]
}
         
@app.route('/api/qpx/trips/search')
def search():
  date = flask.request.args['date']
  return flask.send_from_directory('static/eg', 'sfo_to_ord-%s.json' % date)

@app.route('/api/sg/2/events/')
def seatgeek():
  return flask.send_from_directory('static/eg',
                                   'sg.boston-red-sox-2016-05-03.json')

@app.route('/api/local/teams')
def teams():
  return flask.json.jsonify(TEAMS)

@app.route('/')
def index():
  return flask.render_template('index.html')

if __name__ == "__main__":
  app.run(debug=True)
