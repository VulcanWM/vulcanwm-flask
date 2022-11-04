from flask import Flask, render_template, request, redirect
from functions import addemail, verifyemail, unsubscribe
from lists import contacts, projects

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/contact')
def contact():
  return render_template("contact.html", contacts=contacts)

@app.route("/projects")
def projects_page():
  return render_template("projects.html", projects=projects)

@app.route("/newsletter")
def newsletterpage():
  return render_template("newsletter.html")

@app.route("/newsletter", methods=['POST', 'GET'])
def newsletterfunc():
  if request.method == 'POST':
    email = request.form['email']
    func = addemail(email)
    return render_template("error.html", error=func)
  else:
    return redirect("/newsletter")

@app.route("/verify/<theid>")
def verifyfunc(theid):
  func = verifyemail(theid)
  return render_template("error.html", error=func)

@app.route("/unsubscribe/<theid>")
def unsubscribefunc(theid):
  func = unsubscribe(theid)
  return render_template("error.html", error=func)