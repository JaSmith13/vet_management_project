from flask import Flask, Blueprint, render_template, redirect, request
from repositories import owner_repository
from models.owner import Owner

owners_blueprint = Blueprint("owners", __name__)

#SHOW
@owners_blueprint.route("/owners/<id>", methods=['GET'])
def single_owner_records(id):
    owner = owner_repository.select(id)
    return render_template("owners/show.html", owner = owner)

#DELETE
@owners_blueprint.route("/owners/<id>/delete", methods=['POST'])
def delete_owner(id):
    owner_repository.delete(id)
    return redirect("/pets")

#NEW
@owners_blueprint.route("/owners/new", methods=['GET'])
def new_owner():
    return render_template("owners/new.html")

#CREATE
@owners_blueprint.route("/owners", methods=['POST'])
def create_owner():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    contact_number = request.form["contact_number"]
    address = request.form["address"]
    email = request.form["email"]
    
    new_owner = Owner(first_name, last_name, contact_number, address, email)
    owner_repository.save(new_owner)

    return redirect("/pets/new")

#EDIT
@owners_blueprint.route("/owners/<id>/edit", methods=['GET'])
def edit_owner(id):
    owner = owner_repository.select(id)
    return render_template("owners/edit.html", owner = owner)

#UPDATE
@owners_blueprint.route("/owners/<id>", methods=['POST'])
def update_owner_details(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    contact_number = request.form["contact_number"]
    address = request.form["address"]
    email = request.form["email"]
    
    owner = Owner(first_name, last_name, contact_number, address, email, id)
    owner_repository.update(owner)

    return redirect("/owners/<id>")

