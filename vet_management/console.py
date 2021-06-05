import pdb 

from models.vet import Vet
from repositories import vet_repository

from models.pet import Pet

vets = vet_repository.select_all()

for vet in vets:
    print(vet.__dict__)

print(vet_repository.select(2).first_name)

pdb.set_trace()