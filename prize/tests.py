from django.test import TestCase

from prize.scripts import create_prizes
from prize.scripts import create_prize_types


class TestRetrieval(TestCase):
    def setUp(self):
        create_prize_types()
        create_prizes()