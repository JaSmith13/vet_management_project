from db.run_sql import run_sql
from models.pet import Pet
from models.vet import Vet
from repositories import vet_repository

#Read all
def select_all():
    pets = []
    sql = "SELECT * FROM pets"
    results = run_sql(sql)

    for row in results:
        vet = vet_repository.select(row['vet_id'])
        pet = Pet(row['name'], row['date_of_birth'], row['breed'], row['owner_contact_number'], row['treatment_notes'], vet, row['id'])
        pets.append(pet)
    return pets

#Read one 

#Create 

#Update

#Delete one 

#Delete all