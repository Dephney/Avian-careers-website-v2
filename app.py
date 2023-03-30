from flask import Flask, render_template, jsonify  # from the module flask theres a class called Flask we're importing

app = Flask(
  __name__)  # creating object of type Flask class == creating flask appication

#python list
JOBS = [{
  'id': 1,
  'title': 'Data Scientist',
  'location': 'Durban, South Africa',
  'salary': 'Negotiable'
}, {
  'id': 2,
  'title': 'Backend Engineer',
  'location': 'Cape Town,South Africa',
  'salary': 'R15 000 - R30 000'
}, {
  'id': 3,
  'title': 'Data Analyst',
  'location': 'Remote',
  'salary': 'Negotiable'
}, {
  'id': 4,
  'title': 'Frontend Engineer',
  'location': 'Johannesburg, South Africa',
  'salary': 'Negotiable'
}]


@app.route("/")  #html endpoint - register route to the application
def hello_world():
  return render_template("home.html", jobs=JOBS)

@app.route("/api/jobs")  #json enpoint/api route
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
