from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/internships")
def internships():
    conn = get_db()
    jobs = conn.execute("SELECT * FROM internships").fetchall()
    conn.close()
    return render_template("internships.html", jobs=jobs)

@app.route("/apply/<int:id>", methods=["GET","POST"])
def apply(id):
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]

        conn=get_db()
        conn.execute(
            "INSERT INTO applications(name,email,internship_id) VALUES(?,?,?)",
            (name,email,id)
        )
        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("apply.html")

if __name__=="__main__":
    app.run(debug=True)
    