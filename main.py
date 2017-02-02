import webapp2

import cgi

import re

values = {'user': '', 'email': ''}

page_header = """
<!DOCTYPE html>
<html>
<head>
	<title>Signup</title>
	<style type="text/css">
		.error {
			color: red;
		}
	</style>
</head>
<body>
	<h1>
		<a href="/">Signup</a>
	</h1>
"""

username = """

		<label>
			Username:
			<input type="text" name="username" value= '{}'>
		</label>
""".format(values['user'])
password = """
		<br>
		<label>
			Password:
			<input type="password" name="password" value="">
		</label>
"""
password_verif = """
		<br>
		<label>
			Verify Password:
			<input type="password" name="verify" value="">
		</label>
"""
email = """
		<br>
		<label>
			E-mail (optional):
			<input type="text" name="email" value= '{}'>
		</label>
""".format(values['email'])
button = """
		<br>
			<input type='submit'/>
	</form>

"""

page_footer = """
</body>
</html>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")

PASS_RE = re.compile(r"^.{3,20}$")

EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

class Index(webapp2.RequestHandler):
	def get(self):

		submit = username + password + password_verif + email + button
		body =  page_header + "<form action='/login' method='post'>" + submit + "</form>" + page_footer
		self.response.write(body)

class Login(webapp2.RequestHandler):
	def post(self):
		have_error = False
		username = self.request.get("username")
		pass1 = self.request.get("password")
		pass2 = self.request.get("verify")
		email = self.request.get("email")
		welcome = "Welcome, " + username
		values['user'] = username
		values['email'] = email

		if username == "" or USER_RE.match(username) == None:
			self.redirect("/usererror")

		if PASS_RE.match(pass1) == None:
			self.redirect("/passerror")

		if email !="":
			if EMAIL_RE.match(email) == None:
				self.redirect("/emailerror")
			else:
				self.response.write(welcome)
		else:
			self.response.write(welcome)


class User_Error(webapp2.RequestHandler):
	def get(self):
		submit = username + "That username is not valid" + password + password_verif + email + button
		body = page_header + "<form action='/login' method='post'>" + submit + "</form>" + page_footer
		self.response.write(body)

class Email_Error(webapp2.RequestHandler):
	def get(self):
		submit = username + password + password_verif + email + "That e-mail is not valid" + button
		body = page_header + "<form action='/login' method='post'>" + submit + "</form>" + page_footer
		self.response.write(body)

class Pass_Error(webapp2.RequestHandler):
	def get(self):
		submit = username + password + "That password is not valid" + password_verif + "That password is not valid" + email + button
		body = page_header + "<form action='/login' method='post'>" + submit + "</form>" + page_footer
		self.response.write(body)

app = webapp2.WSGIApplication([
	('/', Index),
	('/login', Login),
	('/emailerror', Email_Error),
	('/usererror', User_Error),
	('/passerror', Pass_Error)
], debug=True)
