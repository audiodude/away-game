import json

import flask
app = flask.Flask(__name__)

TEAM_ABBR = [
  "ari", "atl", "bal", "bos", "chc", "cin", "cle", "col", "cws", "det", "hou",
  "kc", "laa", "lad", "mia", "mil", "min", "nym", "nyy", "oak", "phi", "pit",
  "sd", "sea", "sf", "stl", "tb", "tex", "tor", "was",
]

TEAM_ABBR_AIRPORT_CODE = {
  'atl':    'ATL',
  'bal':    'BWI',
  'bos':    'BOS',
  'chc':    'ORD',
  'cws':    'ORD',
  'cin':    'CVG',
  'cle':    'CLE',
  'tex':    'DAL',
  'col':    'DEN',
  'det':    'DTW',
  'hou':    'IAH',
  'kc':     'MCI',
  'laa':    'LAX',
  'lad':    'LAX',
  'mia':    'MIA',
  'mil':    'MKE',
  'min':    'MSP',
  'nym':    'EWR',
  'nyy':    'EWR',
  'oak':    'OAK',
  'ari':    'PHX',
  'phi':    'PHL',
  'pit':    'PIT',
  'sd':     'SAN',
  'sea':    'SEA',
  'stl':    'STL',
  'tb':     'TPA',
  'tor':    'YYZ',
  'sf':     'SFO',
  'was':    'IAD',
}

AIRPORT_CODE_NAME = {
  'MIA': 'Miami International Airport',
  'ORD': "O'Hare International Airport",
  'LAX': 'Los Angeles International Airport',
  'BWI': 'Baltimore-Washington International Airport',
  'MCI': 'Kansas City International Airport',
  'OAK': 'Oakland International Airport',
  'SFO': 'San Francisco International Airport',
  'YYZ': 'Toronto Pearson International Airport',
  'PIT': 'Pittsburgh International Airport',
  'CVG': 'Cincinnati/Northern Kentucky International Airport',
  'TPA': 'Tampa International Airport',
  'STL': 'Lambert-St. Louis International Airport',
  'BOS': 'Logan International Airport',
  'ATL': 'Hartsfield-Jackson Atlanta International Airport',
  'EWR': 'Newark Liberty International Airport',
  'PHX': 'Phoenix Sky Harbor International Airport',
  'PHL': 'Philadelphia International Airport',
  'IAD': 'Washington Dulles International Airport',
  'SAN': 'San Diego International Airport',
  'DEN': 'Denver International Airport',
  'DAL': 'Dallas Love Field',
  'MKE': 'General Mitchell International Airport',
  'IAH': 'George Bush Intercontinental Airport',
  'MSP': 'Minneapolis-Saint Paul International Airport',
  'SEA': 'Seattle-Tacoma International Airport',
  'CLE': 'Cleveland Hopkins International Airport',
  'DTW': 'Detroit Metropolitan Airport'
}

TEAMS = {
  'teams': [{
    'team': t,
    'airport_code': TEAM_ABBR_AIRPORT_CODE[t],
    'logo': 'logo_%s_79x76.jpg' % t
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

@app.route('/api/local/airports')
def airports():
  return flask.json.jsonify(AIRPORT_CODE_NAME)

@app.route('/')
def index():
  return flask.send_from_directory('templates', 'index.html')

if __name__ == "__main__":
  app.run(debug=True)
