import flask
app = flask.Flask(__name__, static_url_path='')

@app.route("/api/qpx/trips/search")
def search():
  date = flask.request.args['date']
  return flask.send_from_directory('eg', 'sfo_to_ord-%s.json' % date)

@app.route("/api/sg/2/events/")
def seatgeek():
  return flask.send_from_directory('eg', 'sg.boston-red-sox-2016-05-03.json')

if __name__ == "__main__":
  app.run(debug=True)
