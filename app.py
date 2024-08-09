from flask import Flask, request, render_template

# app
app = Flask(__name__)

# routes and views function
@app.route("/")
def index():
    return render_template("index.html")

# python
if __name__=="__main":
    app.run(debug=True)