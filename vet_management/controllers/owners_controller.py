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