from flask import Flask, Blueprint, render_template, request, redirect
from repositories import pet_repository, vet_repository
from models.pet import Pet

pets_blueprint = Blueprint("pets", __name__)

#INDEX
@pets_blueprint.route("/pets", methods=['GET'])
def all_pets():
    pets = pet_repository.select_all()
    return render_template("pets/index.html", pets = pets)

@pets_blueprint.route("/pets/<id>", methods=['GET'])
def single_pet_records(id):
    pet = pet_repository.select(id)
    return render_template("pets/show.html", pet = pet)

#NEW
@pets_blueprint.route("/pets/new", methods=['GET'])
def new_pet():
    vets = vet_repository.select_all()
    return render_template("pets/new.html", vets = vets)

# #CREATE
@pets_blueprint.route("/pets", methods=['POST'])
def create_pet():
    name = request.form["name"]
    date_of_birth = request.form["date_of_birth"]
    breed = request.form["breed"]
    owner_contact_number = request.form["owner_contact_number"]
    treatment_notes = request.form["treatment_notes"]
    vet = vet_repository.select(request.form["vet_id"])

    new_pet = Pet(name, date_of_birth, breed, owner_contact_number, treatment_notes, vet)
    pet_repository.save(new_pet)

    return redirect("/pets")

# #EDIT
@pets_blueprint.route("/pets/<id>/edit", methods=['GET'])
def edit_pet(id):
    pet = pet_repository.select(id)
    vets = vet_repository.select_all()
    return render_template("pets/edit.html", pet = pet, vets = vets)

# #UPDATE
# @pets_blueprint.route("/pets/<id>", methods=['POST'])
# def update_pet_details(id):
#     pass


#DELETE
@pets_blueprint.route("/pets/<id>/delete", methods=['POST'])
def delete_pet(id):
    pet_repository.delete(id)
    return redirect("/pets")
