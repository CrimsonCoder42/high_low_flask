from flask import Flask


app = Flask(__name__)

print(__name__)


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function


@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1> '
            '<p>This is a paragraph</p> '
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>')


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "<p>Bye</p>"


@app.route("/username/<name>")
def greet(name):
    return f"Hello there {name}!"


if __name__ == "__main__":
    app.run(debug=True)

print(f"result{hello_world}" )


