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

@app.route('/madlib', methods=["GET", "POST"])
def show_mad_lib():
    if request.method == 'POST':
        proper_noun = request.form.get("teacher")
        thing = request.form.get("noun")
        hue = request.form.get("color")
        descriptor = request.form.get("adjective")
        adverbs = request.form.getlist("adverb")
        if adverbs == []:
            verb_descriptor = "[Please use your browser's back button to choose at least one adverb.]"
        elif len(adverbs) == 1:
            verb_descriptor = adverbs[0]
        else:
            verb_descriptor = ""
            for word in adverbs:
                verb_descriptor += word + ", "
        template_choice = choice(["madlib.html", "madlib2.html", "madlib3.html"])

        return render_template(template_choice,
                                teacher=proper_noun,
                                noun=thing,
                                color=hue,
                                adjective=descriptor, 
                                adverb=verb_descriptor)

    else:
        return "Are you sure?"


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
