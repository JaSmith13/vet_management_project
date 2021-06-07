import unittest

from models.owner import Owner

class TestOwner(unittest.TestCase):

    def setUp(self):
        self.owner1 = Owner('Bob', 'Barker', '01224 345678', '1 Wheel of fortune road', 'email@definitelyanemailclient.com', 1)

    def test_owner_has_first_name(self):
        self.assertEqual('Bob', self.owner1.first_name)

    def test_owner_has_last_name(self):
        self.assertEqual('Barker', self.owner1.last_name)

    def test_owner_has_telephone_number(self):
        self.assertEqual('01224 345678', self.owner1.contact_number)

    def test_owner_has_address(self):
        self.assertEqual('1 Wheel of fortune road', self.owner1.address)

    def test_owner_has_email(self):
        self.assertEqual('email@definitelyanemailclient.com', self.owner1.email)
