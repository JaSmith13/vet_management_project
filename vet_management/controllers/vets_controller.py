from flask import Flask, Blueprint, render_template, request, redirect
from repositories import vet_repository
from models.vet import Vet

vets_blueprint = Blueprint("vets", __name__)

# INDEX
@vets_blueprint.route("/vets")
def all_vets():
    vets = vet_repository.select_all()
    return render_template("vets/index.html", vets=vets)

#NEW 
@vets_blueprint.route("/vets/new", methods=['GET'])
def new_vet():
    return render_template("vets/new.html")

#CREATE
@vets_blueprint.route("/vets", methods=['POST'])
def create_vet():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    qualifications = request.form["qualifications"]
    contact_number = request.form["contact_number"]

    new_vet = Vet(first_name, last_name, qualifications, contact_number, True)
    vet_repository.save(new_vet)

    return redirect("/vets")

#EDIT
@vets_blueprint.route("/vets/<id>/edit", methods=['GET'])
def edit_vet(id):
    vet = vet_repository.select(id)
    return render_template("vets/edit.html", vet = vet)

#UPDATE