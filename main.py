import webapp2

import cgi

import re 

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

page_footer = """
</body>
</html>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$") 	

PASS_RE = re.compile(r"^.{3,20}$")

EMAIL_RE = re.compile(r"^[/S]+@[/S]+.[/S]$")

class Index(webapp2.RequestHandler):
	def get(self):
		submit = """
			<form action="/login" method="post">
				<label>
					Username:
					<input type="text" name="username"
				</label>
				<br>
				<label>
					Password:
					<input type="text" name="password"
				</label>
				<br>
				<label>
					Verify Password:
					<input type="text" name="verify"
				</label>
				<br>
				<label>
					E-mail (optional):
					<input type="text" name="email"
				</label>
				<br>
					<input type='submit'/>
			</form>

"""
		body = page_header + submit + page_footer 
		self.response.write(body)

class Login(webapp2.RequestHandler):
	def post(self):
		username = self.request.get("username")
		pass1 = self.request.get("password")
		pass2 = self.request.get("verify")
		email = self.request.get("email")
		welcome = "Welcome, " + username
		username_error = "That user name was not valid"
		pass_error = "That password is not valid" 
		if USER_RE.match(username) == None:
			self.response.write("That's a bad username there bud")
		elif PASS_RE.match(pass1) == None:
			self.response.write("That password is a mess.")
		if email != "":
			if EMAIL_RE.match(email) == None:
				self.response.write("That e-mail isn't going to work")
			 
			
		#	self.redirect("?/error=" + username_error)	
	#	elif PASS_RE.match(pass1) == false: 
		#	self.redirect("?/error=" + pass_error)
		 
app = webapp2.WSGIApplication([
	('/', Index),
	('/login', Login)
], debug=True)
