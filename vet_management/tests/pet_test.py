import unittest

from models.pet import Pet
from models.vet import Vet 

class TestPet(unittest.TestCase):

    def setUp(self):
        self.vet1 = Vet('Aileen', 'Matthews', 'MRCVS', '07865 123456', 1)
        self.pet1 = Pet('Stanley', '01/07/2018', 'cocker spaniel', '07891 654321', 'allergic to meat', self.vet1, 2)
        

    #attribute tests
    def test_pet_has_name(self):
        self.assertEqual('Stanley', self.pet1.name)

    def test_pet_has_date_of_birth(self):
        self.assertEqual('01/07/2018', self.pet1.date_of_birth)

    def test_pet_has_breed(self):
        self.assertEqual('cocker spaniel', self.pet1.breed)

    def test_pet_has_owner_contact_number(self):
        self.assertEqual('07891 654321', self.pet1.owner_contact_number)

    def test_pet_has_treatment_notes(self):
        self.assertEqual('allergic to meat', self.pet1.treatment_notes)

    def test_pet_has_vet(self):
        self.assertEqual('Aileen', self.pet1.vet.first_name)

    def test_pet_can_access_vet_id(self):
        self.assertEqual(1, self.pet1.vet.id)

    def test_pet_has_id(self):
        self.assertEqual(2, self.pet1.id)