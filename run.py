from flask import Flask

app = Flask("first flask app")

@app.route('/')
def index(): 
    return "<h1>this is the home page.\'OK\'</h1><br><p>there is go then.</p><br>test here<br>{% if loop.index is divisibleby 3 %}{% if loop.index is divisibleby(3) %}"


@app.route('/next')
def next():
    return "this is next page. <br> <a href='/'>click here</a> to go back to home"


@app.route('/data')
def data():
    return "so data source display  will go here. <br> <a href='/'>home</a> | <a href='/next'>next</a> | <a href='/data'>data</a>"


if __name__ == "__main__":
    app.run()
