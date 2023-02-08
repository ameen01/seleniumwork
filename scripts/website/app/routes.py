from app import app
import flask



@app.route("/")
def homepage():
	 return flask.render_template("homepage.html")