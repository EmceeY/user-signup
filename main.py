import webapp2

import cgi 

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

tem_username = """
<form method="post">
	<label>
		Username:
		<input type="text" name="username"
	</label>
</form>
"""

tem_password = """
<form method="post">
	<label>
		Password:
		<input type="text" name="password"
	</label>
</form>
"""

tem_password_verification = """
<form method="post">
		<label>
		Verify Password:
		<input type="text" name="verify"
	</label>
</form>
"""

tem_email = """
<form method="post">	
	<label>
		E-mail (optional):
		<input type="text" name="email"
	</label>
</form>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$") 	

PASS_RE = re.compile(r"^.{3,20}$")

EMAIL_RE = re.compile(r"^[/S]+@[/S]+.[/S]$")

class Index(webapp2.RequestHandler):
	def get(self):
		submit = "<input type='submit'/>"
		content =  tem_username + "<br>" + tem_password + "<br>" + tem_password_verification + "<br>" +tem_email + "<br>" + submit 
		body = page_header + content + page_footer 
		self.response.write(body)

class Login(webapp2.RequestHandler):
	def post(self):
		username = self.request.get("username")
		pass1 = self.request.get("password")
		pass2 = self.request.get("verify")
		email = self.request.get("email")
		welcome = "Welcome, " + username 
	
	
app = webapp2.WSGIApplication([
	('/', Index)
], debug=True)
