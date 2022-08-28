from flask import Flask, render_template, request, redirect
from functions import addemail, verifyemail, unsubscribe
app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')
names = ['Munity', 'OvalEyes', 'Drinks Cabin', 'FRANK', 'We Greek', 'Imposter', 'Jasonism', 'BesucheResort', 'What If']
urls = ['https://munity.vulcanwm.repl.co/', 'https://ovaleyes.ovaleyes.repl.co/', 'https://drinks-cabin.vulcanwm.repl.co/', 'https://frank.vulcanwm.repl.co/', 'https://wegreek.vulcanwm.repl.co/', 'https://imposter.vulcanwm.repl.co/', 'https://jasonism.vulcanwm.repl.co/', 'https://BesucheResort.vulcanwm.repl.co/', 'https://what-if.vulcanwm.repl.co']
descriptions = ['a music related game', 'a social media website', 'a game in which you have your own drinks company', 'a multi-purpose website', 'a greek mythology wikipedia', 'guess who is the imposter in your online lesson', 'make your block as mighty as the immortal block of wood god Jason', 'virtual resort where you search for money', 'a website where you will face hypothetical scenarios']
numbers = [0,1,2,3,4,5,6,7,8]

@app.route('/')
def index():
  return render_template("index.html")

@app.route("/projects")
def projects():
  return render_template("projects.html", names=names, urls=urls, descriptions=descriptions, numbers=numbers)

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