from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'helo world!'

@app.route('/vstring/<name>')
def vstring(name):
    return f'Hello {name}!'

@app.route('/vint/<int:age>')
def vint(age):
    return f'You are {age} years old.'

if __name__ == '__main__':
    app.run(debug=True)