from flask import Flask  # from the module flask theres a class called Flask we're importing

app = Flask(__name__)  # creating object of type Flask class == creating flask appication


@app.route("/") #register route to the application
def hello_world():
  return "Hello World"


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
