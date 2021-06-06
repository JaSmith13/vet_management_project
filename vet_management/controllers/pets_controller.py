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
# @pets_blueprint("/pets/new", methods=['GET'])
# def new_pet():
#     vets = vet_repository.select_all()
#     return render_template("pets/new.html", vets = vets)

# #CREATE
# @pets_blueprint.route("/pets", methods=['POST'])
# def create_pet():
#     pass

# #EDIT
# @pets_blueprint.route("/pets/<id>/edit", methods=['GET'])
# def edit_pet(id):
#     pass

# #UPDATE
# @pets_blueprint.route("/pets/<id>", methods=['POST'])
# def update_pet_details(id):
#     pass


#DELETE
@pets_blueprint.route("/pets/<id>/delete", methods=['POST'])
def delete_pet(id):
    pet_repository.delete(id)
    return redirect("/pets")
