from collections import OrderedDict

from wazimap.data.utils import get_stat_data

MEAT_RECODES = OrderedDict([
    ('BUFF', 'Water Buffalo'),
    ('CHEVON', 'Goat'),
    ('CHICKEN', 'Chicken'),
    ('DUCK', 'Duck'),
    ('MUTTON', 'Mutton'),
    ('PORK', 'Pork')
])

LIVESTOCK_RECODES = OrderedDict([
    ('BUFFALOES', 'Water Buffalo'),
    ('CATTLE', 'Cattle'),
    ('DUCKS', 'Ducks'),
    ('FOWL', 'Fowl'),
    ('GOATS', 'Goats'),
    ('PIGS', 'Pigs'),
    ('SHEEP', 'Sheep')
])

MILK_ANIMAL_RECODES = OrderedDict([
    ('BUFFALOES', 'Water Buffalo'),
    ('COWS', 'Cows')
])

MILK_RECODES = OrderedDict([
    ('BUFFALO_MILK', 'Water Buffalo Milk'),
    ('COW_MILK', 'Cow Milk')
])


def get_agriculture_profile(geo_code, geo_level, session):
    agriculture_data = {'area_has_data': False}

    if geo_level != 'vdc':

        meat_dist, total_meat = get_stat_data(
            'meat type', geo_level, geo_code, session,
            recode=dict(MEAT_RECODES),
            percent=False,
            order_by='-total')

        livestock_dist, total_livestock = get_stat_data(
            'livestock type', geo_level, geo_code, session,
            recode=dict(LIVESTOCK_RECODES),
            percent=False,
            order_by='-total')

        milk_animal_dist, total_milk_animals = get_stat_data(
            'milk animal type', geo_level, geo_code, session,
            recode=dict(MILK_ANIMAL_RECODES),
            percent=False,
            order_by='-total')

        milk_dist, total_milk = get_stat_data(
            'milk type', geo_level, geo_code, session,
            recode=dict(MILK_RECODES),
            percent=False,
            order_by='-total')

        agriculture_data = dict(
            is_vdc=False,
            area_has_data=True,
            meat_distribution=meat_dist,
            total_meat={
                'name': 'Metric tons of meat produced',
                'values': {'this': total_meat}
            },
            livestock_distribution=livestock_dist,
            total_livestock={
                'name': 'Number of livestock',
                'values': {'this': total_livestock}
            },
            milk_animal_distribution=milk_animal_dist,
            total_milk_animals={
                'name': 'Number of milk animals',
                'values': {'this': total_milk_animals}
            },
            milk_distribution=milk_dist,
            total_milk={
                'name': 'Metric tons of milk',
                'values': {'this': total_milk}
            },
        )

    return agriculture_data
