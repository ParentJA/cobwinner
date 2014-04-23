from cobwinner import settings

import json

import os

from prize.models import Prize
from prize.models import PrizeType

import random

import string


PATH = os.path.abspath(os.path.join(os.path.dirname(settings.BASE_DIR), '.'))


def create_prize_types():
    prize_types_path = os.path.join(PATH, 'prize_types.json')

    with open(prize_types_path, 'rt') as prize_types_file:
        data = prize_types_file.read()

    prize_types = json.loads(data)

    for prize_type in prize_types:
        PrizeType.objects.get_or_create(
            name=prize_type.get('name'),
            display_name=prize_type.get('display_name'),
            value=prize_type.get('value')
        )

    print 'Number of prize types: %d' % len(PrizeType.objects.all())


def create_prizes():
    prizes_path = os.path.join(PATH, 'prizes.json')

    with open(prizes_path, 'rt') as prizes_file:
        data = prizes_file.read()

    prizes = json.loads(data)

    for key in prizes.keys():
        print 'Prize type: %s' % key

        num_prizes = int(prizes.get(key))

        print 'Num prizes: %d' % num_prizes

        prize_type = PrizeType.objects.get(name=key)

        for i in range(num_prizes):
            # Generate random code using guidelines...
            code = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(20))

            Prize.objects.create(type=prize_type, code=code)

    print 'Number of prizes: %d' % len(Prize.objects.all())