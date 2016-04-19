from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_game_form():
    """Route to the game"""

    response = request.args.get("play-game")
    if response == 'yes':
        return render_template("game.html")

    else:
        return render_template("goodbye.html")

@app.route('/madlib')
def show_mad_lib():

    proper_noun = request.args.get("teacher")
    thing = request.args.get("noun")
    hue = request.args.get("color")
    descriptor = request.args.get("adjective")

    return render_template("madlib.html",
                            teacher=proper_noun,
                            noun=thing,
                            color=hue,
                            adjective=descriptor)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)