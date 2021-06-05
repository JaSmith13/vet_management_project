import pdb 

from models.vet import Vet
from models.pet import Pet

from repositories import vet_repository, pet_repository


pet_repository.delete_all()
#vet_repository.delete_all()
#vets = vet_repository.select_all()

pet1 = Pet('Sadie', '10/6/2020', 'scottie cross', '07833 474334', 'grumbler extraordinaire', vet_repository.select(1))
pet_repository.save(pet1)
# for vet in vets:
#     print(vet.__dict__)
pet1.name = 'Douglas'
pet_repository.update(pet1)
# print(vet_repository.select(2).first_name)

pets = pet_repository.select_all()
for pet in pets:
    print(pet.__dict__)
    print(pet.vet.first_name)

#print(pet_repository.select(1).name)

pdb.set_trace()