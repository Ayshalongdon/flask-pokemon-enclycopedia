from flask import Flask


app = Flask(__name__)


@app.get("/")
def pokemon_list():
    return "Charmander, Pikachu, Eevee, Bulbasaur, Diglett"


@app.get("/cgiharmander")
def charmander_data():
    return "This is Charmander, a generation 1 pokemon who's main element is fire!"


@app.get("/bulbasaur")
def bulbasaur_data():
    return "This is Bulbasaur, a generation 1 pokemon who's looks like a little dinsoaur!"


@app.get("/pikachu")
def pikachu_data():
    return "This is Pikachu, a generation 1 pokemon who's looks like a little rabbit!"


@app.get("/eevee")
def eevee_data():
    return "This is Eevee, a generation 1 pokemon who's looks like a little fox!"


@app.get("/diglett")
def diglett_data():
    return "This is Diglett, a generation 1 pokemon who's looks like a little mole!"




if __name__ == "__main__":
    app.run()