from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/employees")
def employees():
    return render_template("employees.html")

@app.route("/billing")
def billing():
    return render_template("billing.html")

@app.route("/phishingtool")
def phishingtool():
    return render_template("phishingtool.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/analytics")
def analytics():
    return render_template("analytics.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/pentesting")
def pentesting():
    return render_template("pentesting.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/selectservices")
def selectservices():
    return render_template("selectservices.html")

@app.route("/ToC")
def ToC():
    return render_template("ToC.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)