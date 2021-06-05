import pdb 

from models.vet import Vet
from models.pet import Pet

from repositories import vet_repository, pet_repository


vets = vet_repository.select_all()


for vet in vets:
    print(vet.__dict__)

print(vet_repository.select(2).first_name)

pets = pet_repository.select_all()
for pet in pets:
    print(pet.__dict__)
    print(pet.vet.first_name)

pdb.set_trace()