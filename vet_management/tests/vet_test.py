import unittest

from models.vet import Vet

class TestVet(unittest.TestCase):

    def setUp(self):
        self.vet1 = Vet('Aileen', 'Matthews', 'MRCVS', '07865 123456', 1)

    #attribute tests
    def test_vet_has_first_name(self):
        self.assertEqual('Aileen', self.vet1.first_name)

    def test_vet_has_last_name(self):
        self.assertEqual('Matthews', self.vet1.last_name)

    def test_vet_has_qualifications(self):
        self.assertEqual('MRCVS', self.vet1.qualfications)

    def test_vet_has_contact_number(self):
        self.assertEqual('07865 123456', self.vet1.contact_number)

    def test_vet_has_id(self):
        self.assertEqual(1, self.vet1.id)