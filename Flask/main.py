from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Hello Rayyan</H1></html>"

@app.route("/home")
def home():
    return "hello Neha"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get("name")
        return f"hello {name}!"
    return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True)