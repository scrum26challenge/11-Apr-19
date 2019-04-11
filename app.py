rom flask import Flask,render_template,url_for,request,redirect

app = Flask(name)

@app.route("/")
def index():
    return render_template("index.html", values ='')

@app.route("/create",methods=["POST"])
def create():
    sprint = request.form.get("sprint")
    plan = request.form.get("plan")
    code = request.form.get("code")
    review = request.form.get("review")
    retro = request.form.get("retro")
    return render_template("index.html", values = [sprint,plan,code,review,retro])

if name == "main":
    app.run(debug=True)
