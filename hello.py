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


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def create_blog_post(user, title, content):
    if user.is_logged_in:
        print(f"This is {user.name}'s new blog post: {title} {content}")
    else:
        print("User must be logged in!")


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0], args[1], args[2])
    return wrapper


new_user = User("Angela")
new_user.is_logged_in = True
create_blog_post(new_user, "Hello", "This is my first post")
