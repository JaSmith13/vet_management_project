import datetime
from db.run_sql import run_sql
from models.pet import Pet
from models.vet import Vet
from repositories import vet_repository, owner_repository

#Read all
def select_all():
    pets = []
    sql = "SELECT * FROM pets"
    results = run_sql(sql)

    for row in results:
        vet = vet_repository.select(row['vet_id'])
        owner = owner_repository.select(row['owner_id'])
        pet = Pet(row['name'], (row['date_of_birth']).strftime("%d/%m/%Y"), row['breed'], owner, row['treatment_notes'], vet, row['id'])
        pets.append(pet)
    return pets

#Read one 
def select(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values =[id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        vet = vet_repository.select(result['vet_id'])
        owner = owner_repository.select(row['owner_id'])
        pet = Pet(result['name'], (result['date_of_birth']).strftime("%d/%m/%Y"), result['breed'], owner, result['treatment_notes'], vet, result['id'])
    return pet

#Create 
def save(pet):
    sql = "INSERT INTO pets (name, date_of_birth, breed, owner_id, treatment_notes, vet_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [pet.name, pet.date_of_birth, pet.breed, pet.owner.id, pet.treatment_notes, pet.vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id =id

#Update
def update(pet):
    sql = "UPDATE pets SET (name, date_of_birth, breed, owner_id, treatment_notes, vet_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [pet.name, pet.date_of_birth, pet.breed, pet.owner.id, pet.treatment_notes, pet.vet.id, pet.id]
    run_sql(sql, values)

#Delete all
def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)

#Delete one
def delete(id):
    sql = "DELETE FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)