from sqlalchemy import create_engine, Column, Integer, Text, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class WarGamingDatabase:
    """
    Main Database Class with declarative style of SQlAlchemy.
    Contains a few methods to access and get the data.
    """
    Base = declarative_base()

    class Ships(Base):
        __tablename__ = 'ships'
        ship = Column(Text, primary_key=True)
        weapon = Column(ForeignKey('weapons.weapon'))
        hull = Column(ForeignKey('hulls.hull'))
        engine = Column(ForeignKey('engines.engine'))

        def __init__(self, ship, weapon, hull, engine):
            self.ship = ship
            self.weapon = weapon
            self.hull = hull
            self.engine = engine

    class Weapons(Base):
        __tablename__ = 'weapons'
        weapon = Column(Text, primary_key=True)
        reload_speed = Column(Integer)
        rotation_speed = Column(Integer)
        diameter = Column(Integer)
        power_volley = Column(Integer)
        count = Column(Integer)

        def __init__(self, weapon, reload_speed, rotation_speed, diameter, power_volley, count):
            self.weapon = weapon
            self.reload_speed = reload_speed
            self.rotation_speed = rotation_speed
            self.diameter = diameter
            self.power_volley = power_volley
            self.count = count

    class Hulls(Base):
        __tablename__ = 'hulls'
        hull = Column(Text, primary_key=True)
        armor = Column(Integer)
        type = Column(Integer)
        capacity = Column(Integer)

        def __init__(self, hull, armor, type, capacity):
            self.hull = hull
            self.armor = armor
            self.type = type
            self.capacity = capacity

    class Engines(Base):
        __tablename__ = 'engines'
        engine = Column(Text, primary_key=True)
        power = Column(Integer)
        type = Column(Integer)

        def __init__(self, engine, power, type):
            self.engine = engine
            self.power = power
            self.type = type

    def __init__(self, db_name):
        self.engine = create_engine(f'sqlite:///{db_name}.db3', echo=False, pool_recycle=7200)
        self.Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.session.commit()

    def add_engine(self, engine, power, type):
        """
        Method to add an engine to database
        :param engine: str
        :param power: int
        :param type: int
        """
        engine = self.Engines(engine, power, type)
        self.session.add(engine)
        self.session.commit()

    def add_hull(self, hull, armor, type, capacity):
        """
        Method to add a hull to database
        :param hull: str
        :param armor: int
        :param type: int
        :param capacity: int
        :return:
        """
        hull = self.Hulls(hull, armor, type, capacity)
        self.session.add(hull)
        self.session.commit()

    def add_weapon(self, weapon, reload_speed, rotation_speed, diameter, power_volley, count):
        """
        Method to add a weapon to database
        :param weapon: str
        :param reload_speed: int
        :param rotation_speed: int
        :param diameter: int
        :param power_volley: int
        :param count: int
        """
        weapon = self.Weapons(weapon, reload_speed, rotation_speed, diameter, power_volley, count)
        self.session.add(weapon)
        self.session.commit()

    def add_ship(self, ship_name, weapon_name, hull_name, engine_name):
        """
        Method to add a ship to database
        :param ship_name: str
        :param weapon_name: str
        :param hull_name: str
        :param engine_name: str
        """
        weapon = self.session.query(self.Weapons).filter_by(weapon=weapon_name).first().weapon
        hull = self.session.query(self.Hulls).filter_by(hull=hull_name).first().hull
        engine = self.session.query(self.Engines).filter_by(engine=engine_name).first().engine

        ship = self.Ships(ship_name, weapon, hull, engine)
        self.session.add(ship)
        self.session.commit()

    def ships_list(self):
        """
        Returns a list of ships from database
        :return: list
        """
        query = self.session.query(
            self.Ships.ship,
            self.Ships.weapon,
            self.Ships.hull,
            self.Ships.engine
        )
        return query.all()

    def weapons_list(self):
        """
        Returns a list of weapons from database
        :return: list
        """
        query = self.session.query(
            self.Weapons.weapon,
            self.Weapons.reload_speed,
            self.Weapons.rotation_speed,
            self.Weapons.diameter,
            self.Weapons.power_volley,
            self.Weapons.count
        )
        return query.all()

    def hulls_list(self):
        """
        Returns a list of hulls from database
        :return: list
        """
        query = self.session.query(
            self.Hulls.hull,
            self.Hulls.armor,
            self.Hulls.type,
            self.Hulls.capacity
        )
        return query.all()

    def engines_list(self):
        """
        Returns a list of engines from database
        :return: list
        """
        query = self.session.query(
            self.Engines.engine,
            self.Engines.power,
            self.Engines.type,
        )
        return query.all()

    def get_all(self):
        """
        Returns a list of query results with all ships
        :return: list
        """
        query = self.session.query(
            self.Ships.ship,
            self.Ships.weapon,
            self.Weapons.reload_speed,
            self.Weapons.rotation_speed,
            self.Weapons.diameter,
            self.Weapons.power_volley,
            self.Weapons.count,
            self.Ships.hull,
            self.Hulls.armor,
            self.Hulls.type,
            self.Hulls.capacity,
            self.Ships.engine,
            self.Engines.power,
            self.Engines.type,
        ).join(self.Weapons, self.Hulls, self.Engines)
        return query.all()

    def get_all_ships_data(self):
        """
        Processes self.get_all() method to create list of dicts that can be used in the future
        for example to transfer data in json.
        Returns usefully structure that can be tested easily (easy access to data using keys)
        :return: list(dict())
        """
        ships_list = self.get_all()

        result_all_ships = []

        for i in range(len(ships_list)):
            ships = {}
            ships['ship'] = ships_list[i][0]
            ships['weapon'] = {'weapon': ships_list[i][1],
                               'reload_speed': ships_list[i][2],
                               'rotation_speed': ships_list[i][3],
                               'diameter': ships_list[i][4],
                               'power_volley': ships_list[i][5],
                               'count': ships_list[i][6]
                               }
            ships['hull'] = {'hull': ships_list[i][7],
                             'armor': ships_list[i][8],
                             'type': ships_list[i][9],
                             'capacity': ships_list[i][10]
                             }
            ships['engine'] = {'engine': ships_list[i][11],
                               'power': ships_list[i][12],
                               'type': ships_list[i][13]
                               }

            result_all_ships.append(ships)

        return result_all_ships


if __name__ == '__main__':
    # Fill main DB here
    import random

    db = WarGamingDatabase('main_data_base')

    for i in range(1, 21):
        db.add_weapon(
            f'Weapon_{i}',
            random.randint(1, 20),
            random.randint(1, 20),
            random.randint(1, 20),
            random.randint(1, 20),
            random.randint(1, 20)
        )
    for i in range(1, 6):
        db.add_hull(
            f'Hull_{i}',
            random.randint(1, 20),
            random.randint(1, 20),
            random.randint(1, 20)
        )
    for i in range(1, 7):
        db.add_engine(
            f'AB-{i}',
            random.randint(1, 20),
            random.randint(1, 20)
        )

    for i in range(1, 201):
        db.add_ship(
            f'Ship_{i}',
            f'Weapon_{random.randint(1, 20)}',
            f'Hull_{random.randint(1, 5)}',
            f'AB-{random.randint(1, 6)}'
        )

    print(db.ships_list())
    print(db.weapons_list())
    print(db.hulls_list())
    print(db.engines_list())
