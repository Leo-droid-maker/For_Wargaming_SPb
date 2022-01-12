import pytest


@pytest.mark.parametrize('i', (range(0, 200)))
def test_ships_weapons(i, setup_database):
    ship_1, ship_2 = setup_database

    ship_1_weapon = ship_1[i]['weapon']
    ship_2_weapon = ship_2[i]['weapon']

    reload_speed_message = f'{ship_2[i]["ship"]}, {ship_2_weapon["weapon"]}\n' \
                           f'reload speed:\nexpected {ship_1_weapon["reload_speed"]}\n' \
                           f'was {ship_2_weapon["reload_speed"]}'

    rotation_speed_message = f'{ship_2[i]["ship"]}, {ship_2_weapon["weapon"]}\n' \
                             f'rotation speed:\nexpected {ship_1_weapon["rotation_speed"]}\n' \
                             f'was {ship_2_weapon["rotation_speed"]}'

    diameter_message = f'{ship_2[i]["ship"]}, {ship_2_weapon["weapon"]}\n' \
                       f'diameter:\nexpected {ship_1_weapon["diameter"]}\n' \
                       f'was {ship_2_weapon["diameter"]}'

    power_volley_message = f'{ship_2[i]["ship"]}, {ship_2_weapon["weapon"]}\n' \
                           f'power volley:\nexpected {ship_1_weapon["power_volley"]}\n' \
                           f'was {ship_2_weapon["power_volley"]}'

    count_message = f'{ship_2[i]["ship"]}, {ship_2_weapon["weapon"]}\n' \
                    f'count:\nexpected {ship_1_weapon["count"]}\n' \
                    f'was {ship_2_weapon["count"]}'

    weapon_message = f'{ship_2[i]["ship"]}, {ship_2_weapon["weapon"]}\n' \
                     f'weapon:\nexpected {ship_1_weapon["weapon"]}\n' \
                     f'was {ship_2_weapon["weapon"]}'

    if ship_1_weapon['weapon'] == ship_2_weapon['weapon']:
        assert ship_1_weapon['reload_speed'] == ship_2_weapon['reload_speed'], reload_speed_message

        assert ship_1_weapon['rotation_speed'] == ship_2_weapon['rotation_speed'], rotation_speed_message

        assert ship_1_weapon['diameter'] == ship_2_weapon['diameter'], diameter_message

        assert ship_1_weapon['power_volley'] == ship_2_weapon['power_volley'], power_volley_message

        assert ship_1_weapon['count'] == ship_2_weapon['count'], count_message

    assert ship_1_weapon['weapon'] == ship_2_weapon['weapon'], weapon_message


@pytest.mark.parametrize('i', (range(0, 200)))
def test_ships_hulls(i, setup_database):
    ship_1, ship_2 = setup_database

    print()

    ship_1_hull = ship_1[i]['hull']
    ship_2_hull = ship_2[i]['hull']

    hull_message = f'{ship_2[i]["ship"]}, {ship_2_hull["hull"]}\n' \
                   f'hull:\nexpected {ship_1_hull["hull"]}\n' \
                   f'was {ship_2_hull["hull"]}'

    armor_message = f'{ship_2[i]["ship"]}, {ship_2_hull["hull"]}\n' \
                    f'armor:\nexpected {ship_1_hull["armor"]}\n' \
                    f'was {ship_2_hull["armor"]}'

    type_message = f'{ship_2[i]["ship"]}, {ship_2_hull["hull"]}\n' \
                   f'type:\nexpected {ship_1_hull["type"]}\n' \
                   f'was {ship_2_hull["type"]}'

    capacity_message = f'{ship_2[i]["ship"]}, {ship_2_hull["hull"]}\n' \
                       f'capacity:\nexpected {ship_1_hull["capacity"]}\n' \
                       f'was {ship_2_hull["capacity"]}'

    if ship_1_hull['hull'] == ship_2_hull['hull']:
        assert ship_1_hull['armor'] == ship_2_hull['armor'], armor_message

        assert ship_1_hull['type'] == ship_2_hull['type'], type_message

        assert ship_1_hull['capacity'] == ship_2_hull['capacity'], capacity_message

    assert ship_1_hull['hull'] == ship_2_hull['hull'], hull_message


@pytest.mark.parametrize('i', (range(0, 200)))
def test_ships_engines(i, setup_database):
    ship_1, ship_2 = setup_database

    print()

    ship_1_engine = ship_1[i]['engine']
    ship_2_engine = ship_2[i]['engine']

    engine_message = f'{ship_2[i]["ship"]}, {ship_2_engine["engine"]}\n' \
                     f'engine:\nexpected {ship_1_engine["engine"]}\n' \
                     f'was {ship_2_engine["engine"]}'

    power_message = f'{ship_2[i]["ship"]}, {ship_2_engine["engine"]}\n' \
                    f'power:\nexpected {ship_1_engine["power"]}\n' \
                    f'was {ship_2_engine["power"]}'

    type_message = f'{ship_2[i]["ship"]}, {ship_2_engine["engine"]}\n' \
                   f'type:\nexpected {ship_1_engine["type"]}\n' \
                   f'was {ship_2_engine["type"]}'

    if ship_1_engine['engine'] == ship_2_engine['engine']:
        assert ship_1_engine['power'] == ship_2_engine['power'], power_message

        assert ship_1_engine['type'] == ship_2_engine['type'], type_message

    assert ship_1_engine['engine'] == ship_2_engine['engine'], engine_message
