import pdb 

from models.vet import Vet
from models.pet import Pet
from models.owner import Owner

from repositories import vet_repository, pet_repository, owner_repository


pet_repository.delete_all()
vet_repository.delete_all()
#owner_repository.delete_all()
#vets = vet_repository.select_all()

# pet1 = Pet('Sadie', '10/6/2020', 'scottie cross', '07833 474334', 'N/A', vet_repository.select(1))
# pet_repository.save(pet1)
# for vet in vets:
#     print(vet.__dict__)


#pet_repository.update(pet1)
# print(vet_repository.select(2).first_name)

# pets = pet_repository.select_all()
# for pet in pets:
#     print(pet.__dict__)
#     print(pet.vet.first_name)

new_vet = Vet('Bob', 'Belcher', 'grill cook', '01224 643827')
vet_repository.save(new_vet)

new_vet.first_name = 'Linda'
vet_repository.update(new_vet)

# owner1 = Owner('Bob', 'Barker', '01224 345678', '1 Wheel of fortune road', 'email@definitelyanemailclient.com')
# owner_repository.save(owner1)

# owner1.first_name = 'Robert'
# owner_repository.update(owner1)

pdb.set_trace()