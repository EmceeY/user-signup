import webapp2

import cgi

import re
global values
values = {'user1': '', 'email2': ''}

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
global username
username = """

		<label>
			Username:
			<input type="text" name="username" value= '{}'>
		</label>
"""

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
"""
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
		
		submit = username.format("") + password + password_verif + email.format("") + button
		body =  page_header + "<form action='/login' method='post'>" + submit + "</form>" + page_footer
		self.response.write(body)

class Login(webapp2.RequestHandler):
	def post(self):
		global values
		username1 = self.request.get("username")
		pass1 = self.request.get("password")
		pass2 = self.request.get("verify")
		email = self.request.get("email")
		welcome = "Welcome, " + username1
		values['user1'] = username1
		values['email2'] = email

		if username1 == "" or USER_RE.match(username1) == None:
			self.redirect("/usererror")

		if PASS_RE.match(pass1) == None:
			self.redirect("/passerror")

		if pass1 != pass2: 
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
		submit = username.format(values['user1']) + "That username is not valid" + password + password_verif + email.format(values['email2'])+ button
		body = page_header + "<form action='/login' method='post'>" + submit + "</form>" + page_footer
		self.response.write(body)

class Email_Error(webapp2.RequestHandler):
	def get(self):
		submit = username.format(values['user1']) + password + password_verif + email.format(values['email2'])+ "That e-mail is not valid" + button
		body = page_header + "<form action='/login' method='post'>" + submit + "</form>" + page_footer
		self.response.write(body)

class Pass_Error(webapp2.RequestHandler):
	def get(self):
		global username
		submit = username.format(values['user1']) + password + "That password is not valid" + password_verif + "That password is not valid" + email.format(values['email2'])+ button
		body = page_header + "<form action='/login' method='post'>" + submit + "</form>" + page_footer
		self.response.write(body)

app = webapp2.WSGIApplication([
	('/', Index),
	('/login', Login),
	('/emailerror', Email_Error),
	('/usererror', User_Error),
	('/passerror', Pass_Error)
], debug=True)
