from flask import render_template
from flask.ext.mail import Message
from config import ADMINS
from .decorators import async

@async
def send_async_mail(app, msg):
	app.app_context()
	mail.send(msg)

def send_mail(subject, sender, reciepients, text_body, html_body ):
	msg = Message(subject, sender = sender, reciepients = reciepients)
	msg.body = text_body
	msg.html = html_body
	send_async_message(app, msg)
	
def follower_notification(followed, follower):
	send_email("[microblog] %s is started following you" %follower.nickname, ADMINS[0], [followed.email], render_template("follower_email.txt" user = followed, follower = follower), render_template("follower_email.html", user = followed, follower = follower))