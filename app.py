from flask import Flask, render_template, request, redirect, send_file
from functions import addemail, verifyemail, unsubscribe
from lists import contacts, projects, keywords, description

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')

@app.route("/robots.txt")
def robotstxt():
  return send_file("static/robots.txt")

@app.route('/')
def index():
  return render_template("index.html", description=description, keywords=keywords)

@app.route('/contact')
def contact():
  return render_template("contact.html", contacts=contacts, description=description, keywords=keywords)

@app.route("/projects")
def projects_page():
  return render_template("projects.html", projects=projects, description=description, keywords=keywords)

@app.route("/newsletter")
def newsletterpage():
  return render_template("newsletter.html", description=description, keywords=keywords)

@app.route("/newsletter", methods=['POST', 'GET'])
def newsletterfunc():
  if request.method == 'POST':
    email = request.form['email']
    func = addemail(email)
    return render_template("newsletter.html", msg=func, description=description, keywords=keywords)
  else:
    return redirect("/newsletter")

@app.route("/verify/<theid>")
def verifyfunc(theid):
  func = verifyemail(theid)
  return render_template("newsletter.html", msg=func, description=description, keywords=keywords)

@app.route("/unsubscribe/<theid>")
def unsubscribefunc(theid):
  func = unsubscribe(theid)
  return render_template("newsletter.html", msg=func, description=description, keywords=keywords)