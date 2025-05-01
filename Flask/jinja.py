from flask import Flask,render_template

app = Flask(__name__)

@app.route("/user/<username>")
def get_user(username):
    return f"hello {username}"

@app.route("/user1/<int:user_id>")
def get_id(user_id):
    return f"ur id {user_id}"

@app.route("/profile/<name>/<int:age>")
def profile(name, age):
    return render_template("profile.html", name=name, age=age)

if __name__ == "__main__":
    app.run(debug=True)