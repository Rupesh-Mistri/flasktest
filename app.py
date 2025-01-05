from flask import Flask,render_template

app = Flask(__name__)
# app.set_app_details({"title" : "Flask", "version" : "2.3.2"})

@app.route('/')
def index():
    name="Rup"
    return render_template("index.html",name=name)

if __name__=="__main__":
    app.run(debug=True)

