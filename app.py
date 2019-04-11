from flask import Flask,render_template,url_for,request,redirect
import time

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", values ='', meeting = '', timer='')

@app.route("/create",methods=["POST"])
def create():
	sprint = request.form.get("sprint")
	plan = request.form.get("plan")
	code = request.form.get("code")
	review = request.form.get("review")
	retro = request.form.get("retro")
	for item in  ['Planning Meeting','Code Meeting','Review Meeting','Retro Meeting']:		
		meeting = item
		if meeting == 'Planning Meeting': 
			duration = int(plan) 
		elif meeting == 'Code Meeting':
			duration = int(code)
		elif meeting == 'Review Meeting':
			duration = int(review)
		elif meeting == 'Retro Meeting':
			duration = int(retro)

		return render_template("index.html", values = sprint, meeting = meeting, timer=duration)


if __name__ == "__main__":
	app.run(debug=True)
