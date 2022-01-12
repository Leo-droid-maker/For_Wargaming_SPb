import pytest
from create_and_fill_db import WarGamingDatabase
from random import choice, randint
import os


@pytest.fixture(scope='session')
def setup_database():
    """
    Fixture that creates a test database, fill it with data from main DB and randomly change parameters
    in test DB. Returns the list of dicts that can be easily to test using keys.
    After test will be done, test DB will be destroyed.
    :return: list(dict())
    """
    test_database = WarGamingDatabase('test_data_base')
    main_database = WarGamingDatabase('main_data_base')

    main_engines_table_results = main_database.engines_list()

    for engine in main_engines_table_results:

        test_database.add_engine(engine[0], engine[1], engine[2])

        rand_engine_component_number = randint(1, 2)
        randomized_engine = test_database.session.query(WarGamingDatabase.Engines).filter_by(engine=engine[0]).first()

        if rand_engine_component_number == 1:
            randomized_engine.power = randint(1, 20)
        elif rand_engine_component_number == 2:
            randomized_engine.type = randint(1, 20)

    main_hulls_table_results = main_database.hulls_list()

    for hull in main_hulls_table_results:

        test_database.add_hull(hull[0], hull[1], hull[2], hull[3])

        rand_hull_component_number = randint(1, 3)
        randomized_hull = test_database.session.query(WarGamingDatabase.Hulls).filter_by(hull=hull[0]).first()

        if rand_hull_component_number == 1:
            randomized_hull.armor = randint(1, 20)
        elif rand_hull_component_number == 2:
            randomized_hull.type = randint(1, 20)
        elif rand_hull_component_number == 3:
            randomized_hull.capacity = randint(1, 20)

    main_weapons_table_results = main_database.weapons_list()

    for weapon in main_weapons_table_results:

        test_database.add_weapon(weapon[0], weapon[1], weapon[2], weapon[3], weapon[4], weapon[5])

        rand_weapon_component_number = randint(1, 5)
        randomized_weapon = test_database.session.query(WarGamingDatabase.Weapons).filter_by(weapon=weapon[0]).first()

        if rand_weapon_component_number == 1:
            randomized_weapon.reload_speed = randint(1, 20)
        elif rand_weapon_component_number == 2:
            randomized_weapon.rotation_speed = randint(1, 20)
        elif rand_weapon_component_number == 3:
            randomized_weapon.diameter = randint(1, 20)
        elif rand_weapon_component_number == 4:
            randomized_weapon.power_volley = randint(1, 20)
        elif rand_weapon_component_number == 5:
            randomized_weapon.count = randint(1, 20)

    main_ships_table_results = main_database.ships_list()

    for ship in main_ships_table_results:

        random_ship_component = choice((ship[1], ship[2], ship[3]))

        if random_ship_component.startswith('Weapon'):
            test_database.add_ship(ship[0], f'Weapon_{randint(1, 20)}', ship[2], ship[3])
        elif random_ship_component.startswith('Hull'):
            test_database.add_ship(ship[0], ship[1], f'Hull_{randint(1, 5)}', ship[3])
        elif random_ship_component.startswith('AB'):
            test_database.add_ship(ship[0], ship[1], ship[2], f'AB-{randint(1, 6)}')

    ships_from_main = main_database.get_all_ships_data()
    ships_from_test = test_database.get_all_ships_data()

    yield ships_from_main, ships_from_test
    main_database.session.close()
    test_database.session.close()
    os.remove('test_data_base.db3')
