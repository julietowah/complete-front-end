from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def index():
  return render_template('index.html')

@app.route("/user")
def about():
  return render_template('about.html')

@app.route("/service")
def service():
  return render_template('service.html')

@app.route("/contact")
def contact():
  return render_template('contact.html')
  
  

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)