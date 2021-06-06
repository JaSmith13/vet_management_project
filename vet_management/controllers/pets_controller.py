from flask import Flask, Blueprint, render_template, request, redirect
from repositories import pet_repository, vet_repository
from models.pet import Pet

pets_blueprint = Blueprint("pets", __name__)

# INDEX
@pets_blueprint.route("/pets")
def all_pets():
    pets = pet_repository.select_all()
    return render_template("pets/index.html", pets=pets)