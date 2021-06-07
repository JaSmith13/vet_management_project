from flask import Flask, render_template

from controllers.vets_controller import vets_blueprint
from controllers.pets_controller import pets_blueprint
from controllers.owners_controller import owners_blueprint

app = Flask(__name__)

app.register_blueprint(vets_blueprint)
app.register_blueprint(pets_blueprint)
app.register_blueprint(owners_blueprint)


if __name__ == '__main__':
    app.run()

@app.route("/")
def main():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template(
        "404.html",
        title= "Woops!"
    ), 404
