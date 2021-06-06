from flask import Flask, Blueprint, render_template, request, redirect
from repositories import vet_repository
from models.vet import Vet

vets_blueprint = Blueprint("vets", __name__)

# INDEX
@vets_blueprint.route("/vets")
def all_vets():
    vets = vet_repository.select_all()
    return render_template("vets/index.html", vets=vets)