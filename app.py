from flask import Flask, render_template, jsonify  # from the module flask theres a class called Flask we're importing
from database import load_jobs_from_db

app = Flask(
  __name__)  # creating object of type Flask class == creating flask appication


@app.route("/")  #html endpoint - register route to the application
def hello_world():
  jobs = load_jobs_from_db()
  return render_template("home.html", jobs=jobs)


# @app.route("/api/jobs")  #json enpoint/api route
#def list_jobs():
#  jobs = load_jobs_from_db()
#  return jsonify(jobs)  # error - TypeError: Object of type Row is not JSON serializable

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
