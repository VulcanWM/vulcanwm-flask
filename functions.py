import os
import pymongo
import dns
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import ssl
from bson.objectid import ObjectId

clientmos = os.getenv("clientm")
clientm = pymongo.MongoClient(clientmos)
newslettersdb = clientm.Newsletters
verificationcol = newslettersdb.Verification
emaillistcol = newslettersdb.EmailList

def checkemaillist(email):
  myquery = { "Email": email }
  mydoc = emaillistcol.find(myquery)
  for x in mydoc:
    return x
  return False

def checkemailverification(email):
  myquery = { "Email": email }
  mydoc = verificationcol.find(myquery)
  for x in mydoc:
    return x
  return False

def searchidveri(theid):
  myquery = {"_id": ObjectId(theid)}
  mydoc = verificationcol.find(myquery)
  for x in mydoc:
    return x
  return False

def searchidsub(theid):
  myquery = {"_id": ObjectId(theid)}
  mydoc = emaillistcol.find(myquery)
  for x in mydoc:
    return x
  return False

def addemail(email):
  veri = checkemailverification(email)
  if veri != False:
    verificationcol.delete_one({"_id": veri['_id']})
  emailcheck = checkemaillist(email)
  if emailcheck != False:
    return "You have already subscribed to VulcanWM's Newsletter!"
  name = email.split("@")[0]
  document = [{
    "Email": email
  }]
  verificationcol.insert_many(document)
  theid = checkemailverification(email)['_id']
  context = ssl.create_default_context()
  MAILPASS = os.getenv("MAIL_PASS")
  MAIL = os.getenv("MAIL")
  html = f"""
    <h1>VulcanWM's Newsletter</h1>
    <p>Hello {name}, you have signed up for VulcanWM's Newsletter!</p>
    <p>Click <a href='https://vulcanwm.is-a.dev/verify/{str(theid)}'>here</a> to verify and be able to recieve VulcanWM's Newsletters!</p>
  """
  message = MIMEMultipart("alternative")
  message["Subject"] = "VulcanWM's Newsletter"
  part2 = MIMEText(html, "html")
  message.attach(part2)
  sendermail = MAIL
  password = MAILPASS
  gmail_server = smtplib.SMTP('smtp.gmail.com', 587)
  gmail_server.starttls(context=context)
  gmail_server.login(sendermail, password)
  message["From"] = sendermail
  message["To"] = email
  gmail_server.sendmail(sendermail, email, message.as_string())
  return "Check your emails and verify your email to start receiving VulcanWM's Newsletters!"

def verifyemail(theid):
  search = searchidveri(theid)
  if search == False:
    return "This is not a valid url!"
  email = search['Email']
  verificationcol.delete_one({"_id": search['_id']})
  document = [{
    "Email": email
  }]
  emaillistcol.insert_many(document)
  context = ssl.create_default_context()
  MAILPASS = os.getenv("MAIL_PASS")
  MAIL = os.getenv("MAIL")
  name = email.split("@")[0]
  html = f"""
    <h1>VulcanWM's Newsletter</h1>
    <p>Hello {name}, you have verified your email and will start receiving VulcanWM's Newsletter!</p>
  """
  message = MIMEMultipart("alternative")
  message["Subject"] = "VulcanWM's Newsletter"
  part2 = MIMEText(html, "html")
  message.attach(part2)
  sendermail = MAIL
  password = MAILPASS
  gmail_server = smtplib.SMTP('smtp.gmail.com', 587)
  gmail_server.starttls(context=context)
  gmail_server.login(sendermail, password)
  message["From"] = sendermail
  message["To"] = email
  gmail_server.sendmail(sendermail, email, message.as_string())
  return "Email verified! You will start receiving VulcanWM's Newsletters!"

def unsubscribe(theid):
  try:
    ObjectId(theid)
  except:
    return "This is not a valid url!"
  search = searchidsub(theid)
  if search == False:
    return "This is not a valid url!"
  emaillistcol.delete_one({"_id": search['_id']})
  return "You have unsubscribed to VulcanWM's Newsletters!"