from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index_page():
    # Return this as a strange
    return render_template("index.html")
    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")
@app.route("/start")
def application_form():
	return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def application_page():
	firstname = request.form.get("first_name")
	lastname = request.form.get("last_name")
	salary = request.form.get("salary")
	position = request.form.get("position")
	return render_template("confirm_application.html", 
							firstname=firstname,
							lastname=lastname,
							salary=salary,
							position=position )


if __name__ == "__main__":
    app.run(debug=True)