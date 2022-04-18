from Flask import flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("basicprofile.html")

if __name__=="__main__":
    app.run(debug=True)